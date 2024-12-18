# AllForGraphs Library #

## What is this? ##
allforgraphs – это библиотека для работы с графами и построением матриц. Она включает в себя два модуля: алгоритмы для задач с графами и методы генерации матриц.

## Quick Guide ##
### Структура библиотеки ###

allforgraphs состоит из двух модулей:

1. algorithms - Модуль для работы с алгоритмами графа.
2. matrices - Модуль для работы с матрицами, связанными с графами.

## Installation ## 

Чтобы начать работу с allforgraphs, установите её через pip:

```pip install allforgraphs2```


## Using ##

После установки библиотеку можно импортировать с помощью:

``` python
from allforgraphs import *
```

## Modules Overview ##

### Algorithms Module ###

#### Функция find_shortest_path(edges_input, start_node, end_node) позволяет находить кратчайший путь между двумя узлами в ориентированном графе, используя алгоритм Дейкстры. #####

Параметры:

1. edges_input: список рёбер графа, где каждое ребро представлено кортежем (weight, node1, node2), где weight — это вес ребра, а node1 и node2 — вершины, соединённые этим ребром.
2. start_node: узел, от которого начинается поиск кратчайшего пути.
3. end_node: узел, до которого необходимо найти путь.

Возвращает:
Кортеж, содержащий кратчайшее расстояние и сам путь в виде списка узлов.

Пример использования: 

``` python
from allforgraphs.algorithms.dr import find_shortest_path

edges_input = [
    (11, 3, 1), (5, 4, 3), (8, 5, 4), (12, 6, 5), (3, 8, 6), 
    (14, 8, 20), (7, 19, 20), (2, 19, 7), (9, 2, 7), (4, 1, 2),
    (10, 7, 32), (6, 32, 31), (15, 32, 34), (13, 31, 7), 
    (1, 34, 31), (8, 19, 21), (11, 21, 20), (7, 29, 8), 
    (2, 29, 30), (5, 33, 29), (14, 8, 30), (6, 30, 33), 
    (12, 31, 22), (3, 24, 22), (9, 22, 25), (5, 26, 24), 
    (7, 25, 26), (13, 26, 23), (1, 23, 30), (4, 26, 27), 
    (8, 27, 28), (2, 23, 28), (10, 11, 12), (15, 13, 14), 
    (12, 16, 15), (6, 18, 17)
]
start_node = 34
end_node = 8

distance, path = find_shortest_path(edges_input, start_node, end_node)
print(f"Кратчайшее расстояние от {start_node} до {end_node}: {distance}")
print(f"Путь: {' -> '.join(map(str, path))}")
```

#### Функция kruskal_maximum_tree(edges_input) реализует алгоритм Краскала для нахождения максимального охватывающего дерева в графе ####

Параметры:

1. edges_input: список рёбер графа в формате (weight, node1, node2), где weight — это вес ребра, а node1 и node2 — вершины, соединённые этим ребром.

Возвращает:
Кортеж, содержащий список рёбер максимального покрывающего дерева и его общий вес.

Пример использования: 

``` python
from allforgraphs.algorithms.kr_max import kruskal_maximum_tree

edges_input = [
    (9, 0, 1), (12, 0, 2), (10, 1, 2), (15, 1, 3),
    (5, 2, 3), (20, 2, 4), (25, 3, 4), (30, 4, 5)
]

max_tree_edges, max_tree_weight = kruskal_maximum_tree(edges_input)

print('Максимальное покрывающее дерево:')
for edge in max_tree_edges:
    print(f'Вес: {edge[0]}, Вершины: ({edge[1]}, {edge[2]})')

print('Общий вес максимального покрывающего дерева:', max_tree_weight)
```

#### Функция kruskal_minimum_tree(edges_input) реализует алгоритм Краскала для нахождения минимального охватывающего дерева в графе. ####

Параметры:

1. edges_input: список рёбер графа в формате (weight, node1, node2), где weight — это вес ребра, а node1 и node2 — вершины, соединённые этим ребром.

Возвращает:
Кортеж, содержащий список рёбер минимального покрывающего дерева и его общий вес.

Пример использования: 

``` python
from allforgraphs.algorithms.kr_min import kruskal_minimum_tree

edges_input = [
    (11, 3, 1), (5, 4, 3), (8, 5, 4), (12, 6, 5), (3, 8, 6),
    (14, 8, 20), (7, 19, 20), (2, 19, 7), (9, 2, 7), (4, 1, 2),
    (10, 7, 32), (6, 32, 31), (15, 32, 34), (13, 31, 7), (1, 34, 31),
    (8, 19, 21), (11, 21, 20), (7, 29, 8), (2, 29, 30), (5, 33, 29),
    (14, 8, 30), (6, 30, 33), (12, 31, 22), (3, 24, 22), (9, 22, 25),
    (5, 26, 24), (7, 25, 26), (13, 26, 23), (1, 23, 30), (4, 26, 27),
    (8, 27, 28), (2, 23, 28), (10, 11, 12), (15, 13, 14), (12, 16, 15),
    (6, 18, 17)
]

min_tree_edges, min_tree_weight = kruskal_minimum_tree(edges_input)

print('Минимальное покрывающее дерево:')
for edge in min_tree_edges:
    print(f'Вес: {edge[0]}, Вершины: ({edge[1]}, {edge[2]})')

print('Общий вес минимального покрывающего дерева:', min_tree_weight)
```

#### Метод prima_maximum_covering_tree реализует алгоритм Прима для построения максимального покрывающего дерева на основе заданного графа. ####

Класс Graph_1 используется для представления графа, который инициализируется списком рёбер. Каждый элемент рёбер представляет собой кортеж, содержащий вес ребра и узлы, которые оно соединяет.

Параметры: Не имеет параметров, так как использует внутреннее состояние объекта Graph, включающее список рёбер, узлы и другие переменные.

Возвращает:

1. total_weight: Общий вес максимального покрывающего дерева (целое число). 
2. tree_ribs: Список рёбер, входящих в максимальное покрывающее дерево. Каждый элемент списка представляет собой кортеж (узел1, узел2, вес).

Пример использования: 

``` python
from allforgraphs.algorithms.prima_max import prima_maximum_covering_tree

E = [
        (18, 1, 2), (14, 2, 3), (23, 4, 5), (12, 5, 6),
        (16, 1, 6), (28, 6, 8), (24, 8, 9), (3, 9, 10)
    ]
    
    graph = Graph_1(E)
    total_weight, max_tree_ribs = graph.prima_maximum_covering_tree()

    print("Общий вес максимального покрывающего дерева:", total_weight)
    print("Рёбра максимального покрывающего дерева:")
    for u, v, weight in max_tree_ribs:
        print(f"Вес: {weight}, Ребро: ({u}, {v})")
```

#### Метод prima_minimum_covering_tree реализует алгоритм Прима для построения минимального покрывающего дерева. ####

Класс Graph используется для представления графа, который инициализируется списком рёбер. Каждый элемент рёбер представляет собой кортеж, содержащий вес ребра и узлы, которые оно соединяет.

Параметры: Не имеет параметров, так как использует внутреннее состояние объекта Graph_2, включающее список рёбер, узлы и другие переменные.

Возвращает: 
1. total_weight: Общий вес минимального покрывающего дерева (целое число).
2. min_tree_ribs: Список рёбер, входящих в минимальное покрывающее дерево, заданный в формате (узел1, узел2, вес)

Пример использования: 

``` python
from allforgraphs.algorithms.prima_min import prima_minimum_covering_tree

E = [
        (1, 1, 3), (1, 2, 6), (2, 2, 4),
        (3, 1, 5), (4, 3, 4), (5, 4, 5),
        (6, 3, 5), (7, 1, 2), (7, 4, 6)
    ]
    
    graph = Graph_2(E)
    total_weight, min_tree_ribs = graph.prima_minimum_covering_tree()

    print("Общий вес минимального покрывающего дерева:", total_weight)
    print("Рёбра минимального покрывающего дерева:")
    for u, v, weight in min_tree_ribs:
        print(f"Вес: {weight}, Ребро: ({u}, {v})")
```

#### Функция find_eulerian_cycle находит Эйлеров цикл в неориентированном графе, заданном списком рёбер. ####

Параметры:

1. edges: Список рёбер графа, где каждое ребро представлено как кортеж (узел1, узел2).
2. start_vertex: Узел, с которого начинается поиск Эйлерова цикла.

Возвращает:

1. path: Список вершин, представляющий Эйлеров цикл. Если Эйлеров цикл отсутствует, возвращается пустой список.

Пример использования: 

``` python
from allforgraphs.algorithms.euler_gr import find_eulerian_cycle

    edges = [
        (1, 2), (1, 5), (1, 7), (1, 4), (2, 3),
        (2, 5), (2, 6), (4, 5), (5, 6), (5, 7),
        (5, 8), (6, 7), (7, 8), (6, 8), (6, 9),
        (6, 3), (8, 9)
    ]

    start_vertex = 5

    cycle = find_eulerian_cycle(edges, start_vertex)
    print("Эйлеров цикл:", cycle)
```

### Matrices Module ###

##### Функция build_incidence_matrix(edges) строит матрицу инцидентности для графа, заданного списком рёбер. ####

Параметры:

1. edges: список рёбер графа в формате (weight, node1, node2), где weight — это вес ребра, а node1 и node2 — вершины, соединённые этим ребром.

Возвращает:
Матрицу инцидентности в виде списка списков. Если список рёбер пуст, возвращает None.


Пример использования:

``` python
from allforgraphs.matrices.matr_sm import build_incidence_matrix

edges = [
    (5, 1, 2),
    (0, 1, 3),
    (4, 2, 3),
    (3, 3, 4),
    (2, 4, 1),
    (0, 2, 4)
]

incidence_matrix = build_incidence_matrix(edges)

if incidence_matrix:
    print("Матрица инцидентности:")
    print(incidence_matrix)
else:
    print("Список рёбер пуст.")
```

#### Функция build_adjacency_matrix(edges) строит матрицу смежности для графа, заданного списком рёбер. ####

Параметры:

1. edges: список рёбер графа в формате (weight, node1, node2), где weight — это вес ребра, а node1 и node2 — вершины, соединённые этим ребром.

Возвращает:
Матрицу смежности в виде списка списков. Если список рёбер пуст или не содержит рёбер с ненулевым весом, возвращает None.

Пример использования: 

``` python
from allforgraphs.matrices.matr_sm import build_adjacency_matrix

edges = [
    (5, 1, 2),
    (0, 1, 3),
    (4, 2, 3),
    (3, 3, 4),
    (2, 4, 1),
    (0, 2, 4)
]

adjacency_matrix = build_adjacency_matrix(edges)

if adjacency_matrix:
    print("Матрица смежности:")
    print(adjacency_matrix)
else:
    print("Список рёбер пуст.")
```

#### Функция build_weight_matrix(edges) строит матрицу весов для графа, заданного списком рёбер. ####

Параметры:

1. edges: список рёбер графа в формате (weight, node1, node2), где weight — это вес ребра, а node1 и node2 — вершины, соединённые этим ребром.

Возвращает:
Матрицу весов в виде списка списков. Если список рёбер пуст, возвращает None. Веса, отсутствующие в графе, инициализируются значением бесконечности (inf). Для диаметрических рёбер диагональные элементы устанавливаются в 0.

Пример использования: 

``` python
from allforgraphs.matrices.matr_sm import build_weight_matrix

edges = [
    (5, 1, 2),
    (10, 1, 3),
    (0, 2, 3),
    (7, 3, 4),
    (2, 4, 1),
    (3, 2, 4)
]

weight_matrix = build_weight_matrix(edges)

if weight_matrix:
    print("Матрица весов:")
    print(weight_matrix)
else:
    print("Список рёбер пуст.")
```

#### Функция transitive_closure(edges, num_vertices) вычисляет матрицу транзитивного замыкания для графа, заданного списком рёбер. ####

Параметры:

1. edges: список рёбер графа в формате (weight, node1, node2), где weight — это вес ребра, а node1 и node2 — вершины, соединённые этим ребром.
2. num_vertices: общее количество вершин в графе.

Возвращает:
Матрицу транзитивного замыкания в виде списка списков, где значение 1 указывает на наличие пути между вершинами, а 0 — на отсутствие пути.

Пример использования: 

``` python
from allforgraphs.matrices.matr_sm import transitive_closure

edges_input = [
    (5, 1, 2), (4, 2, 4), (4, 2, 3), (7, 3, 1)
]

num_vertices = max(max(i, j) for _, i, j in edges_input)

closure_matrix = transitive_closure(edges_input, num_vertices)

print("Матрица транзитивного замыкания:")
for row in closure_matrix:
    print(" ".join(map(str, row)))
```

#### Функция floyd_warshall(edges, num_vertices) реализует алгоритм Флойда-Уоршелла для нахождения кратчайших расстояний между всеми парами вершин в графе. ####

Параметры:

1. edges: список рёбер графа в формате (weight, node1, node2), где weight — это вес ребра, а node1 и node2 — вершины, соединённые этим ребром.
2. num_vertices: общее количество вершин в графе.

Возвращает:
Матрицу расстояний в виде списка списков, где значение на позиции [i][j] представляет кратчайшее расстояние от вершины i до вершины j. Если путь отсутствует, значение будет равно float('inf').

Пример использования: 

``` python
from allforgraphs.matrices.matr_sm import floyd_warshall

edges_input = [
    (2, 1, 2), (1, 2, 3), (6, 2, 3), (1, 3, 1), (5, 1, 3)
]

num_vertices = max(max(i, j) for _, i, j in edges_input)
shortest_paths_matrix = floyd_warshall(edges_input, num_vertices)

print("Матрица кратчайших расстояний:")
for row in shortest_paths_matrix:
    print(" ".join(map(lambda x: f"{x:5}" if x != float('inf') else " INF", row)))
```

## Developers ##

Авторы библиотеки: Бызова Мария, Верниковская Екатерина, Ольга Калашникова. 

GitHub Бызовой Марии: [link](https://github.com/mobyzova)

GitHub Верниковской Екатерины: [link](https://github.com/Katerok27153)

GitHub Калашниковой Ольги: [link](https://github.com/lacrimell)
