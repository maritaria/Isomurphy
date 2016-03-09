from graph.graphs import Graph, Vertex, Edge
from isomorphism.IsomorphismChecker import IsomorphismChecker
from utils.lists import *

class FastPartitionRefinementChecker(IsomorphismChecker):

    #Override
    def isIsomorphic(self, graph1: Graph, graph2: Graph) -> bool:

        splitter = Splitter()
        compoments1 = splitter.split(graph1.clone())
        components2 = splitter.split(graph2.clone())



        pass


class Splitter:

    def split(self, graph : Graph) -> list:

        #TODO returns the components of a graph if the graph is not connected, otherwise returns a singleton component (the graph itself)
        components = []

        return components

    def breadthFirstFind(self, graph : Graph) -> list:

        for vertex in graph.V():
            vertex.found = False

        vertex = graph.V().pop(0)

        foundVertices = []

        def markFoundAndAppend(v : Vertex):
            v.found = True
            foundVertices.append(v)

        queue = [vertex]

        while (not isEmpty(queue)):
            newNeighbours = filter(lambda v: not v.found, vertex.nbs())
            queue = concat(queue, newNeighbours)
            markFoundAndAppend(queue.pop(0))

        return foundVertices

class Partitioner:

    def __init__(self):
        #TODO
        pass

    def parition(self, graph : Graph) -> list:
        #returns a list of color classes TODO
        pass

class ColorClass:

    def __init__(self):

        pass

    def predecendents(self) -> ColorClass:
        #TODO

        return ColorClass()

class Component:

    #represents a connected subgraph of a graph. TODO
    #can have color class information.

    def __init__(self):
        self.colorClasses = []
        self.V = []
        self.E = []
