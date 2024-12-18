from collections import defaultdict

#функция для построения списка смежности из списка рёбер
def build_adjacency_list(edges):
    adjacency_list = defaultdict(list) #создаём defaultdict, где для каждого ключа будет список
    for u, v in edges: #перебираем все рёбра (u, v) в графе
        adjacency_list[u].append(v) #добавляем вершину v в список соседей вершины u
        adjacency_list[v].append(u)  #так как граф неориентированный, добавляем вершину u в список соседей вершины v
    return adjacency_list #возвращаем список смежности

#функция для поиска Эйлерова цикла в графе, заданном списком рёбер
def find_eulerian_cycle(edges, start_vertex):
    #построение списка смежности из списка рёбер
    graph = build_adjacency_list(edges)

    #проверка, что все вершины графа имеют чётную степень (необходимое условие для существования Эйлерова цикла)
    for vertex in graph:
        if len(graph[vertex]) % 2 != 0:  #если степень вершины нечётная
            print("Граф не имеет Эйлерова цикла, так как у вершины", vertex, "чётная степень")
            return [] #возвращаем пустой список, так как Эйлеров цикл невозможен

    #копируем граф, чтобы не менять исходные данные
    graph_copy = defaultdict(list)
    for vertex, neighbors in graph.items():
        graph_copy[vertex].extend(neighbors) #копируем список соседей каждой вершины

    #стек для текущего пути и список для хранения итогового Эйлерова цикла
    stack = [start_vertex] #стартуем с заданной вершины
    path = [] #cписок для хранения Эйлерова цикла

    #fлгоритм поиска Эйлерова цикла с использованием стека
    while stack:
        current_vertex = stack[-1]  #берём вершину с вершины стека

        if graph_copy[current_vertex]:  #если у вершины есть ещё неиспользованные рёбра
            next_vertex = graph_copy[current_vertex].pop() #берём одно ребро (соседнюю вершину)
            graph_copy[next_vertex].remove(current_vertex) #удаляем обратное ребро (так как граф неориентированный)
            stack.append(next_vertex) #добавляем эту вершину в стек для дальнейшего обхода
        else:
            #если у вершины больше нет рёбер, фиксируем её в цикле
            path.append(stack.pop()) #убираем вершину из стека и добавляем в путь

    #возвращаем путь в правильной последовательности (разворачиваем его)
    return path[::-1] #разворачиваем список, чтобы получить цикл в правильном порядке


if __name__ == "__main__":
    #список рёбер графа
    edges = [
        (1, 2), (1, 5), (1, 7), (1, 4), (2, 3),
        (2, 5), (2, 6), (4, 5), (5, 6), (5, 7),
        (5, 8), (6, 7), (7, 8), (6, 8), (6, 9),
        (6, 3), (8, 9) ]

    start_vertex = 5 #начинаем с вершины 5 для поиска Эйлерова цикла

    #нахождение Эйлерова цикла
    cycle = find_eulerian_cycle(edges, start_vertex)
    print("Эйлеров цикл:", cycle)