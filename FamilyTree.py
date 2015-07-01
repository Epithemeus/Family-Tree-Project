import csv

class Person(object):
	def __init__(self, name, mothersName, fathersName):
		self.mothersName = mothersName
		self.fathersName = fathersName
		self.name = name
		self.father = None
		self.mother = None
		self.children = []
		
	def __str__(self):
		return self.name

	def checkLowerGen(self, person, generations):
                generations = generations + 1
                if self.name = person.name:
                        return true
                for child in self.children:
                        child.checkLowerGen(person, generations)

familyTreeFile = open('RoyalFamily.csv', 'r')

reader = csv.reader(familyTreeFile, delimiter=',', quotechar='|')
familyTree = []

#This needs to be fixed
for individual in reader:
	familyTree.append(Person(individual[0], individual[2], individual[1]))

for individual in familyTree:
	for parent in familyTree:
		if individual.fathersName == parent.name:
			individual.father = parent
		elif individual.mothersName == parent.name:
			individual.mother = parent

for individual in familyTree:
	if individual.father:
		individual.father.children.append(individual)
	if individual.mother:
		individual.mother.children.append(individual)

#get names here, dummy for now
name1 = 'William Windsor'
name2 = 'Peter Phillips'

for individual in familyTree:
        if individual.name = name1:
                name1 = individual
        if individual.name = name2:
                name2 = individual

    
