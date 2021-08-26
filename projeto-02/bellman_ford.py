from collections import defaultdict
from typing import Dict, List, Tuple
from graph import Graph


class BellmanFord:
    def __init__(self, graph: Graph) -> None:
        self.graph = graph
        self.paths: Dict[str, Dict[str, Tuple[str, float]]] = defaultdict(dict)

    def calculate_shortest_paths(self, source: str) -> Dict[str, Tuple[str, float]]:
        if source not in self.graph:
            raise ValueError(f"vertice {source} not found in graph {self.graph}")

        paths: Dict[str, Tuple[str, float]] = defaultdict(lambda: ("", float("inf")))
        paths[source] = ("", 0)

        vertices_list = list(self.graph.elements.keys())
        vertices_list.remove(source)
        vertices_list.insert(0, source)

        relaxed = True
        for _ in range(len(vertices_list) - 1):
            if not relaxed:
                break
            relaxed = False

            for vertice in vertices_list:
                accumulated_distance = paths[vertice][1]
                for relaxing_vertice, distance in self.graph[vertice].items():
                    new_distance = accumulated_distance + distance
                    if new_distance < paths[relaxing_vertice][1]:
                        paths[relaxing_vertice] = vertice, new_distance
                        relaxed = True

        self.paths[source] = paths
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
