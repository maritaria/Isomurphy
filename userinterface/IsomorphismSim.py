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


class IsomorphismSim:
	def __init__(self, left: Graph, right: Graph):
		self._leftGraph = left
		self._rightGraph = right
		self.create_ui()

	def run(self):
		self.prepare_run()
		self._window.mainloop()
		self._canvas.create_circle(100, 120, 50, fill="blue", outline="#DDD", width=4)

	def prepare_run(self):
		self.clear_canvas()

	def clear_canvas(self):
		self._canvas.delete("all")

	def create_ui(self):
		self.create_ui_window()
		self.create_ui_canvas()
		self.create_ui_toolbar()

	def create_ui_window(self):
		self._window = tk.Tk()
		self._window.wm_title("IsomorphismSim")

	def create_ui_canvas(self):
		self._frame= tk.Frame(self._window)
		self._frame.pack(row=0)
		self._canvas = tk.Canvas(self._frame, width=200, height=200, bd=2, relief=tk.RIDGE, bg="RED")
		self._canvas.grid(row=0)

	def create_ui_toolbar(self):
		self._stepbutton = tk.Button(self._window, text="Perform step", command=lambda: self.perform_step())
		self._stepbutton.grid(row=1, sticky=tk.W)

	def perform_step(self):
		print("Hello World")

#TODO: New class for drawing a graph

sim = IsomorphismSim(None, None)
sim.run()