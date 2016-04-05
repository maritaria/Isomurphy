import copy

from graph.graphIO import loadgraphs
from isomorphism.ColorRefinementChecker import ColorRefinementChecker
from isomorphism.FastPartitionRefinement import FastPartitionRefinementChecker
from isomorphism.IndividualizationRefinementChecker import IndividualizationRefinementChecker


def run():
    checker = IndividualizationRefinementChecker()
    command = None
    chosen_coloring = False
    while not chosen_coloring:
        coloring = input("Would you like to 1. Use normal Coloring or 2. Use fast Coloring")
        if coloring == "1":
            checker._checker = ColorRefinementChecker()
            chosen_coloring = True
        elif coloring == "2":
            checker._checker = FastPartitionRefinementChecker()
            chosen_coloring = True
        else:
            print("Please pick either 1 or 2")
    chosen_mode = False
    while not chosen_mode:
        mode = input("Would you like to 1. Find an isomorphism or 2. Count the automorphisms")
        if mode == "1":
            command = "isIsomorphic"
            chosen_mode = True
        elif mode == "2":
            command = "countIsomorphisms"
            chosen_mode = True
        else:
            print("Please pick either 1 or 2")
    name = input("What file would you like to use?")
    L = loadgraphs(name)
    if command == "isIsomorphic":
        isomorphism(checker, L)
    elif command == "countIsomorphisms":
        automorphism(checker, L)

def isomorphism(checker, L):
    print("Sets of isomorphic graphs:")
    isomorph = []
    toCheck = []
    checking = []
    for i in range(len(L[0])):
        toCheck.append(i)
    while len(toCheck) > 0:
        checking = toCheck
        toCheck = []
        isomorph.append(checking[0])
        for j in range(1, len(checking)):
            if checker.isIsomorphic(copy.deepcopy(L[0][checking[0]]), copy.deepcopy(L[0][checking[j]])):
                isomorph.append(checking[j])
            else:
                toCheck.append(checking[j])
        if len(isomorph) <= 1:
            isomorph = []
        else:
            print(isomorph)
            isomorph = []


def automorphism(checker, L):
     for i in range(len(L[0]) - 1):
        for j in range(i + 1, len(L[0])):
            if checker.countIsomorphism(copy.deepcopy(L[0][i]), copy.deepcopy(L[0][j])):
                print(i, " and ", j, "are isomorphic")


run()