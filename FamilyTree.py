from Person import *
from TreeReader import *
from TraversalFunctions import *

treeReader = TreeReader('RoyalFamily.csv')
familyTree = treeReader.create_tree()

for individual in familyTree:
    if individual.children:
        print(individual.name + '\'s children are ', end='')
        for child in individual.children:
            print(child.name, end=', ')
        print()
