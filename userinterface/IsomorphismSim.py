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
		x, y ,w, h = self.bbox(tk.ALL)
		self.configure(scrollregion=(x,y,w,h))


class GraphCanvasContainer(tk.Frame):
	def __init__(self, master, g: Graph, cnf=None, **kwargs):
		tk.Frame.__init__(self, master, cnf, **kwargs)

		# setup scrollbars
		self._hscroll = tk.Scrollbar(self, orient=tk.HORIZONTAL)
		self._hscroll.grid(row=1, column=0, sticky=tk.EW)
		self._vscroll = tk.Scrollbar(self, orient=tk.VERTICAL)
		self._vscroll.grid(row=0, column=1, sticky=tk.NS)

		# setup canvas
		self._canvas = GraphCanvas(self, g, bg="yellow",
		                           xscrollcommand=self._hscroll.set,
		                           yscrollcommand=self._vscroll.set)
		self._canvas.grid(row=0, column=0, sticky=tk.NSEW)
		# This is what enables scrolling with the mouse:
		self._canvas.bind("<ButtonPress-1>", self.canvas_grab)
		self._canvas.bind("<B1-Motion>", self.canvas_drag)
		self._canvas.bind("<MouseWheel>", self.canvas_zoom)
		self._hscroll.config(command=self._canvas.xview)
		self._vscroll.config(command=self._canvas.yview)
		# make the canvas expandable
		self.grid_rowconfigure(0, weight=1)
		self.grid_columnconfigure(0, weight=1)
		self._canvas.reset_graph()

	def canvas_grab(self, event):
		self._canvas.scan_mark(event.x, event.y)

	def canvas_drag(self, event):
		self._canvas.scan_dragto(event.x, event.y, gain=1)

	def canvas_zoom(self, event):
		print(event.delta)
		delta = event.delta / 320
		delta += 1
		true_x = self._canvas.canvasx(event.x)
		true_y = self._canvas.canvasy(event.y)
		self._canvas.scale(tk.ALL, true_x, true_y , delta, delta)
		x, y ,w, h = self._canvas.bbox(tk.ALL)
		self._canvas.configure(scrollregion=(x,y,w,h))


class IsomorphismSim:
	def __init__(self, left: Graph, right: Graph):
		self._left_graph = left
		self._right_graph = right
		self.create_ui()

	def run(self):
		self._window.mainloop()

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
		self._containers = tk.PanedWindow(self._window, sashwidth=8, bg="#DDD")
		self._containers.grid(row=0, sticky=tk.NSEW)
		self._left_container = GraphCanvasContainer(self._containers, self._left_graph)
		self._containers.add(self._left_container, stretch="always")
		self._right_container = GraphCanvasContainer(self._containers, self._right_graph)
		self._containers.add(self._right_container, stretch="always")

	def create_ui_toolbar(self):
		self._stepbutton = tk.Button(self._window, text="Perform step", command=lambda: self.perform_step())
		self._stepbutton.grid(row=1, sticky=tk.SW)

	def perform_step(self):
		self._left_container._canvas._graph.addvertex()
		self._left_container._canvas.reset_graph()
		self._right_container._canvas._graph.addvertex()
		self._right_container._canvas.reset_graph()


graphs = loadgraph("../tests/data/colorref_smallexample_6_15.grl", True)

sim = IsomorphismSim(Graph(1), Graph(2))
sim.run()
