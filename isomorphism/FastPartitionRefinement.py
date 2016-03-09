from graph.graphs import Graph
from isomorphism.IsomorphismChecker import IsomorphismChecker

class FastPartitionRefinementChecker(IsomorphismChecker):

    def isIsomorphic(self, graph1: Graph, graph2: Graph) -> bool:
        pass


class Splitter:

    def split(self, graph : "Graph") -> list:
        #returns the components of a graph if the graph is not connected, otherwise returns a singleton component (the graph itself)
        pass


class Partitioner:

    def __init__(self):

        pass

    def parition(self, graph : Graph) -> list:
        #returns a list of color classes
        pass

class ColorClass:

    def __init__(self):

        pass

class Component:
    #represents a connected subgraph of a graph.
    #can have color class information.
    pass