from collections import deque
import GraphRepresentations as GR

def DFS(graph, start, visited = None):
    if visited == None:
        visited = []
    visited.append(start)
    temp = set(visited)
    for node in graph[start] - temp:
        if node not in visited:
            DFS(graph, node, visited)
    return visited

def BFS(graph, start, end): #also the shortest path problem
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



def main():
    graph = []
    with open('input.txt') as inp:
        for line in inp:
            e = inp.readline().split()
            graph.append(e)
    graph = GR.adjList(graph)

    print(graph)
    print(' ')
    print(DFS(graph, '1'))
    print(' ')
    print(DFS(graph, '12'))
    print(' ')
    t = BFS(graph,'2','6')
    print(t)
    print(' ')
    print(len(t))
    t = BFS(graph, '7', '13')
    print(t)
    print(' ')
    print(len(t))

if __name__ =="__main__": main()

