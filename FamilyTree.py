from Person import *
from TreeReader import *
from TraversalFunctions import *

treeReader = TreeReader('RoyalFamily.csv')
familyTree = treeReader.create_tree()

#This is to confirm traversal functions functioning
generations = [0, 0]
personName = input('Enter a name\n')
targetName = input('Enter another name\n')
person = None
target = None
for individual in familyTree:
    if individual.name == personName:
        person = individual
    if individual.name == targetName:
        target = individual

##if person and target:
##    if traverse_down_tree(person, target, generations):
##        print('There are ' + str(generations[0]) + ' generations between them')
##    elif traverse_down_tree(target, person, generations):
##        print('There are ' + str(generations[0]) + ' generations between them')
##    else:
##        print('This relationship is not parental')

if person and target:
    if traverse_up_tree(person, target, generations):
        print('Generations down ' + str(generations[0]))
        print('Generations up ' + str(generations[1]))
    else:
        print('Weird')
