from graph.graphs import Graph, Vertex
from isomorphism.IsomorphismChecker import IsomorphismChecker

class ColorRefinementChecker(IsomorphismChecker):

    def isIsomorphic(self, graph1: Graph, graph2: Graph) -> bool:
        graph1Colors = makeColors(graph1)
        graph2Colors = makeColors(graph2)
        return graph1Colors == graph2Colors

def makeColors(graph: Graph):

    #Initialization. put 'colors' on each vertex from their degrees, starting from 0.
    verticesDictionary = getVerticesByDegree(graph)
    currentColor = 0
    for degree, vertices in verticesDictionary.items():
        for vertex in vertices:
            vertex.color = degree
        currentColor = max(degree, currentColor)
        
    currentColor += 1

    #iterative step keep refining
    changed = True
    while changed:
        checkColor = 0
        changed = False
        while checkColor < currentColor:
            allSameColor = getVerticesByColor(graph, checkColor)
            if len(allSameColor) > 0:
                first = allSameColor.pop(0)
                changedColor = False

                verticesThatNeedAChange = set()
                while len(allSameColor) > 0:
                    second = allSameColor.pop(0)
                    if not (equalNeighborhood(first, second)):
                        verticesThatNeedAChange.add(second)
                        changed = True
                        changedColor = True
                if changedColor:
                    for vertex in verticesThatNeedAChange:
                        vertex.color = currentColor
                    currentColor += 1

            checkColor += 1
    colors = [0] * currentColor
    for vertex in graph.V():
        colors[vertex.color] += 1
    return colors

def getVerticesByDegree(graph : Graph) -> dict:

    verticesDictionary = dict()
    for vertex in graph.V():
        verticesForDegree = verticesDictionary.get(vertex.deg(), [])
        verticesForDegree.append(vertex)
        verticesDictionary[vertex.deg()] = verticesForDegree
    return verticesDictionary

def equalNeighborhood(vertex1 : Vertex, vertex2 : Vertex) -> bool:
    return [v.color for v in quickSortByColor(vertex1.nbs())] == [v.color for v in quickSortByColor(vertex2.nbs())]

def quickSortByColor(items : list) -> list:
    if (len(items) == 0 or len(items) == 1):
        return items
    pivot = items.pop(0)
    small, big = partition(items, pivot.color)
    return quickSortByColor(small) + [pivot] + quickSortByColor(big)

def partition(items : list, discriminator : int) -> (list, list):
    left = []
    right = []
    for item in items:
        if item.color < discriminator:
            left.append(item)
        else:
            right.append(item)
    return left, right

def getVerticesByColor(graph: Graph, color: int):
    return [v for v in graph.V() if v.color == color]