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
    stop = False
    while not stop:
        execute_file(command, checker)
        cont = input("Would you like to read another file? Y/N")
        if cont == "Y":
            stop = False
        elif cont == "N":
            stop = True

def execute_file(command, checker):
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
    print("Sets of isomorphic graphs:", "Number of automorphisms:")
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
            number = checker.countIsomorphisms(L[0][isomorph[0]], L[0][isomorph[0]])
            print(isomorph, number)
            isomorph = []
        else:
            number = checker.countIsomorphisms(L[0][isomorph[0]], L[0][isomorph[1]])
            print(isomorph, number)
            isomorph = []

run()