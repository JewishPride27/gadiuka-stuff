from math import inf

def EdmondsKarp(graph, capacity, s, k):
    n = len(capacity)
    flow = 0
    Flow = [[0 for x in range(n)] for y in range(n)]
    while True:
        path = [-1 for x in range(n)]
        path[s] = -2
        m = [0 for x in range(n)]
        m[s] = inf
        queue = []
        queue.append(s)
        pathFlow, path = BFS(graph, capacity, s, k, Flow, path, m, queue)
        if pathFlow == 0:
            break
        flow = flow + pathFlow
        v = k
        while v!= s:
            u = path[v]
            Flow[u][v] = Flow[u][v] + pathFlow
            Flow[v][u] = Flow[v][u] - pathFlow
            v = u
    return flow



def BFS(graph, capacity, s, k, Flow, path, m, queue):
    while(len(queue) > 0):
        u = queue.pop()
        for v in graph[u]:
            if capacity[u][v] - Flow[u][v] > 0 and path[v] == -1:
                path[v] = u
                m[v] = min(m[u], capacity[u][v] - Flow[u][v])
                if v != k:
                    queue.append(v)
                else:
                    return m[k], path
    return 0, path



graph = []
capacity = []
#если в списке под индексом n лежит другой список, это значит, что между вершиной n и вершинами в списке есть
#направленное ребро. Лежит пустой список - значит, вершина n не соединена с другими вершинами. Почти аналогично с
#матрицей потоков: если между вершиной-индексом и вершиной в списке нет пути или это одна и та же вершина, значение
#нулевое.

with open ('input1.txt') as inp: #заполняем матрицу смежности
     for line in inp:
        e = inp.readline().split()
        e = [int(x) for x in e]
        graph.append(e)

with open ('input2.txt') as inp:
    for line in inp:
        j = inp.readline().split()
        j = [int(x) for x in j]
        capacity.append(j)

print(graph)
print(capacity)

s = 0 #source
k = 4 #sink

print(EdmondsKarp(graph, capacity, s, k))