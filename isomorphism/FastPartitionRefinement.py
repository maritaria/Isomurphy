from graph.graphs import Graph, Vertex, Edge
from isomorphism.ColorRefinementChecker import makeColors, countColors
from isomorphism.IsomorphismChecker import IsomorphismChecker
from utils.lists import *


class FastPartitionRefinementChecker(IsomorphismChecker):
	# Override
	def isIsomorphic(self, graph1: Graph, graph2: Graph) -> (bool, list):

		self.partition(graph1)
		self.partition(graph2)

		colors1, colors2 = countColors(len(graph1.V()) * len(graph1.V()), graph1, graph2)

		return colors1 == colors2, colors1

	def partition(self, component: Graph):
		self.prepare(component)
		while self.queue:  # while queue has elements
			self.step()

	def prepare(self, component):
		# returns a list of color classes TODO
		partitions = self.prepareColorClasses(component)
		# partitions = dictionary of <int, ColorClass> (degree, colorclass)
		classes = list(partitions.values())
		self.colorclassesSorted = mergeSortBy(classes, lambda x, y: len(x) - len(y))
		self.currentMaximum = maximum(map(lambda x: x.color, classes))
		self.queue = self.colorclassesSorted.copy()# init(self.colorclassesSorted)  # queue is every color class except for the biggest

	def step(self):
		# perform partitioning
		currentcolorclass = self.queue.pop(0)
		largestColor = self.colorclassesSorted[-1].color

		def findNewVertexColor(v: Vertex) -> int:
			connected = False
			pass

		otherClasses = currentcolorclass.predecessors()
		colorAssignment = {}
		for colorClass in otherClasses:
			classAssignments = {}
			for v in colorClass.V():
				if anyMatch(lambda v1: v.adj(v1), currentcolorclass.V()):
					# connected
					newColor = self.getSpecificDegree(v, currentcolorclass)
					classAssignments[newColor] = classAssignments.get(newColor, [])
					classAssignments[newColor].append(v)
			colorAssignment[colorClass] = classAssignments
		resolvedColors = {}
		for colorClass in colorAssignment.keys():
			assignedColors = {}
			colors = colorAssignment[colorClass]
			for color in colors.keys():
				convertedColor = 0
				if color in assignedColors.keys():
					convertedColor = assignedColors[color]
				else:
					self.currentMaximum = maximum(map(lambda x: x.colornum, currentcolorclass._V[-1]._graph.V())) + 1
					convertedColor = self.currentMaximum
					assignedColors[color] = convertedColor
				for v in colors[color]:
					resolvedColors[v] = convertedColor
		for colorClass in otherClasses:
			colorClass.split(lambda v: resolvedColors.get(v, v.colornum), lambda cc: self.queue.append(cc))
			self.queue.append(colorClass)

		# TODO

	def addToQueue(self, obj):
		if obj not in self.queue:
			self.queue.append(obj)

	def getColors(self, g: Graph) -> dict:
		result = {}
		for v in g.V():
			if hasattr(v, "colornum"):
				result[v] = v.colornum
			else:
				result[v] = -1
		return result

	def prepareColorClasses(self, graph: Graph) -> (dict):
		classes = dict()
		for v in graph.V():
			color = -1
			if hasattr(v, 'colornum'):
				color = v.colornum
			else:
				color = v.deg()
			classes[color] = classes.get(color, ColorClass(color))
			classes[color].addVertex(v)

		return classes

	def getSpecificDegree(self, v : Vertex, currentcolorclass : "ColorClass") -> int:
		return len(filter(lambda edge: edge.head() in currentcolorclass.V(), v.inclist()))


class ColorClass:
	def __init__(self, color):
		self._V = []
		self.color = color

	def predecessors(self) -> list:
		# returns a list of ColorClasses
		return self.computePredecessors()

	def computePredecessors(self):
		# returns a dictionary from color(int) to colorclass
		predecessors = []

		def pointingToVertex(vertex):
			incidents = vertex.inclist()
			for e in incidents:
				if e.head() == vertex or not vertex._graph._directed:
					predecessor = e.tail()
					if predecessor.colorclass not in predecessors:
						predecessors.append(predecessor.colorclass)

		for v in self._V:
			pointingToVertex(v)
		return predecessors

	def V(self):
		return self._V

	def addVertex(self, v: Vertex):
		self._V.append(v)
		v.colorclass = self
		v.colornum = self.color

	def __len__(self):
		return len(self._V)

	def split(self, predicate, onNew):

		classes = dict()
		for v in self.V():
			newColor = predicate(v)
			classes[newColor] = classes.get(newColor, ColorClass(newColor))
			classes[newColor].addVertex(v)
			self.V().remove(v)
		for colorClass in classes.values():
			onNew(colorClass)
		return classes.values()
