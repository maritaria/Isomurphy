from isomorphism.ColorRefinementChecker import ColorRefinementChecker
from graph.graphIO import loadgraph
from isomorphism.IndividualizationRefinementChecker import IndividualizationRefinementChecker

# L = loadgraphs('data\colorref_smallexample_4_7.grl')
# checker = ColorRefinementChecker()
# print(checker.isIsomorphic(L[0][0], L[0][1]))
# print(checker.isIsomorphic(L[0][0], L[0][2]))
# print(checker.isIsomorphic(L[0][0], L[0][3]))

L = loadgraph('data\\basicAut1.gr')
checker = IndividualizationRefinementChecker()
print(checker.countIsomorphisms(L[0], L[0]))
#print(checker.countIsomorphisms(L[0][1], L[0][2]))
#L = loadgraphs('data\\trees90.grl')
#print(checker.countIsomorphisms(L[0][0], L[0][3]))
#print(checker.countIsomorphisms(L[0][1], L[0][2]))