from graph.basicgraphs import *

def complement(g : Graph):
    c = Graph()
    newVerts = {}
    for v in g.V():
        newVerts[v] = c.addvertex(str(v))
    for v, newV in newVerts.items():
        for w, newW in newVerts.items():
            if (v == w): continue
            if not w.adj(v):
                c.addedge(newV, newW)
                print("TODO: remove w from newVerts that are left if the Graph is NOT directed")
    return c