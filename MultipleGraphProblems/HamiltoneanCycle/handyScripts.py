from collections import deque

def countVertices(graph = []):
    saved = []
    c = 0
    for edge in graph:
        for i in range (2):
            if edge[i] not in saved:
                saved.append(edge[i])
                c+=1
            else:
                pass
    del saved
    return c

def adjMatrix(graph = []):
    v = countVertices(graph)
    m = [[0 for x in range(v)] for y in range (v)]
    for edge in graph:
        row = int(edge[0])
        column = int(edge[1])
        m[column - 1][row - 1] = 1
        m[row - 1][column - 1] = 1
    return m

def adjList (graph):
    temp = {}
    saved = []
    for edge in graph:
        for i in range(2):
            if edge[i] not in temp:
                temp[edge[i]] = set()
                temp[edge[i]].add(edge[(i + 1)%2])
                saved.append(edge[i])
            elif edge[i] in saved:
                temp[edge[i]].add(edge[(i + 1) % 2])
    del saved
    return temp

def degrees(graph):
    deg = []
    for vertex in graph:
        deg.append((len(graph[vertex])) % 2)
    return deg

def BFS(graph, start, end):
    queue = deque([start])
    while queue:
        path = list(queue.popleft())
        v = path[-1]
        if v == end:
            return path
        for neighbour in graph.get(v,[]):
            new_path = list(path)
            new_path.append(neighbour)
            queue.append(new_path)