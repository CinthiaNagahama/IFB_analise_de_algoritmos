from collections import defaultdict
from typing import Dict, List, Tuple
import sys

sys.path.append("../../projeto-02")

from graph import Graph


class DijkstraList:
    def __init__(self, graph: Graph) -> None:
        self.graph = graph
        self.paths: Dict[str, Dict[str, Tuple[str, float]]] = defaultdict(dict)

    def calculate_shortest_paths(self, source: str) -> Dict[str, Tuple[str, float]]:
        if source not in self.graph:
            raise ValueError(f"vertice {source} not found in graph {self.graph}")

        paths: Dict[str, Tuple[str, float]] = defaultdict(lambda: ("", float("inf")))
        paths[source] = ("", 0)

        visited_vertices: List[str] = list()

        vertices_queue: List[Tuple[float, str]] = list()
        vertices_queue.append((0, source))

        while len(vertices_queue) > 0:
            accumulated_distance, current_vertice = vertices_queue.pop(vertices_queue.index(min(vertices_queue)))
            if current_vertice in visited_vertices:
                continue

            for (next_vertice, distance) in self.graph[current_vertice].items():
                new_distance = accumulated_distance + distance
                if new_distance < paths[next_vertice][1]:
                    paths[next_vertice] = current_vertice, new_distance

                vertices_queue.append((new_distance, next_vertice))

            visited_vertices.append(current_vertice)

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
