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

def artPoints(graph, v, parent, cutPoints, visited, low, discovered, time = 0):
    children = 0
    visited[v] = True
    discovered[v] = time
    low[v] = time
    time += 1
    for adj in graph[v]:
        if visited[adj] == False:
            parent[adj] = v
            children += 1
            artPoints(graph, adj, parent, cutPoints, visited, low, discovered, time)
            low[v] = min(low[adj], low[v])

            if parent[v] == -1 and children > 1:
                cutPoints[v] = True
            if parent[v] != -1 and low[adj] >= discovered[v]:
                cutPoints[v] = True

        elif adj != parent[v]:
            low[v] = min(low[v], disc[adj])



graph = []
with open('input.txt') as inp:
    for line in inp:
        e = inp.readline().split()
        graph.append(e)
        e[0] = int(e[0])
        e[1] = int(e[1])
graph = adjList(graph)

print(graph)
visited = [False] * len(graph)
parent = [-1] * len(graph)
cutPoints = [False] * len(graph)
discovered = [float("Inf")]*len(graph)
low = [float("Inf")]*len(graph)

for i in range(len(graph)):
    if visited[i] == False:
        artPoints(graph, i, parent, cutPoints, visited, low, discovered)

for index, value in enumerate(cutPoints):
    if value == True:
        print (index)