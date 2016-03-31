import copy

from graph.graphIO import loadgraphs
from isomorphism.IndividualizationRefinementChecker import IndividualizationRefinementChecker

L = loadgraphs('data\\alphabet.grl')
checker = IndividualizationRefinementChecker()

for i in range(len(L[0]) - 1):
    for j in range(i + 1, len(L[0])):
        if checker.isIsomorphic(copy.deepcopy(L[0][i]), copy.deepcopy(L[0][j])):
            print(i, " and ", j, "are isomorphic")
