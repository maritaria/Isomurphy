from graph.graphs import Graph, Vertex
from isomorphism.IsomorphismChecker import IsomorphismChecker

class ColorRefinementChecker(IsomorphismChecker):

    def isIsomorphic(self, graph1 : Graph, graph2 : Graph) -> bool:



        #TODO
        return False

def makeColors(graph : Graph) -> Graph:

    #Initialization. put 'colors' on each vertex from their degrees, starting from 1.
    verticesDictionary = getVerticesByDegree(graph)
    currentColor = 0
    for degree, vertices in verticesDictionary.items():
        currentColor += 1
        for vertex in vertices:
            vertex.color = currentColor

    #TODO iterative step keep refining


    pass

def getVerticesByDegree(graph : Graph) -> dict:

    verticesDictionary = dict()
    for vertex in graph.V():
        verticesForDegree = verticesDictionary.get(vertex.deg(), [])
        verticesForDegree.append(vertex)
    return verticesDictionary

def equalNeighbours(vertex1 : Vertex, vertex2 : Vertex) -> bool:
    return [v.color for v in quickSortByColor(vertex1.nbs())] == [v.color for v in quickSortByColor(vertex2.nbs())]

def quickSortByColor(items : list) -> list:
    if (len(items) == 0 or len(items) == 1):
        return items
    pivot = items.pop(0)
    small, big = partition(items, pivot.color);
    return quickSortByColor(small) + [pivot] + quickSortByColor(big)

def partition(items : list, discriminator : int) -> (list, list):
    left = []
    right = []
    for item in items:
        if (item.color < discriminator):
            left.append(item)
        else:
            right.append(item)
    return left, right