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
    g.add("A", Edge("B", 2), Edge("C", 3, True), Edge("D", 4))
    print(g)
    g.remove("A")
    print(g)
