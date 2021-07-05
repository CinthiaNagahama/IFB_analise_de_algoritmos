#!/usr/bin/env python3
import sys
import os
from time import sleep
from subprocess import Popen, PIPE
from pathlib import PurePath
import csv


def log(*args):
    if DEBUG:
        print(*args)


def get_rssize(sid: int) -> int:
    rssize = 0

    # Example: /bin/ps -o rssize= -o comm= --sid 23928 -> [(xxxx)kb, command]
    proc = Popen(
        ["ps", "-o", "rss=", "-o", "comm=", "--sid", str(sid)], stdout=PIPE, stderr=None, shell=False, text=True
    )
    stdout, _ = proc.communicate()

    # Iterate over each process within the process tree of our process session
    # (this ensures that we include processes launched by a child bash script, etc.)
    process_lines = [line.split() for line in stdout.split("\n") if len(line) > 0]
    log(process_lines)
    for line in process_lines:
        if line[1] not in ["python3", "ps", "sh"]:
            rssize += int(line[0])

    return rssize


DEBUG = False
try:
    child_command_name = PurePath(sys.argv[1]).name
    if sys.argv[-1] in ("-d", "--debug"):
        DEBUG = True
        child_command = sys.argv[1:-1]
    else:
        child_command = sys.argv[1:]

except IndexError:
    print("Argument(s) is missing")
    sys.exit()


log(child_command_name, child_command)

# Create a new process session for this process so that we can
# easily calculate the memory usage of the whole process tree using ps
#
# Since we need a new session using os.setsid(), we must first fork()
pid = os.getpid()
sid = os.getsid(pid)

fork_pid = os.fork()
if fork_pid == 0:
    # We *are* the new fork (not the original process)
    pid = os.getpid()
    sid = os.getsid(pid)

    os.setsid()
    sid = os.getsid(pid)

    proc = Popen(child_command, stdin=None, stdout=PIPE, stderr=None, env=None, shell=False, text=True)

    rsspeak = -1
    while proc.returncode is None:
        rsspeak = max(get_rssize(sid), rsspeak)
        proc.poll()
        sleep(0.05)  # Time in seconds (float)

    # print(f"memusg: rsspeak: {rsspeak}kb")
    with open("data.csv", "a", newline="") as csv_file:
        csv_writer = csv.writer(csv_file, delimiter=";")
        for line in proc.stdout or [""]:
            raw_line = line.strip() + " | " + str(rsspeak)
            csv_writer.writerow(entry.strip() for entry in raw_line.split("|"))

    status = proc.returncode
    sys.exit(status)

else:
    # This is the branch of fork that continues the original process
    _, full_status = os.waitpid(fork_pid, 0)
    status = full_status >> 8
    sys.exit(status)
