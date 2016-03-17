from graph.graphs import Graph, Vertex, Edge
from isomorphism.ColorRefinementChecker import makeColors, countColors
from isomorphism.IsomorphismChecker import IsomorphismChecker
from utils.lists import *



class FastPartitionRefinementChecker(IsomorphismChecker):
	# Override
	def isIsomorphic(self, graph1: Graph, graph2: Graph) -> (bool, list):

		self.partition(graph1)
		colors1 = self.colorClasses
		self.partition(graph2)
		colors2 = self.colorClasses

		if not self.isBijection(colors1, colors2):
			return False

		colorList = []
		for color in colors1.keys():
			colorClass = colors1[color]
			for v in colorClass.V():
				v.colornum = len(colorList)
			colorList.append(len(colorClass.V()))

		return True, colorList

	def isBijection(self, colors1, colors2) -> bool:
		colors2 = list(colors2.values())
		for colorClass in colors1.values():
			for otherClass in colors2:
				if len(colorClass.V()) is len(otherClass.V()):
					colors2.remove(otherClass)
					break
		return len(colors2) is 0

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
		currentcolorclass = self.getQueuedColorClass()
		if not currentcolorclass:
			return
		#Pick new raw colors for the vertices
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
		#Turn the raw colors into colors compatible with the graph
		resolvedColors = {}
		self.currentMaximum = maximum(map(lambda x: x.colornum, currentcolorclass._V[-1]._graph.V()))
		for colorClass in colorAssignment.keys():
			assignedColors = {}
			colors = colorAssignment[colorClass]
			for color in colors.keys():
				convertedColor = 0
				if color in assignedColors.keys():
					convertedColor = assignedColors[color]
				else:
					self.currentMaximum += 1
					convertedColor = self.currentMaximum
					assignedColors[color] = convertedColor

				for v in colors[color]:
					resolvedColors[v] = convertedColor
		#Split color classes based on the assigned new colors
		for colorClass in otherClasses:
			newClasses = [colorClass]
			colorClass.split(lambda v: resolvedColors.get(v, v.colornum), lambda cc: newClasses.append(cc))
			newClasses = mergeSortBy(newClasses, lambda x, y: len(x) - len(y))
			#newClasses = init(newClasses)
			for c in newClasses:
				self.addToQueue(c)

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
		self.colorClasses = {}
		for v in graph.V():
			color = -1
			if hasattr(v, 'colornum'):
				color = v.colornum
			else:
				color = v.deg()
			self.getColorClass(color).addVertex(v)

		return self.colorClasses.copy()

	def getSpecificDegree(self, v : Vertex, currentcolorclass : "ColorClass") -> int:
		return len(filter(lambda edge: edge.head() in currentcolorclass.V(), v.inclist()))

	def getColorClass(self, color) -> "ColorClass":
		colorClass = self.colorClasses.get(color, ColorClass(self, color))
		self.colorClasses[color] = colorClass
		return colorClass

	def getQueuedColorClass(self):
		while(self.queue):
			currentcolorclass = self.queue.pop(0)
			if currentcolorclass.V():
				return currentcolorclass



class ColorClass:
	def __init__(self, colorProvider, color):
		self._V = []
		self.color = color
		self.colorProvider = colorProvider

	def __str__(self):
		return str(self.color)

	def __repr__(self):
		return str(self)

	def predecessors(self) -> list:
		# returns a dictionary from color(int) to colorclass
		predecessors = []

		for v in self._V:
			incidents = v.inclist()
			for e in incidents:
				if e.head() == v or not v._graph._directed:
					predecessor = e.tail()
					if predecessor.colorclass not in predecessors and (len(predecessor.colorclass.V()) > 1):
						predecessors.append(predecessor.colorclass)

		return predecessors

	def V(self):
		return self._V

	def addVertex(self, v: Vertex):
		self._V.append(v)
		if hasattr(v, "colorclass"):
			v.colorclass.V().remove(v)
		v.colorclass = self
		v.colornum = self.color

	def __len__(self):
		return len(self._V)

	def split(self, predicate, onNew):

		classes = dict()
		for v in self.V():
			newColor = predicate(v)
			if v.colornum is not newColor:
				classes[newColor] = classes.get(newColor, self.getColorClass(newColor))
				classes[newColor].addVertex(v)
		for colorClass in classes.values():
			onNew(colorClass)
		return classes.values()

	def getColorClass(self, color):
		return self.colorProvider.getColorClass(color)
