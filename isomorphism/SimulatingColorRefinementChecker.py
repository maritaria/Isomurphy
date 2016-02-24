from graph.graphs import Graph, Vertex
from isomorphism.IsomorphismChecker import IsomorphismChecker


class SimulatingColorRefinementChecker:
	def __init__(self, graph1: Graph, graph2: Graph):
		self._graph1 = graph1
		self._graph2 = graph2
		self._completed = False
		self._degreeDictionary = dict()

	def isCompleted(self) -> bool:
		return self._completed

	def prepare(self):
		self.buildDegreeDictionary()
		self._currentColor = 0
		for degree, vertices in self._degreeDictionary.items():
			for vertex in vertices:
				if not hasattr(vertex, 'colornum'):
					vertex.colornum = degree
				else:
					self._currentColor = max(vertex.colornum, self._currentColor)
			self._currentColor = max(degree, self._currentColor)
		self._currentColor += 1
		self._maxDegree = self._currentColor

	def step(self):
		checkColor = 0
		changed = False
		while checkColor < self._currentColor:
			allSameColor = self.getVerticesByColor(self._graph1, checkColor)
			allSameColor += self.getVerticesByColor(self._graph2, checkColor)
			if len(allSameColor) > 0:
				first = allSameColor.pop(0)
				changedColor = False

				verticesThatNeedAChange = set()
				while len(allSameColor) > 0:
					second = allSameColor.pop(0)
					if not (self.equalNeighborhood(first, second)):
						verticesThatNeedAChange.add(second)
						changed = True
						changedColor = True
				if changedColor:
					for vertex in verticesThatNeedAChange:
						vertex.colornum = self._currentColor
					self._currentColor += 1

			checkColor += 1
		self._completed = not changed

	def finish(self):
		self._colors1 = [0] * self._currentColor
		self._colors2 = [0] * self._currentColor
		for vertex in self._graph1.V():
			self._colors1[vertex.colornum] += 1
		for vertex in self._graph2.V():
			self._colors1[vertex.colornum] += 1

	def getColorCounts(self, g: Graph) -> dict:
		result = [0] * self._currentColor
		for v in g.V():
			result[v.colornum] += 1
		return result

	def getColors(self, g: Graph) -> dict:
		result = []
		for v in g.V():
			result[v] = v.colornum
		return result

	def isIsomorphic(self) -> bool:
		return self.getColorCounts(self._graph1) == self.getColorCounts(self._graph2)

	def buildDegreeDictionary(self) -> dict:
		self._degreeDictionary = dict()
		for vertex in self._graph1.V():
			verticesForDegree = self._degreeDictionary.get(vertex.deg(), [])
			verticesForDegree.append(vertex)
			self._degreeDictionary[vertex.deg()] = verticesForDegree
		for vertex in self._graph2.V():
			verticesForDegree = self._degreeDictionary.get(vertex.deg(), [])
			verticesForDegree.append(vertex)
			self._degreeDictionary[vertex.deg()] = verticesForDegree

	def equalNeighborhood(self, vertex1: Vertex, vertex2: Vertex) -> bool:
		return [v.colornum for v in self.quickSortByColor(vertex1.nbs())] ==\
		       [v.colornum for v in self.quickSortByColor(vertex2.nbs())]

	def quickSortByColor(self, items: list) -> list:
		if (len(items) == 0 or len(items) == 1):
			return items
		pivot = items.pop(0)
		small, big = self.partition(items, pivot.colornum)
		return self.quickSortByColor(small) + [pivot] + self.quickSortByColor(big)

	def partition(self, items: list, discriminator: int) -> (list, list):
		left = []
		right = []
		for item in items:
			if item.colornum < discriminator:
				left.append(item)
			else:
				right.append(item)
		return left, right

	def getVerticesByColor(self, graph: Graph, colornum: int):
		return [v for v in graph.V() if v.colornum == colornum]
