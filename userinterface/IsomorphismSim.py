import tkinter as tk

import math

from graph.graphIO import loadgraph
from graph.graphs import Graph, Vertex, Edge


def _create_circle(self, x, y, r, **kwargs):
	return self.create_oval(x - r, y - r, x + r, y + r, **kwargs)


tk.Canvas.create_circle = _create_circle


def _create_circle_arc(self, x, y, r, **kwargs):
	if "start" in kwargs and "end" in kwargs:
		kwargs["extent"] = kwargs["end"] - kwargs["start"]
		del kwargs["end"]
	return self.create_arc(x - r, y - r, x + r, y + r, **kwargs)


tk.Canvas.create_circle_arc = _create_circle_arc


class GraphCanvas(tk.Canvas):
	VERTEX_SIZE = 50
	VERTEX_HALFSIZE = 25
	VERTEX_DISTANCE = 75

	def __init__(self, master, g: Graph, cnf=None, **kwargs):
		tk.Canvas.__init__(self, master, cnf, **kwargs)
		self._graph = g
		self.reset_graph()

	def reset_graph(self):
		self.delete("all")
		self._vertices = {}
		self._edges = {}
		self._vertexPositions = {}
		for v in self._graph.V():
			self.addVertex(v)
		self.prepare_layout()
		self.layout_vertices()
		for e in self._graph.E():
			self.addEdge(e)
		self.adjust_size()

	def addVertex(self, v: Vertex):
		print("Vertex %s" % v)
		shape = self.create_oval(0, 0, 50, 50, fill="#F00", outline="black")
		self._vertices[v] = shape

	def prepare_layout(self):
		verticesCount = len(self._vertices)
		self._anglePerVertex = (2 * math.pi) / verticesCount
		self._radius = verticesCount * GraphCanvas.VERTEX_DISTANCE / (2 * math.pi)
		self._radius = max(self._radius, 3 * GraphCanvas.VERTEX_DISTANCE / (2 * math.pi))

	def layout_vertices(self):
		currentAngle = 0
		for v, shape in self._vertices.items():
			x = (math.cos(currentAngle) * self._radius)
			y = (math.sin(currentAngle) * self._radius)
			self.place_vertex(v, x, y)
			currentAngle += self._anglePerVertex

	def place_vertex(self, v, x, y):
		shape = self._vertices[v]
		x1 = x - GraphCanvas.VERTEX_HALFSIZE
		y1 = y - GraphCanvas.VERTEX_HALFSIZE
		x2 = x1 + GraphCanvas.VERTEX_SIZE
		y2 = y1 + GraphCanvas.VERTEX_SIZE
		self.coords(shape, x1, y1, x2, y2)
		self._vertexPositions[v] = (x, y)

	def addEdge(self, e: Edge):
		print("Edge %s" % e)
		x1, y1 = self._vertexPositions[e.head()]
		x2, y2 = self._vertexPositions[e.tail()]
		shape = self.create_line(x1, y1, x2, y2, fill="black", width=5)
		self._edges[e] = shape

	def adjust_size(self):
		r = self._radius + GraphCanvas.VERTEX_SIZE
		self.configure(scrollregion=(-r, -r, r, r), width= r*2, height= r*2)


class IsomorphismSim:
	def __init__(self, left: Graph, right: Graph):
		self._leftGraph = left
		self._rightGraph = right
		self.create_ui()

	def run(self):
		self._window.mainloop()

	# self._canvas.create_circle(100, 120, 50, fill="blue", outline="#DDD", width=4)

	def create_ui(self):
		self.create_ui_window()
		self.create_ui_canvas()
		self.create_ui_toolbar()

	def create_ui_window(self):
		self._window = tk.Tk()
		self._window.wm_title("IsomorphismSim")
		self._window.grid_rowconfigure(0, weight=1)
		self._window.grid_columnconfigure(0, weight=1)

	def create_ui_canvas(self):
		# create root
		self._frame = tk.Frame(self._window)
		self._frame.grid(row=0, sticky=tk.NSEW)

		# setup scrollbars
		self._vscroll = tk.Scrollbar(self._frame, orient=tk.VERTICAL)
		# self._vscroll.pack(side=tk.BOTTOM, fill=tk.X)
		self._vscroll.grid(row=0, column=1, sticky=tk.NS)
		self._hscroll = tk.Scrollbar(self._frame, orient=tk.HORIZONTAL)
		# self._hscroll.pack(side=tk.RIGHT, fill=tk.Y)
		self._hscroll.grid(row=1, column=0, sticky=tk.EW)

		# setup canvas
		self._canvas = GraphCanvas(self._frame, self._leftGraph, xscrollcommand=self._hscroll.set,
		                           yscrollcommand=self._vscroll.set, width=100, height=100, bg="yellow")
		# self._canvas.pack(fill=tk.BOTH)
		self._canvas.grid(row=0, column=0)
		# make the canvas expandable
		self._frame.grid_rowconfigure(0, weight=1)
		self._frame.grid_columnconfigure(0, weight=1)
		self._canvas.reset_graph()

	# self._canvas = tk.Canvas(self._frame, width=200, height=200, bd=2, relief=tk.RIDGE, bg="RED")
	# self._canvas.grid(row=0)

	def create_ui_toolbar(self):
		self._stepbutton = tk.Button(self._window, text="Perform step", command=lambda: self.perform_step())
		self._stepbutton.grid(row=1, sticky=tk.SW)

	def perform_step(self):
		self._canvas._graph.addvertex()
		self._canvas.reset_graph()


# TODO: New class for drawing a graph

graphs = loadgraph("../tests/data/colorref_smallexample_6_15.grl", True)

sim = IsomorphismSim(Graph(1), None)
sim.run()
