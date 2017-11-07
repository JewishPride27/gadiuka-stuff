import handyScripts as hs

def deletePath(graph, path):
   if len(path) == 2:
       graph[path[0]].remove(path[1])
       graph[path[1]].remove(path[0])
   else:
       for i in range(len(path)):
           if i != 0 and path[i] != path[-1]:
               del graph[path[i]]
       for vertex in graph:
           tempList = [x for x in graph[vertex] if x not in path]
           if path[0] in graph[vertex]:
               tempList.append(path[0])
           if path[-1] in graph[vertex]:
               tempList.append(path[-1])
           graph[vertex] = tempList

   return graph


graph = []
with open('input.txt') as inp:
    for line in inp:
        e = inp.readline().split()
        graph.append(e)
start = str(input())
end = str(input())
graph = hs.adjList(graph)
temp = graph
print(graph)
print (' ')

path_1 = hs.BFS(graph, start, end)
print(path_1)
print (' ')

temp = deletePath(temp, path_1)
print(temp)
print(' ')

path_2 = hs.BFS(temp, start, end)
print(path_2)