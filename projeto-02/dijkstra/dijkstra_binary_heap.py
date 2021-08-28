from collections import defaultdict
from typing import Dict, List, Tuple
import heapq
import sys

sys.path.append("../../projeto-02")

from graph import Graph


class DijkstraBinaryHeap:
    def __init__(self, graph: Graph) -> None:
        self.graph = graph
        self.paths: Dict[str, Dict[str, Tuple[str, float]]] = defaultdict(dict)

    def calculate_shortest_paths(self, source: str) -> Dict[str, Tuple[str, float]]:
        if source not in self.graph:
            raise ValueError(f"vertice {source} not found in graph {self.graph}")

        paths: Dict[str, Tuple[str, float]] = defaultdict(lambda: ("", float("inf")))
        paths[source] = ("", 0)

        vertices_dict: Dict[str, Tuple[float, str]] = dict()
        vertices_queue: List[Tuple[float, str]] = list()

        for v in self.graph:
            shared_vertice = [float("inf"), v]
            vertices_dict[v] = shared_vertice
            heapq.heappush(vertices_queue, shared_vertice)

        vertices_dict[source][0] = 0

        while len(vertices_queue) > 0:
            accumulated_distance, current_vertice = heapq.heappop(vertices_queue)

            for (next_vertice, distance) in self.graph[current_vertice].items():
                new_distance = accumulated_distance + distance
                old_distance = paths[next_vertice][1]

                if new_distance < old_distance:
                    paths[next_vertice] = current_vertice, new_distance
                    vertices_dict[next_vertice][0] = new_distance
                    heapq.heapify(vertices_queue)

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


if __name__ == "__main__":
    g = Graph.random_generator(10, 0.5)
    d = DijkstraBinaryHeap(g)
    d.calculate_shortest_paths("0")
    # print(d.build_path("A", "B"))
