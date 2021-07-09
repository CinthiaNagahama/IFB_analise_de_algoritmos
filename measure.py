from subprocess import run
from os import path, makedirs
import csv

if not path.exists("./sort"):
    run(["make", "build"])

makedirs(path.join(path.curdir, "data"), exist_ok=True)

for sort_method in ("merge", "heap", "bubble"):
    with open(path.join(path.curdir, "data", f"{sort_method}_sort.csv"), "w", newline="") as csv_file:
        csv_writer = csv.writer(csv_file, delimiter=";")
        csv_writer.writerow(["case", "method", "entries", "time(s)", "memory(kb)"])

    for sort_case in ("best", "random", "worst"):
        for entries in (
            (1e4, 1e5, 1e6) if sort_method == "bubble" and sort_case != "best" else (1e4, 1e5, 1e6, 1e7, 1e8, 1e9)
        ):
            run(["./memusg.py", "./sort", sort_method, sort_case, "{:.0f}".format(entries)])
