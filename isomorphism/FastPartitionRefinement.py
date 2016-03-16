from graph.graphs import Graph, Vertex, Edge
from isomorphism.IsomorphismChecker import IsomorphismChecker
from utils.lists import *

class FastPartitionRefinementChecker(IsomorphismChecker):

	#Override
	def isIsomorphic(self, graph1: Graph, graph2: Graph) -> bool:

		splitter = Splitter()
		components1 = splitter.split(graph1.clone())
		components2 = splitter.split(graph2.clone())

		groupedComponents1 = {}
		for comp in components1:
			id = (len(comp.V()), len(comp.E()))
			list = groupedComponents1.get(id, [])
			list.append(comp)
		groupedComponents2 = {}
		for comp in components2:
			id = (len(comp.V()), len(comp.E()))
			list = groupedComponents2.get(id, [])
			list.append(comp)

		if not self.checkPairs(groupedComponents1, groupedComponents2):
			return False

		for key in groupedComponents1.keys():
			comps1 = groupedComponents1[key]
			comps2 = groupedComponents2[key]
			if not self.checkGroupedComponents(comps1, comps2):
				return False
		return True

	def checkPairs(self, groupedComponents1, groupedComponents2) -> bool:
		for key in groupedComponents1.keys():
			value = groupedComponents1[key]
			l = len(value)
			if len(groupedComponents2.get(key, [])) is not l:
				return False
		return True

	def checkGroupedComponents(self, comps1 : list, comps2 : list)-> bool:
		partitioner = Partitioner()
		colors1 = {}
		for comp in comps1:
			colors1[comp] = partitioner.partition(comp)
		colors2 = {}
		for comp in comps2:
			colors2[comp] = partitioner.partition(comp)

		for comp in colors1.keys():
			partition = colors1[comp]
			self.removeIsometricComponent(comp, colors2)
		return len(comps2) is 0

	def removeIsometricComponent(self, targetPartition : list, colors2 : dict):
		for comp in colors2.keys():
			partition = colors2[comp]
			if (self.isIsometricPartition(targetPartition, partition)):
				colors2.pop(comp)
				return

	def isIsometricPartition(self, targetPartition : list, partition : list)->bool:

		groupedColors1 = {}
		for colorClass in targetPartition:
			l = len(colorClass.V())
			groupedColors1[l] = groupedColors1.get(l, 0) + 1
		groupedColors2 = {}
		for colorClass in partition:
			l = len(colorClass.V())
			groupedColors2[l] = groupedColors2.get(l, 0) + 1

		for classSize in groupedColors1.keys():
			vertexCount = groupedColors1[classSize]
			for otherClassSize in groupedColors2.keys():
				otherVertexCount = groupedColors2[otherClassSize]
				if (vertexCount is otherVertexCount):
					groupedColors2.pop(otherClassSize)
					break

		return len(groupedColors2) is 0


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

	def __init__(self):
		#TODO
		pass

	def partition(self, graph : Graph) -> list:
		#returns a list of color classes TODO
		pass

class ColorClass:

	def __init__(self):

		pass

	def predecendents(self) -> ColorClass:
		#TODO

		pass

class Component:

	#represents a connected subgraph of a graph. TODO
	#can have color class information.

	def __init__(self, graph : Graph, vertices=[], edges=[]):
		self.colorClasses = []
		self._G = graph
		self._V = vertices
		self._E = edges

	def V(self):
		return self._V

	def E(self):
		return self._E

	def Graph(self):
		return self._G

	def colorClasses(self):
		return self.colorClasses
