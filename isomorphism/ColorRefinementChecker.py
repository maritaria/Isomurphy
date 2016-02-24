from graph.graphs import Graph, Vertex
from isomorphism.IsomorphismChecker import IsomorphismChecker

class ColorRefinementChecker(IsomorphismChecker):

    def isIsomorphic(self, graph1: Graph, graph2: Graph) -> bool:
        graph1Colors, graph2Colors = makeColors(graph1, graph2)
        result = graph1Colors == graph2Colors
        return result, graph1Colors

def makeColors(graph: Graph, graph2: Graph):

    #Initialization. put 'colors' on each vertex from their degrees, starting from 0.
    verticesDictionary = getVerticesByDegree(graph, graph2)
    currentColor = 0
    for degree, vertices in verticesDictionary.items():
        for vertex in vertices:
            if not hasattr(vertex, 'colornum'):
                vertex.colornum = degree
            else:
                currentColor = max(vertex.colornum, currentColor)
        currentColor = max(degree, currentColor)
    currentColor += 1
    maxDegree = currentColor

    #iterative step keep refining
    changed = True
    while changed:
        checkColor = 0
        changed = False
        while checkColor < currentColor:
            allSameColor = getVerticesByColor(graph, checkColor)
            allSameColor += getVerticesByColor(graph2, checkColor)
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
                        vertex.colornum = currentColor
                    currentColor += 1

            checkColor += 1
    colors = [0] * currentColor
    colors2 = [0] * currentColor
    for vertex in graph.V():
        colors[vertex.colornum] += 1
    for vertex in graph2.V():
        colors2[vertex.colornum] += 1
    return colors, colors2

def getVerticesByDegree(graph : Graph, graph2: Graph) -> dict:

    verticesDictionary = dict()
    for vertex in graph.V():
        verticesForDegree = verticesDictionary.get(vertex.deg(), [])
        verticesForDegree.append(vertex)
        verticesDictionary[vertex.deg()] = verticesForDegree
    for vertex in graph2.V():
        verticesForDegree = verticesDictionary.get(vertex.deg(), [])
        verticesForDegree.append(vertex)
        verticesDictionary[vertex.deg()] = verticesForDegree
    return verticesDictionary

def equalNeighborhood(vertex1 : Vertex, vertex2 : Vertex) -> bool:
    return [v.colornum for v in quickSortByColor(vertex1.nbs())] == [v.colornum for v in quickSortByColor(vertex2.nbs())]

def quickSortByColor(items : list) -> list:
    if (len(items) == 0 or len(items) == 1):
        return items
    pivot = items.pop(0)
    small, big = partition(items, pivot.colornum)
    return quickSortByColor(small) + [pivot] + quickSortByColor(big)

def partition(items : list, discriminator : int) -> (list, list):
    left = []
    right = []
    for item in items:
        if item.colornum < discriminator:
            left.append(item)
        else:
            right.append(item)
    return left, right

def getVerticesByColor(graph: Graph, colornum: int):
    return [v for v in graph.V() if v.colornum == colornum]