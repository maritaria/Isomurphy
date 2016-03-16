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
        components = []
        verticesToGo = graph.V()

        for v in graph.V():
            v._found = False
        for e in graph.E():
            e._found = False

        while(not isEmpty(verticesToGo)):
            component = self.breadthFirstFind(verticesToGo)
            components.append(component)
            verticesToGo = filter(lambda v: not v._found, verticesToGo)

        for v in graph.V():
            del v._found
        for e in graph.E():
            del e._found

        return components

    def breadthFirstFind(self, vertices : list) -> Component:

        foundVertices, foundEdges = [], []

        def markFoundAndAppend(v : Vertex):
            v._found = True
            foundVertices.append(v)

            newIncidents = filter(lambda e: not e._found, v.inclist())

            for e in newIncidents:
                e._found = True
            foundEdges.extend(newIncidents)

        queue = [vertices[0]]

        while (not isEmpty(queue)):
            vertex = queue.pop(0)
            newNeighbours = filter(lambda v: not v._found, vertex.nbs())
            queue.extend(newNeighbours)
            markFoundAndAppend(vertex)

        return Component(foundVertices, foundEdges)

class Partitioner:

    def partition(self, component : Component) -> dict:
        #returns a list of color classes TODO
        partitions, lastcolor = self.getVerticesByDegree(component)
        #partitions = dictionary of <int, ColorClass> (degree, colorclass)

        colorclasses = partitions.values()
        colorclassesSorted = mergeSortBy(colorclasses, lambda x, y : len(x) - len(y))

        colorclassesByVertex = dict()
        for cclass in colorclasses:
            for v in cclass.V():
                colorclassesByVertex[v] = cclass

        queue = init(colorclassesSorted) #queue is every color class except for the biggest
        while queue: #while queue has elements
            #perform partitioning
            currentcolorclass = queue.pop(0)

            #TODO


        return partitions

    def getVerticesByDegree(self, graph : Graph) -> (dict, int):
        byDegree = dict()
        i = 0
        for v in graph.V():

            degree = v.deg()
            vertices = byDegree.get(degree, None)
            if vertices == None:
                vertices = ColorClass([])
                vertices.color = i
                i += 1
                byDegree[degree] = vertices

            vertices.addVertex(v)

        return byDegree, i


class ColorClass:

    def __init__(self, vertices, predecessors=dict()):
        self._V = vertices
        self._pre = predecessors

    def predecessors(self) -> list:
       return self._pre.keys()

    def computePredecessors(self):
        predecessors = dict()

        def pointingToVertex(vertex):
            incidents = vertex.inclist()
            for e in incidents:
                if e.head() == vertex:
                    predecessor = e.tail()
                    if not predecessor in predecessors:
                        predecessors[predecessor] = True

        for v in self._V:
            pointingToVertex(v)
        self._pre = predecessors

    def V(self):
        return self._V

    def addVertex(self, v : Vertex):
        self._V.append(v)

    def __len__(self):
        return len(self._V)


class Component:

    #represents a connected subgraph of a graph. TODO
    #can have color class information.

    def __init__(self, vertices=[], edges=[]):
        self.colorClasses = []
        self._V = vertices
        self._E = edges

    def V(self):
        return self._V

    def E(self):
        return self._E

    def colorClasses(self):
        return self.colorClasses
