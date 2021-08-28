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

qtds = list(np.arange(10, 91, 10)) + list(np.arange(100, 1001, 100))

with open(path.join(path.curdir, "priority_queues.csv"), "w") as priority_queues:
    csv_writer = csv.writer(priority_queues)
    csv_writer.writerow(["Number of elements", "List", "Binary Heap", "Fibonacci Heap", "Density (%)"])

    for density, n in product((0.25, 0.5, 1), [int(qtd) for qtd in qtds]):
        print(f"{n} elements with {int(density * 100)}% of density")
        g = Graph.random_generator(n, density)

        dl = DijkstraList(g)
        dh = DijkstraBinaryHeap(g)
        df = DijkstraFibonacciHeap(g)

        time_dl = time()
        dl.calculate_shortest_paths("0")
        time_dl = time() - time_dl

        time_dh = time()
        dh.calculate_shortest_paths("0")
        time_dh = time() - time_dh

        time_df = time()
        df.calculate_shortest_paths("0")
        time_df = time() - time_df

        csv_writer.writerow([n, f"{time_dl:.2e}", f"{time_dh:.2e}", f"{time_df:.2e}", str(int(density * 100))])
