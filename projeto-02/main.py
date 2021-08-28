from dijkstra.dijkstra_list import DijkstraList
from dijkstra.dijkstra_binary_heap import DijkstraBinaryHeap
from dijkstra.dijkstra_fibonacci_heap import DijkstraFibonacciHeap
from bellman_ford import BellmanFord
from graph import Edge, Graph
from time import time

if __name__ == "__main__":
    RUN_PART_1 = True
    RUN_PART_2 = False
    RUN_PART_3 = False

    # Comparing the different implementations of Dijkstra algorithm,
    # using a list, a binary heap, and a fibinacci heap.

    if RUN_PART_1:
        g1 = Graph()
        g1.add("A", Edge("B", 50), Edge("C", 45), Edge("D", 10, True))
        g1.add("B", Edge("C", 10))
        g1.add("C", Edge("E", 30))
        g1.add("D", Edge("B", 15), Edge("E", 15))
        g1.add("E", Edge("B", 20), Edge("C", 35))
        g1.add("F", Edge("E", 3))

        dl = DijkstraList(g1)
        exec_time = time()
        dl.calculate_shortest_paths("A")
        exec_time = time() - exec_time

        for v in g1:
            try:
                print(dl.build_path("A", v))
            except Exception as e:
                print(e)

        print(f"\nExecution Dijkstra with list: {exec_time:.2e}s\n")

        dh = DijkstraBinaryHeap(g1)
        exec_time = time()
        dh.calculate_shortest_paths("A")
        exec_time = time() - exec_time

        for v in g1:
            try:
                print(dh.build_path("A", v))
            except Exception as e:
                print(e)

        print(f"\nExecution Dijkstra with binary heap: {exec_time:.2e}s\n")

        df = DijkstraFibonacciHeap(g1)
        exec_time = time()
        df.calculate_shortest_paths("A")
        exec_time = time() - exec_time

        for v in g1:
            try:
                print(df.build_path("A", v))
            except Exception as e:
                print(e)

        print(f"\nExecution Dijkstra with fibonacci heap: {exec_time:.2e}s\n")

    # Comparing dijkstra (binary heap) with bellman-ford using a graph with negative values.

    if RUN_PART_2:
        g2 = Graph()
        g2.add("A", Edge("B", 6), Edge("C", 5), Edge("D", 5))
        g2.add("B", Edge("E", -1))
        g2.add("C", Edge("B", -2), Edge("E", 1))
        g2.add("D", Edge("C", -2), Edge("F", -1))
        g2.add("E", Edge("G", 3))
        g2.add("F", Edge("G", 3))

        d = DijkstraBinaryHeap(g2)
        exec_time = time()
        d.calculate_shortest_paths("A")
        exec_time = time() - exec_time

        print(f"\nDijkstra - Execution time ({exec_time:.2e}s):")
        for v in g2:
            try:
                print("\t" + d.build_path("A", v))
            except Exception as e:
                print("\t" + e)

        b = BellmanFord(g2)
        exec_time = time()
        b.calculate_shortest_paths("A")
        exec_time = time() - exec_time

        print(f"\nBellman-Ford - Execution time ({exec_time:.2e}s):")
        for v in g2:
            try:
                print("\t" + b.build_path("A", v))
            except Exception as e:
                print("\t" + e)

    # Final comparison between dijkstra and bell-ford using brazil's map of capital cities.
    # Distance in KM (Road-distance)

    if RUN_PART_3:
        g3 = Graph()
        g3.add(
            "Aracajú",
            Edge("Fortaleza", 1101, True),
            Edge("Maceió", 273, True),
            Edge("Salvador", 320, True),
            Edge("Teresina", 1146, True),
        )
        g3.add(
            "Belém",
            Edge("Cuiabá", 2356, True),
            Edge("Macapá", 329, True),
            Edge("Manaus", 3063, True),
            Edge("Palmas", 1230, True),
            Edge("São Luiz", 587, True),
        )
        g3.add(
            "Belo Horizonte",
            Edge("Brasília", 740, True),
            Edge("Campo Grande", 1269, True),
            Edge("Goiânia", 864, True),
            Edge("Rio de Janeiro", 442, True),
            Edge("Salvador", 1410, True),
            Edge("São Paulo", 584, True),
            Edge("Vitória", 514, True),
        )
        g3.add("Boa Vista", Edge("Macapá", 1110, True), Edge("Manaus", 748, True))
        g3.add("Brasília", Edge("Goiânia", 208, True), Edge("Salvador", 1447, True))
        g3.add(
            "Campo Grande",
            Edge("Cuiabá", 709, True),
            Edge("Curitiba", 979, True),
            Edge("Goiânia", 839, True),
            Edge("São Paulo", 987, True),
        )
        g3.add("Cuiabá", Edge("Goiânia", 898, True), Edge("Palmas", 1427, True), Edge("Porto Velho", 1459, True))
        g3.add("Curitiba", Edge("Florianópolis", 307, True), Edge("São Paulo", 495))
        g3.add("Florianópolis", Edge("Porto Alegre", 462, True))
        g3.add(
            "Fortaleza",
            Edge("João Pessoa", 709, True),
            Edge("Maceió", 949, True),
            Edge("Natal", 525, True),
            Edge("Recife", 819, True),
            Edge("Salvador", 1183, True),
            Edge("São Luiz", 887, True),
            Edge("Teresina", 595, True),
        )
        g3.add("Goiânia", Edge("Palmas", 823, True))
        g3.add("João Pessoa", Edge("Natal", 181, True), Edge("Recife", 116, True), Edge("Teresina", 1158, True))
        g3.add("Macapá", Edge("Manaus", 1054, True))
        g3.add("Maceió", Edge("Recife", 257, True), Edge("Teresina", 1194, True))
        g3.add("Manaus", Edge("Porto Velho", 889, True))
        g3.add("Natal", Edge("Teresina", 1054, True))
        g3.add("Palmas", Edge("Salvador", 1450, True), Edge("São Luiz", 1246, True), Edge("Teresina", 1107, True))
        g3.add("Porto Velho", Edge("Rio Branco", 510, True))
        g3.add("Recife", Edge("Teresina", 1128, True))
        g3.add("Rio de Janeiro", Edge("São Paulo", 433, True), Edge("Vitória", 517, True))
        g3.add("Salvador", Edge("Teresina", 1154, True), Edge("Vitória", 1172, True))
        g3.add("São Luiz", Edge("Teresina", 433, True))

        exec_times = []

        for _ in range(10):
            d = DijkstraBinaryHeap(g3)
            start_time = time()
            d.calculate_shortest_paths("Brasília")
            exec_times.append(time() - start_time)

        print(f"\nDijkstra - Execution time ({(sum(exec_times) / len(exec_times)):.2e}s):")
        for v in g3:
            try:
                print("\t" + d.build_path("Brasília", v))
            except Exception as e:
                print("\t" + e)

        exec_times.clear()

        for _ in range(10):
            b = BellmanFord(g3)
            start_time = time()
            b.calculate_shortest_paths("Brasília")
            exec_times.append(time() - start_time)

        print(f"\nBellman Ford - Execution time ({(sum(exec_times) / len(exec_times)):.2e}s):")
        for v in g3:
            try:
                print("\t" + b.build_path("Brasília", v))
            except Exception as e:
                print("\t" + e)
