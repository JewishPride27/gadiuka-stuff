from collections import deque

def adjList (graph=[]):
    temp = {}
    saved = []
    for edge in graph:
        for i in range (2):
            if edge[i] not in temp:
                temp[edge[i]] = set()
                temp[edge[i]].add(edge[(i + 1)%2])
                saved.append(edge[i])
            elif edge[i] in saved:
                temp[edge[i]].add(edge[(i + 1) % 2])
    del saved
    return temp

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