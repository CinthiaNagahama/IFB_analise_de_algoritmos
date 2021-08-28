from __future__ import annotations
from collections import defaultdict
from math import ceil
from typing import Dict, NamedTuple
from random import randint, sample


class Edge(NamedTuple):
    vertice: str
    distance: float
    bidrectional: bool = False


class Graph:
    def __init__(self) -> None:
        self.elements: Dict[str, Dict[str, float]] = defaultdict(dict)

    def __getitem__(self, key: str) -> Dict[str, float]:
        return self.elements[key]

    def __setitem__(self, key: str, value: Edge) -> None:
        self.elements[key][value.vertice] = value.distance

    def __contains__(self, key: str) -> bool:
        return key in self.elements

    def __iter__(self):
        for x in self.elements:
            yield x

    def __str__(self) -> str:
        return str(dict(self.elements))

    def add(self, vertice: str, *edges: Edge) -> None:
        for edge in edges:
            self[vertice] = edge

            if edge.vertice not in self:
                self[edge.vertice]
            if edge.bidrectional:
                self[edge.vertice] = Edge(vertice, edge.distance)

    def remove(self, vertice: str) -> None:
        self.elements.pop(vertice, dict())

        for key in self.elements:
            self.elements[key].pop(vertice, dict())

    @staticmethod
    def random_generator(vertices: int, density: float) -> Graph:
        g = Graph()
        max_num_edges = vertices * (vertices - 1) / 2
        num_edges = ceil(max_num_edges * density)
        vertice_degree = ceil((vertices - 1) * num_edges / max_num_edges)

        added_vertices = set()
        range_vertice = range(vertices)
        for src in range_vertice:
            actual_vertice_degree = vertice_degree - len(g[str(src)].values())
            added_vertices.add(src)

            reduced_sample = set(range_vertice) - added_vertices
            dests = sample(
                reduced_sample,
                actual_vertice_degree
                if actual_vertice_degree > 0 and actual_vertice_degree <= len(reduced_sample)
                else 0,
            )

            for dest in dests:
                g.add(str(src), Edge(str(dest), randint(1, 999), True))
                if len(g[str(dest)].values()) == vertice_degree:
                    added_vertices.add(dest)

        return g


if __name__ == "__main__":
    # g = Graph.random_generator(10, 0.2)
    # print(g)
    # print(len(g["0"].values()))

    for i in (0.25, 0.5, 1):
        g = Graph.random_generator(10, i)

        print(g, end="\n\n")
