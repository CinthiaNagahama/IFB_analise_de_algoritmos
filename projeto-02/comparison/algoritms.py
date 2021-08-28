from itertools import product
from time import time
import csv
from os import path
import sys
import numpy as np

sys.path.append("../../projeto-02")

from graph import Graph
from dijkstra.dijkstra_list import DijkstraList
from bellman_ford import BellmanFord

qtds = list(np.arange(10, 91, 10)) + list(np.arange(100, 1001, 100))
# qtds = list(np.arange(10, 91, 10))

with open(path.join(path.curdir, "algorithms.csv"), "w") as priority_queues:
    csv_writer = csv.writer(priority_queues)
    csv_writer.writerow(["Number of elements", "Dijkstra", "Bellman-Ford", "Density (%)"])

    for density, n in product((0.25, 0.5, 1), [int(qtd) for qtd in qtds]):
        # print(f"{n} elements with {int(density * 100)}% of density")
        g = Graph.random_generator(n, density)
        time_dl = []
        time_bf = []

        for i in range(10):
            dl = DijkstraList(g)
            bf = BellmanFord(g)

            start_time = time()
            dl.calculate_shortest_paths("0")
            time_dl.append(time() - start_time)

            start_time = time()
            bf.calculate_shortest_paths("0")
            time_bf.append(time() - start_time)

        csv_writer.writerow(
            [
                n,
                f"{(sum(time_dl) / len(time_dl)):.2e}",
                f"{(sum(time_bf) / len(time_bf)):.2e}",
                str(int(density * 100)),
            ]
        )
