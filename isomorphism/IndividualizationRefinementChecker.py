import copy

from graph.graphs import Graph
from isomorphism.FastPartitionRefinement import FastPartitionRefinementChecker
from isomorphism.IsomorphismChecker import IsomorphismChecker
from isomorphism.ColorRefinementChecker import ColorRefinementChecker
from isomorphism.ColorRefinementChecker import getVerticesByColor


class IndividualizationRefinementChecker(IsomorphismChecker):
    def __init(self):
        self._checker = ColorRefinementChecker()

    def isIsomorphic(self, graph1: Graph, graph2: Graph) -> (bool, list):
        result, colorList = self._checker.isIsomorphic(graph1, graph2)
        if not result:
            return False
        for i in range(len(colorList)):
            if i == (len(colorList) - 1) and (colorList[i] == 0 or colorList[i] == 1):
                return True
            elif colorList[i] > 1:
                break
        isIso = self.findIsomorphism(graph1, graph2, colorList)
        return isIso


    def findIsomorphism(self, graph1: Graph, graph2: Graph, colorList):
        color = len(graph1.V()) + 1
        for i in range(len(colorList)):
            if colorList[i] > 1 and i < color:
                color = i
        verteces1 = getVerticesByColor(graph1, color)
        verteces2 = getVerticesByColor(graph2, color)
        vertix1 = verteces1.pop(0)
        for i in range(len(verteces2)):
            vertix2 = verteces2.pop(0)
            vertix1.colornum = len(colorList) + 1
            vertix2.colornum = len(colorList) + 1
            if self.isIsomorphic(graph1, graph2):
                return True
        return False

    def countIsomorphisms(self, graph1: Graph, graph2: Graph):
        # sim = IsomorphismSim.IsomorphismSim(copy.deepcopy(graph1), copy.deepcopy(graph2))
        # sim.run()
        result, colorList = self._checker.isIsomorphic(graph1, graph2)
        if not result:
            return 0
        bijection = True
        for i in range(len(colorList)):
            bijection = bijection and (colorList[i] == 0 or colorList[i] == 1)
        if bijection:
            return 1
        else:
            color = len(graph1.V()) + 1
            for i in range(len(colorList)):
                if colorList[i] > 1 and i < color:
                    color = i
            verteces1 = getVerticesByColor(graph1, color)
            verteces2 = getVerticesByColor(graph2, color)
            vertix1 = verteces1.pop(0)
            num = 0
            for i in range(len(verteces2)):
                vertix2 = verteces2.pop(0)
                coloring = vertix2.colornum
                vertix1.colornum = len(colorList)
                vertix2.colornum = len(colorList)
                num = num + self.countIsomorphisms(copy.deepcopy(graph1), copy.deepcopy(graph2))
                vertix1.colornum = coloring
                vertix2.colornum = coloring
            return num


