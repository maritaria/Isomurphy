from graph.graphs import *


def complement(g: Graph):
	c = Graph()
	newVerts = {}
	for v in g.V():
		newVerts[v] = c.addvertex(v.label())
	for v, newV in newVerts.items():
		for w, newW in newVerts.items():
			if v == w: continue
			if not w.adj(v):
				c.addedge(newV, newW)
			if g.isdirected() and not v.adj(w):
				c.addedge(newW, newV)
	return c
