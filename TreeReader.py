import csv
from Person import *

class TreeReader(object):
    def __init__(self, familyTreeFileName):
        familyTreeFile = open(familyTreeFileName, 'r')
        self.csvReader = csv.reader(familyTreeFile, delimiter=',', quotechar='|')

    def link_parents(self, familyTree):
        for individual in familyTree:
            for parent in familyTree:
                #At some point I'll have to account for duplicate names
                #But I could just insist my data must contain numerals I.E. George II
                if individual.fathersName == parent.name:
                    individual.father = parent
                if individual.mothersName == parent.name:
                    individual.mother = parent

    #Must be called after link_parents to get wanted results
    def link_children(self, familyTree):
        for individual in familyTree:
            if individual.father:
                individual.father.children.append(individual)
            if individual.mother:
                individual.mother.children.append(individual)

    def create_tree(self):
        familyTree = []
        for individual in self.csvReader:
            familyTree.append(Person(*individual))
        self.link_parents(familyTree)
        self.link_children(familyTree)
        return familyTree
