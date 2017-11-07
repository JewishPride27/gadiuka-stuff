import handyScripts as hs


graph = []
with open('HamiltonianInput.txt') as inp:
    for line in inp:
        e = inp.readline().split()
        graph.append(e)
graph = hs.adjList(graph)
quantity = len(graph.keys())
print(graph)
print(' ')

visited = [False for x in range(quantity)]
path = []
def hamilton(curr):
    path.append(curr)
    if len(path) == quantity:
        if path[-1] in graph[path[0]] or path[0] in graph[path[-1]]:
            return True
        else:
            path.pop()
            return False
    visited[int(curr)] = True

    for next in range(quantity):
        if curr in graph[str(next)] and not visited[next]:
            if hamilton(str(next)):
                return True
    visited[int(curr)] = False
    path.pop()
    return False


hamilton('0')
print(path)
