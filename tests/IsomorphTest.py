import unittest
from graph.graphIO import loadgraphs
from isomorphism.ColorRefinementChecker import ColorRefinementChecker
from isomorphism.ColorRefinementChecker import makeColors
from graph.graphIO import writeDOT


class IsomorphTest(unittest.TestCase):
    L = loadgraphs('data\colorref_smallexample_4_16.grl')
    checker = ColorRefinementChecker()
    # print(checker.isIsomorphic(L[0][0], L[0][0]))
    # print(checker.isIsomorphic(L[0][0], L[0][1]))
    # print(checker.isIsomorphic(L[0][0], L[0][2]))
    # print(checker.isIsomorphic(L[0][0], L[0][3]))
    # print(checker.isIsomorphic(L[0][1], L[0][1]))
    # print(checker.isIsomorphic(L[0][1], L[0][2]))
    # print(checker.isIsomorphic(L[0][1], L[0][3]))
    # print(checker.isIsomorphic(L[0][2], L[0][2]))
    # print(checker.isIsomorphic(L[0][2], L[0][3]))
    # print(checker.isIsomorphic(L[0][3], L[0][3]))
    for i in range(0, len(L[0])):
        for j in range(0, i):
            print("Graph", i, "and graph", j, checker.isIsomorphic(L[0][i], L[0][j]))
    writeDOT(L[0][0], 'colorful.dot')
    writeDOT(L[0][1], 'colorful1.dot')
    writeDOT(L[0][2], 'colorful2.dot')
    writeDOT(L[0][3], 'colorful3.dot')




