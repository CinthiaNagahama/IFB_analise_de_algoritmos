from time import time
from random import random
import heapq
from itertools import product
import csv
from os import path
import sys

sys.path.append("../../projeto-02")

from lib.fib_heap import FibonacciHeap

qtds = (1e1, 1e2, 1e3, 1e4, 1e5)

no_heap = list()
binary_heap = list()
fib_heap = FibonacciHeap()

with open(path.join(path.curdir, "priority_queues.csv"), "w") as priority_queues:
    csv_writer = csv.writer(priority_queues)
    csv_writer.writerow(["Number of elements", "List", "Binary Heap", "Fibonacci Heap", "Measure"])

    for n in [int(qtd) for qtd in qtds]:
        print(f"For {n} numbers with additional text")

        time_l_insertion = time()
        for _ in range(n):
            r = random()
            no_heap.append((r, f"{r:.2e}"))
        time_l_insertion = time() - time_l_insertion

        time_l_deletion = time()
        while no_heap:
            _ = no_heap.pop(no_heap.index(min(no_heap)))
        time_l_deletion = time() - time_l_deletion

        print("\tList:")
        print(f"\t\tInsertion: {time_l_insertion:.2e}")
        print(f"\t\tDeletion: {time_l_deletion:.2e}")
        print(f"\t\tInsertion and deletion: {(time_l_insertion + time_l_deletion):.2e}")

        time_h_insertion = time()
        for _ in range(n):
            r = random()
            heapq.heappush(binary_heap, (r, f"{r:.2e}"))
        time_h_insertion = time() - time_h_insertion

        time_h_deletion = time()
        while binary_heap:
            _ = heapq.heappop(binary_heap)
        time_h_deletion = time() - time_h_deletion

        print("\tBinary Heap:")
        print(f"\t\tInsertion: {time_h_insertion:.2e}")
        print(f"\t\tDeletion: {time_h_deletion:.2e}")
        print(f"\t\tInsertion and deletion: {(time_h_insertion + time_h_deletion):.2e}")

        time_f_insertion = time()
        for _ in range(n):
            r = random()
            fib_heap.insert(r, f"{r:.2e}")
        time_f_insertion = time() - time_f_insertion

        time_f_deletion = time()
        while fib_heap.total_nodes > 0:
            _ = fib_heap.extract_min()
        time_f_deletion = time() - time_f_deletion

        print("\tFibonacci Heap:")
        print(f"\t\tInsertion: {time_f_insertion:.2e}")
        print(f"\t\tDeletion: {time_f_deletion:.2e}")
        print(f"\t\tInsertion and deletion: {(time_f_insertion + time_f_deletion):.2e}")

        csv_writer.writerows(
            [
                [
                    n,
                    f"{time_l_insertion:.2e}",
                    f"{time_h_insertion:.2e}",
                    f"{time_f_insertion:.2e}",
                    "insertion",
                ],
                [
                    n,
                    f"{time_l_deletion:.2e}",
                    f"{time_h_deletion:.2e}",
                    f"{time_f_deletion:.2e}",
                    "deletion",
                ],
                [
                    n,
                    f"{(time_l_insertion + time_l_deletion):.2e}",
                    f"{(time_h_insertion + time_h_deletion):.2e}",
                    f"{(time_f_insertion + time_f_deletion):.2e}",
                    "insertion and deletion",
                ],
            ]
        )
