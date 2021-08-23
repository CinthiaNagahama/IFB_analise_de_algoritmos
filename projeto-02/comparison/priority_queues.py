from time import time
from random import random
import heapq
from itertools import product
import csv
from os import path
import sys

sys.path.append("../../projeto-02")

from lib.fib_heap import FibonacciHeap

qtd = (10, 100, 1000, 10000)
text_options = (False, True)

l = list()
h = list()
f = FibonacciHeap()

with open(path.join(path.curdir, "priority_queues.csv"), "w") as priority_queues:
    csv_writer = csv.writer(priority_queues)
    csv_writer.writerow(["Number of elements", "Additional text", "List", "Binary Heap", "Fibonacci Heap"])

    for n, text in product(qtd, text_options):
        for _ in range(n):
            r = random()

            if text:
                l.append((r, f"{r:.2e}"))
                heapq.heappush(h, (r, f"{r:.2e}"))
                f.insert(r, f"{r:.2e}")
            else:
                l.append(r)
                heapq.heappush(h, r)
                f.insert(r)

        print(f"For {n} numbers" if not text else f"For {n} numbers with additional text")

        start_time_l = time()
        while l:
            _ = l.pop(l.index(min(l)))
        print(f"\tList: {(time() - start_time_l):.2e}s")

        start_time_h = time()
        while h:
            _ = heapq.heappop(h)
        print(f"\tBinary Heap: {(time() - start_time_h):.2e}s")

        start_time_f = time()
        while f.total_nodes > 0:
            _ = f.extract_min()
        print(f"\tFibonacci Heap n°2: {(time() - start_time_f):.2e}s", end="\n\n")

        csv_writer.writerow(
            [
                n,
                "Yes" if text else "No",
                f"{(time() - start_time_l):.2e}s",
                f"{(time() - start_time_h):.2e}s",
                f"{(time() - start_time_f):.2e}s",
            ]
        )
