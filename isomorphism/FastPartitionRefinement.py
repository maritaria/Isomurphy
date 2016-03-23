from graph.graphs import Graph, Vertex, Edge
from isomorphism.ColorRefinementChecker import makeColors, countColors
from isomorphism.IsomorphismChecker import IsomorphismChecker
from isomorphism.Mock import Partitioner
from utils.lists import *



class FastPartitionRefinementChecker(IsomorphismChecker):
	# Override
	def isIsomorphic(self, graph1: Graph, graph2: Graph) -> (bool, list):
		party = Partitioner(graph1, graph2)
		if not party.partition():
			return False, []

		colorList = []
		for color in party._colors.keys():
			colorClass = party._colors[color]
			count = colorClass.count()
			if (count > 0):
				for v in colorClass.V1():
					v.colornum = len(colorList)
				for v in colorClass.V2():
					v.colornum = len(colorList)
				colorList.append(count)

		return True, colorList

	def isBijection(self, colors1, colors2) -> bool:
		colors2 = list(colors2.values())
		for colorClass in colors1.values():
			for otherClass in colors2:
				if len(colorClass.V()) is len(otherClass.V()) and\
					colorClass.depth is otherClass.depth:
					colors2.remove(otherClass)
					break
		return len(colors2) is 0
