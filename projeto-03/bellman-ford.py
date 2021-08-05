from collections import defaultdict
from typing import Dict, List, Tuple
from graph import Edge, Graph


class Bellman_ford:
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

        for _ in range(len(vertices_list) - 1):
            for vertice in vertices_list:
                accumulated_distance = paths[vertice][1]
                for relaxing_vertice, distance in self.graph[vertice].items():
                    new_distance = accumulated_distance + distance
                    if new_distance < paths[relaxing_vertice][1]:
                        paths[relaxing_vertice] = vertice, new_distance

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


if __name__ == "__main__":

    g = Graph()
    g.add("1", Edge("2", 6), Edge("3", 5), Edge("4", 5))
    g.add("2", Edge("5", -1))
    g.add("3", Edge("2", -2), Edge("5", 1))
    g.add("4", Edge("3", -2), Edge("6", -1))
    g.add("5", Edge("7", 3))
    g.add("6", Edge("7", 3))

    print(g)
    b = Bellman_ford(g)
    b.calculate_shortest_paths("1")

    for v in g:
        try:
            print(b.build_path("1", v))
        except Exception as e:
            print(e)
