import GraphRepresentations as GR
import BFSandDFS as BD

def components(graph, anynode):
    component = {1:set(BD.DFS(graph, anynode))}
    vertices = set(graph.keys())
    vertices-=component[1]
    n = 1
    while vertices:
        n+=1
        x = vertices.pop()
        component[n] = set(BD.DFS(graph, x))
        vertices-=component[n]

    return component

def main():
    graph = []
    with open('input.txt') as inp:
        for line in inp:
            e = inp.readline().split()
            graph.append(e)
    graph = GR.adjList(graph)
    print(components(graph, '1'))


if __name__ == "__main__": main()