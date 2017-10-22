import handyScripts as hs

def isEulerian(graph):
    for edge in graph:
        if getDegree(graph, edge[0]) % 2 == 1 or getDegree(graph, edge[1]) % 2 == 1:
            return False
    return True

def edgeIndex(graph, vertex):
    for i in range(len(graph)):
        if (vertex == graph[i][0] or vertex == graph[i][1]):
            edge, index = graph[i], i
            break
    return index, edge

def getDegree(graph, vertex):
    degree = 0;
    for edge in graph:
        if vertex == edge[0] or vertex == edge[1]:
            degree+=1
    return degree

def eulerianCycle (graph, start):
    stack = [start]
    cycle = []

    while stack:
        v = stack[- 1]
        degree = getDegree(graph, v)

        if degree != 0:
            index, edge = edgeIndex(graph, v)
            graph.pop(index)
            stack.append(edge[1] if v == edge[0] else edge[0])
        else:
            stack.pop()
            cycle.append(v)
    return cycle


graph = []
with open('EulerianInput.txt') as inp:
    for line in inp:
        e = inp.readline().split()
        graph.append(e)

clone = graph
clone = hs.adjList(clone) #для удобства при проверке
print(graph)
print(' ')
print(clone)
print(' ')

if isEulerian(graph) == False:
    print('Wrong input')
    quit()

print(eulerianCycle(graph, '2'))


