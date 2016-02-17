import unittest
from graph.graphIO import loadgraphs
from isomorphism.ColorRefinementChecker import ColorRefinementChecker


class IsomorphTest(unittest.TestCase):
    L = loadgraphs('data\colorref_smallexample_4_7.grl')
    checker = ColorRefinementChecker()
    checker.isIsomorphic(L[0][0], L[0][1])
