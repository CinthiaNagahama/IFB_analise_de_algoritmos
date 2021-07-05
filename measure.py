from subprocess import run
import csv

with open("data.csv", "w", newline="") as csv_file:
    csv_writer = csv.writer(csv_file, delimiter=";")
    csv_writer.writerow(["case", "method", "entries", "time(ms)", "memory(kb)"])

# for sort_case in ("random", "best", "worst"):
for sort_case in ["random"]:
    # for sort_method in ("merge", "heap", "bubble"):
    for sort_method in ["merge", "heap"]:
        for entries in (1e5, 1e6):
            run(["./memusg.py", "./src/sort", sort_case, sort_method, "{:.0f}".format(entries)])
