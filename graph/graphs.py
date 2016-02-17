# Modifying graphs: We will now extend basicgraphs.py. Copy the code
# in this module and call it e.g. mygraphs.py.
"""
This is a module for working with *undirected* graphs (simple graphs or multigraphs).

It contains three classes: Vertex, Edge and Graph.

The interface of these classes is extensive and allows programming all kinds of Graph algorithms.

However, the data structure used is quite basic and inefficient: a Graph object stores only a Vertex list and an Edge list, and methods such as adjacency testing / finding neighbors of a Vertex require going through the entire Edge list!
"""
# version: 29-01-2015, Paul Bonsma

unsafe = False

# Set to True for faster, but unsafe listing of all vertices and edges.

class GraphError(Exception):
	def __init__(self, message):
		self.mess = message

	def __str__(self):
		return self.mess


class Vertex:
	"""
	Vertex objects have an attribute <_graph> pointing to the Graph they are part of,
	and an attribute <_label> which can be anything: it is not used for any methods,
	except for __repr__.
	"""

	def __init__(self, graph: "Graph", label: int = 0):
		"""
		Creates a Vertex, part of <Graph>, with optional label <label>.
		(Labels of different vertices may be chosen the same; this does
		not influence correctness of the methods, but will make the string
		representation of the Graph ambiguous.)
		"""
		self._graph = graph
		self._label = label
		self._links = []
		self._nbs = {}

	def __repr__(self):
		return str(self._label)

	def adj(self, other: "Vertex") -> bool:
		"""
		Returns True iff Vertex <self> is adjacent to <other> Vertex.
		"""
		return self._nbs.get(other, 0) > 0

	def inclist(self) -> list:
		"""
		Returns the list of edges incident with Vertex <self>.
		"""
		return self._links.copy()

	def nbs(self) -> list:
		"""
		Returns the list of neighbors of Vertex <self>.
		In case of parallel edges: duplicates are not removed from this list!
		"""
		nbl = []
		for e in self.inclist():
			nbl.append(e.otherend(self))
		return nbl

	def deg(self) -> int:
		"""
		Returns the degree of Vertex <self>.
		"""
		return len(self.inclist())

	def internalAddEdge(self, edge: "Edge"):
		self._links.append(edge)
		other = edge.otherend(self)
		self._nbs[other] = self._nbs.get(other, 0) + 1

	def internalDelEdge(self, edge: "Edge"):
		self._links.remove(edge)
		other = edge.otherend(self)
		self._nbs[other] = self._nbs[other]
		if (self._nbs[other] == 0):
			self._nbs.pop(other, None)

	def label(self):
		return self._label

class Edge:
	"""
	Edges have attributes <_tail> and <_head> which point to the end vertices
	(Vertex objects). The order of these is arbitrary (undirected edges).
	"""

	def __init__(self, tail : "Vertex", head : "Vertex"):
		"""
		Creates an Edge between vertices <tail> and <head>.
		"""
		# tail and head must be Vertex objects.
		if not tail._graph == head._graph:
			raise GraphError(
				'Can only add edges between vertices of the same Graph')
		self._tail = tail
		self._head = head

	def __repr__(self):
		return '(' + str(self._tail) + ',' + str(self._head) + ')'

	def tail(self) -> Vertex:
		return self._tail

	def head(self) -> Vertex:
		return self._head

	def otherend(self, oneend: "Vertex") -> "Vertex":
		"""
		Given one end Vertex <oneend> of the Edge <self>, this returns
		the other end Vertex of <self>.
		"""
		# <oneend> must be either the head or the tail of this Edge.
		if self._tail == oneend:
			return self._head
		elif self._head == oneend:
			return self._tail
		raise GraphError(
			'Edge.otherend(oneend): oneend must be head or tail of Edge')

	def incident(self, vertex: "Vertex") -> bool:
		"""
		Returns True iff the Edge <self> is incident with the
		Vertex <Vertex>.
		"""
		if self._tail == vertex or self._head == vertex:
			return True
		else:
			return False


#TODO: Create unit tests to confirm correct behaviour
class Graph():
	"""
	A Graph object has as main attributes:
	 <_V>: the list of its vertices
	 <_E>: the list of its edges
	In addition:
	 <_simple> is True iff the Graph must stay simple (used when trying to add edges)
	 <_directed> is False for now (feel free to write a directed variant of this
	 	module)
	 <_nextlabel> is used to assign default labels to vertices.
	"""

	def __init__(self, n: int = 0, simple: bool = False):
		"""
		Creates a Graph.
		Optional argument <n>: number of vertices.
		Optional argument <simple>: indicates whether the Graph should stay simple.
		"""
		self._V = []
		self._E = []
		self._directed = False
		# may be changed later for a more general version that can also
		# handle directed graphs.
		self._simple = simple
		self._nextlabel = 0
		for i in range(n):
			self.addvertex()

	def __repr__(self):
		return 'V=' + str(self._V) + '\nE=' + str(self._E)

	def V(self) -> list:
		"""
		Returns the list of vertices of the Graph.
		"""
		if unsafe:  # but fast
			return self._V
		else:
			return self._V[:]  # return a *copy* of this list

	def E(self) -> list:
		"""
		Returns the list of edges of the Graph.
		"""
		if unsafe:  # but fast
			return self._E
		else:
			return self._E[:]  # return a *copy* of this list

	def __getitem__(self, i) -> "Vertex":
		"""
		Returns the <i>th Vertex of the Graph -- as given in the Vertex list;
		this is not related to the Vertex labels.
		"""
		return self._V[i]

	def addvertex(self, label: int = -1) -> "Vertex":
		"""
		Add a Vertex to the Graph.
		Optional argument: a Vertex label (arbitrary)
		"""
		if label == -1:
			label = self._nextlabel
			self._nextlabel += 1
		u = Vertex(self, label)
		self._V.append(u)
		return u

	def addedge(self, tail: "Vertex", head: "Vertex") -> "Edge":
		"""
		Add an Edge to the Graph between <tail> and <head>.
		Includes some checks in case the Graph should stay simple.
		"""
		if self._simple:
			if tail == head:
				raise GraphError('No loops allowed in simple graphs')
			for e in self._E:
				if (e._tail == tail and e._head == head):
					raise GraphError(
						'No multiedges allowed in simple graphs')
				if not self._directed:
					if (e._tail == head and e._head == tail):
						raise GraphError(
							'No multiedges allowed in simple graphs')
		if not (tail._graph == self and head._graph == self):
			raise GraphError(
				'Edges of a Graph G must be between vertices of G')
		e = Edge(tail, head)
		tail.internalAddEdge(e)
		head.internalAddEdge(e)
		self._E.append(e)
		return e

	def findedge(self, u: "Vertex", v: "Vertex") -> "Edge":
		"""
		If <u> and <v> are adjacent, this returns an Edge between them.
		(Arbitrary in the case of multigraphs.)
		Otherwise this returns <None>.
		"""
		for e in self._E:
			if (e._tail == u and e._head == v) or (e._tail == v and e._head == u):
				return e
		return None

	def adj(self, u: "Vertex", v: "Vertex") -> bool:
		"""
		Returns True iff vertices <u> and <v> are adjacent.
		"""
		if self.findedge(u, v) == None:
			return False
		else:
			return True

	def isdirected(self) -> bool:
		"""
		Returns False, because for now these graphs are always undirected.
		"""
		return self._directed

	def deledge(self, e: "Edge"):
		self._E.remove(e)
		e._head.internalDelEdge(e)
		e._tail.internalDelEdge(e)

	def delvertex(self, v: "Vertex"):
		for e in v.inclist():
			self.deledge(e)
		self._V.remove(v)

	def complement(self) -> "Graph":
		c = Graph()
		newVerts = {}
		for v in self.V():
			newVerts[v] = c.addvertex(v.label())
		for v, newV in newVerts.items():
			for w, newW in newVerts.items():
				if v == w: continue
				if not w.adj(v):
					c.addedge(newV, newW)
		return c

	def clone(self) -> "Graph":
		c = Graph()
		newVerts = {}
		for v in self.V():
			newVerts[v] = c.addvertex(v.label())
		for v, newV in newVerts.items():
			for w, newW in newVerts.items():
				if (v != w) and w.adj(v):
					c.addedge(newV, newW)
		return c