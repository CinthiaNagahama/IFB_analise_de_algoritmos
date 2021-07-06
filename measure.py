from subprocess import run
from os import path
import csv

if not path.exists("./sort"):
    run(["make", "build"])

with open("data.csv", "w", newline="") as csv_file:
    csv_writer = csv.writer(csv_file, delimiter=";")
    csv_writer.writerow(["case", "method", "entries", "time(s)", "memory(kb)"])

for sort_method in ["bubble"]:
    for sort_case in ["best"]:
        # for entries in (1e4, 1e5, 1e6, 1e7, 1e8, 1e9):
        for entries in [1e4, 1e5, 1e6]:
            run(["./memusg.py", "./sort", sort_method, sort_case, "{:.0f}".format(entries)])
