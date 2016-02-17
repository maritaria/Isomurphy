import unittest
from graph.graphIO import loadgraphs
from isomorphism.ColorRefinementChecker import ColorRefinementChecker


class IsomorphTest(unittest.TestCase):
    L = loadgraphs('data\colorref_smallexample_4_7.grl')
    checker = ColorRefinementChecker()
    print(checker.isIsomorphic(L[0][0], L[0][0]))
    print(checker.isIsomorphic(L[0][0], L[0][1]))
    print(checker.isIsomorphic(L[0][0], L[0][2]))
    print(checker.isIsomorphic(L[0][0], L[0][3]))
    print(checker.isIsomorphic(L[0][1], L[0][1]))
    print(checker.isIsomorphic(L[0][1], L[0][2]))
    print(checker.isIsomorphic(L[0][1], L[0][3]))
    print(checker.isIsomorphic(L[0][2], L[0][2]))
    print(checker.isIsomorphic(L[0][2], L[0][3]))
    print(checker.isIsomorphic(L[0][3], L[0][3]))





