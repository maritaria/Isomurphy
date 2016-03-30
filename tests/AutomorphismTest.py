import unittest
from graph.graphIO import loadgraphs, writeDOT
from isomorphism.IndividualizationRefinementChecker import IndividualizationRefinementChecker

class IsomorphCountTest(unittest.TestCase):

    def setUp(self):
        self._checker = IndividualizationRefinementChecker()

    def test_cubes(self):
        self._graphs = loadgraphs('data\cubes3.grl')
        self.runTest(0, 1, 0)
        self.runTest(0, 2, 48)
        self.runTest(0, 3, 0)
        self.runTest(1, 2, 0)
        self.runTest(1, 3, 16)
        self.runTest(2, 3, 0)

    def test_cubes2(self):
        self._graphs = loadgraphs('data\cubes4.grl')
        self.runTest(0, 1, 0)
        self.runTest(0, 2, 8)
        self.runTest(0, 3, 0)
        self.runTest(1, 2, 0)
        self.runTest(1, 3, 384)
        self.runTest(2, 3, 0)

    def test_cubes3(self):
        self._graphs = loadgraphs('data\cubes5.grl')
        self.runTest(0, 1, 3840)
        self.runTest(0, 2, 0)
        self.runTest(0, 3, 0)
        self.runTest(1, 2, 0)
        self.runTest(1, 3, 0)
        self.runTest(2, 3, 24)

    def test_torus(self):
        self._graphs = loadgraphs('data\\torus24.grl')
        self.runTest(0, 3, 96)
        self.runTest(1, 2, 96)

    def runTest(self, index1: int, index2: int, expectedResult : int):
        g1 = self._graphs[0][index1].clone()
        g2 = self._graphs[0][index2].clone()
        result = self._checker.countIsomorphisms(g1, g2)
        print(index1, index2, result)
        self.assertEqual(expectedResult, result)
        if result:
            writeDOT(g1, 'cubes_' + str(index1) + '.dot')
            writeDOT(g2, 'cubes_' + str(index2) + '.dot')
