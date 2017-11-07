from GraphRepresentations import adjList
import FindingTheComponent as FTC
from BFSandDFS import DFS

def degrees(graph):
    deg = []
    for vertex in graph:
        deg.append((len(graph[vertex])) % 2)
    return deg

dominoes = []
quantity = int(input())
for edge in range(quantity):
    edge = input().split()
    dominoes.append(edge)
clone = adjList(dominoes)
d = degrees(clone)
c = 0
for x in d:
    if x % 2 == 1:
        c+=1
comp = FTC.components(clone, dominoes[0][0])

print(clone)
print(' ')
print(d)
print(' ')
print(comp)

if c <= 2 and len(comp) == 1:
    print("Yes")
else:
    print("No")

