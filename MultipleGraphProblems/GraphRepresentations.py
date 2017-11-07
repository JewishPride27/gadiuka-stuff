
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

def adjMatrix(graph = []):
    v = countVertices(graph)
    m = [[0 for x in range(v)] for y in range (v)]
    for edge in graph:
        row = int(edge[0])
        column = int(edge[1])
        m[column - 1][row - 1] = 1
        m[row - 1][column - 1] = 1
    return m

def incMatrix(graph = []):
    v = countVertices(graph)
    e = len(graph)
    m = [[0 for x in range(e)] for y in range(v)]
    for i in range(e):
        m[int(graph[i][0]) - 1][i] = 1
        m[int(graph[i][1]) - 1][i] = 1
    return m

def main():
    graph = []
    with open('input.txt') as inp:
        for line in inp:
            e = inp.readline().split()
            graph.append(e)

    print(graph)
    print('')
    print(countVertices(graph))
    print('')
    print(adjList(graph))
    print('')
    for elem in adjMatrix(graph):
        print(elem)
    print('')
    for elem in incMatrix(graph):
        print(elem)

if __name__ =="__main__": main()