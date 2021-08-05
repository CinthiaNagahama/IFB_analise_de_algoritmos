from collections import defaultdict
from typing import Dict, NamedTuple


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


if __name__ == "__main__":
    g = Graph()
    g.add("1", Edge("2", 50), Edge("3", 45), Edge("4", 10, True))
    g.add("2", Edge("4", 15), Edge("3", 10))
    g.add("3", Edge("5", 30))
    g.add("4", Edge("5", 15))
    g.add("5", Edge("2", 20), Edge("3", 35))
    g.add("6", Edge("5", 3))

    print(g)
