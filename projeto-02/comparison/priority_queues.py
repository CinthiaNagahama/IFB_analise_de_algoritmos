from itertools import product
from time import time
import csv
from os import path
import sys
import numpy as np

sys.path.append("../../projeto-02")

from graph import Graph
from dijkstra.dijkstra_list import DijkstraList
from dijkstra.dijkstra_binary_heap import DijkstraBinaryHeap
from dijkstra.dijkstra_fibonacci_heap import DijkstraFibonacciHeap

# qtds = list(np.arange(10, 91, 10)) + list(np.arange(100, 1001, 100))
qtds = list(np.arange(10, 91, 10))

with open(path.join(path.curdir, "priority_queues_2.csv"), "w") as priority_queues:
    csv_writer = csv.writer(priority_queues)
    csv_writer.writerow(["Number of elements", "List", "Binary Heap", "Fibonacci Heap", "Density (%)"])

    for density, n in product((0.25, 0.5, 1), [int(qtd) for qtd in qtds]):
        # print(f"{n} elements with {int(density * 100)}% of density")
        g = Graph.random_generator(n, density)
        time_dl = []
        time_dh = []
        time_df = []

        for i in range(10):
            dl = DijkstraList(g)
            dh = DijkstraBinaryHeap(g)
            df = DijkstraFibonacciHeap(g)

            start_time = time()
            dl.calculate_shortest_paths("0")
            time_dl.append(time() - start_time)

            start_time = time()
            dh.calculate_shortest_paths("0")
            time_dh.append(time() - start_time)

            start_time = time()
            df.calculate_shortest_paths("0")
            time_df.append(time() - start_time)

        csv_writer.writerow(
            [
                n,
                f"{(sum(time_dl) / len(time_dl)):.2e}",
                f"{(sum(time_dh) / len(time_dh)):.2e}",
                f"{(sum(time_df) / len(time_df)):.2e}",
                str(int(density * 100)),
            ]
        )
