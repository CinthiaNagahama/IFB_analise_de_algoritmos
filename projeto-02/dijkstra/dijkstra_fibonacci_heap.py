from collections import defaultdict
from typing import Dict, List, Tuple
import sys

sys.path.append("../../projeto-02")

from graph import Graph
from lib.fib_heap import FibonacciHeap


class DijkstraFibonacciHeap:
    def __init__(self, graph: Graph) -> None:
        self.graph = graph
        self.paths: Dict[str, Dict[str, Tuple[str, float]]] = defaultdict(dict)

    def calculate_shortest_paths(self, source: str) -> Dict[str, Tuple[str, float]]:
        if source not in self.graph:
            raise ValueError(f"vertice {source} not found in graph {self.graph}")

        paths: Dict[str, Tuple[str, float]] = defaultdict(lambda: ("", float("inf")))
        paths[source] = ("", 0)
        fib_nodes: Dict[str, FibonacciHeap.Node] = dict()

        vertices_queue = FibonacciHeap()
        for v in self.graph:
            if v == source:
                fib_nodes[v] = vertices_queue.insert(0, v)
            else:
                fib_nodes[v] = vertices_queue.insert(float("inf"), v)

        while vertices_queue.total_nodes > 0:
            min_node = vertices_queue.extract_min()
            accumulated_distance, current_vertice = min_node.key, min_node.value

            for (next_vertice, distance) in self.graph[current_vertice].items():
                new_distance = accumulated_distance + distance
                old_distance = paths[next_vertice][1]

                if new_distance < old_distance:
                    paths[next_vertice] = current_vertice, new_distance
                    vertices_queue.decrease_key(fib_nodes[next_vertice], new_distance)

        self.paths[source] = dict(paths)
        return dict(paths)

    def build_path(self, source: str, destination: str) -> str:
        if source not in self.paths:
            raise ValueError(f"There are no paths calculated from source vertice: {source}")

        if destination not in self.paths[source]:
            raise ValueError(f"Destination: {destination} unreacheable from source: {source}")

        path: List[str] = list()
        current_step = destination

        while current_step != "":
            path.append(f"{current_step} ({self.paths[source][current_step][1]})")
            current_step = self.paths[source][current_step][0]

        return " -> ".join(path[::-1])
