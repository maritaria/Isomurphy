import tkinter as tk

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
	def __init__(self, master, g : Graph, cnf=None, **kwargs):
		tk.Canvas.__init__(self, master, cnf, **kwargs)
		self._graph = g
		self.reset_graph()

	def reset_graph(self):
		self.delete("all")
		self._vertices = {}
		self._edges = {}
		for v in self._graph.V():
			self.addVertex(v)
		for e in self._graph.E():
			self.addEdge(e)

	def addVertex(self, v : Vertex):
		print("Vertex %s"%v)
		shape = self.create_oval(0, 0, 50, 50, fill="#F00",outline="black" )
		self._vertices[v] = shape

	def addEdge(self, e : Edge):
		print("Edge %s"%e)
		shape = self.create_line(0, 0, 50, 0, fill="#0F0", width=20)
		self._edges[e] = shape
		self.coords(shape, 0, 0, 50, 50)


class IsomorphismSim:
	def __init__(self, left: Graph, right: Graph):
		self._leftGraph = left
		self._rightGraph = right
		self.create_ui()

	def run(self):
		self._window.mainloop()
		#self._canvas.create_circle(100, 120, 50, fill="blue", outline="#DDD", width=4)

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
		self._frame= tk.Frame(self._window)
		self._frame.grid(row=0, sticky=tk.NSEW)

		# setup scrollbars
		self._vscroll = tk.Scrollbar(self._frame, orient=tk.VERTICAL)
		#self._vscroll.pack(side=tk.BOTTOM, fill=tk.X)
		self._vscroll.grid(row= 0, column=1,sticky=tk.NS)
		self._hscroll = tk.Scrollbar(self._frame, orient=tk.HORIZONTAL)
		#self._hscroll.pack(side=tk.RIGHT, fill=tk.Y)
		self._hscroll.grid(row=1,column=0,sticky=tk.EW)

		# setup canvas
		self._canvas = GraphCanvas(self._frame, self._leftGraph, xscrollcommand= self._hscroll.set, yscrollcommand=self._vscroll.set, width=100, height=100)
		#self._canvas.pack(fill=tk.BOTH)
		self._canvas.grid(row=0, column=0, sticky=tk.NSEW)

		self._vscroll.config(command= self._canvas.yview)
		self._hscroll.config(command= self._canvas.xview)
		# make the canvas expandable
		self._frame.grid_rowconfigure(0, weight=1)
		self._frame.grid_columnconfigure(0, weight=1)
		self._canvas.reset_graph()
		#self._canvas = tk.Canvas(self._frame, width=200, height=200, bd=2, relief=tk.RIDGE, bg="RED")
		#self._canvas.grid(row=0)

	def create_ui_toolbar(self):
		self._stepbutton = tk.Button(self._window, text="Perform step", command=lambda: self.perform_step())
		self._stepbutton.grid(row=1, sticky=tk.SW)

	def perform_step(self):
		print("Hello World")

#TODO: New class for drawing a graph

myGraph = Graph(3)
myGraph.addedge_simple(0,1)
myGraph.addedge_simple(1,2)
myGraph.addedge_simple(2,0)

sim = IsomorphismSim(myGraph, None)
sim.run()