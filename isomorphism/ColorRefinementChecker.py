from graph.graphs import Graph, Vertex
from isomorphism.IsomorphismChecker import IsomorphismChecker

class ColorRefinementChecker(IsomorphismChecker):

    def isIsomorphic(self, graph1: Graph, graph2: Graph) -> bool:
        graph1Colors, degree1 = makeColors(graph1)
        graph2Colors, degree2 = makeColors(graph2)
        if degree1 != degree2:
            return False
        set1 = [set() for j in range(degree1)]
        set2 = [set() for j in range(degree2)]
        for i in range(len(graph1Colors)):
            if len(graph1Colors[i]) > 0:
                set1[graph1Colors[i].pop().deg()] = len(graph1Colors[i])
        for i in range(len(graph2Colors)):
            if len(graph2Colors[i]) > 0:
                set2[graph2Colors[i].pop().deg()] = len(graph2Colors[i])
        result = True
        for i in range(degree1):
            result = result and (set1[i] == set2[i])
        return result

def makeColors(graph: Graph):

    #Initialization. put 'colors' on each vertex from their degrees, starting from 0.
    verticesDictionary = getVerticesByDegree(graph)
    currentColor = 0
    for degree, vertices in verticesDictionary.items():
        for vertex in vertices:
            vertex.colornum = degree
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
    colors = [set() for i in range(currentColor)]
    for vertex in graph.V():
        colors[vertex.colornum].add(vertex)
    return colors, maxDegree

def getVerticesByDegree(graph : Graph) -> dict:

    verticesDictionary = dict()
    for vertex in graph.V():
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