from graph.graphs import Graph
from isomorphism.IsomorphismChecker import IsomorphismChecker

class ColorRefinementChecker(IsomorphismChecker):

    def isIsomorphic(self, graph1 : Graph, graph2 : Graph) -> bool:



        #TODO
        return False;

def makeColors(graph : Graph) -> Graph:

    #Initialization. put 'colors' on each vertex from their degrees, starting from 1.
    verticesDictionary = getVerticesByDegree(graph)
    currentColor = 0
    for (degree, vertices) in verticesDictionary.items():
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



