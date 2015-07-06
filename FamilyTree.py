from TreeReader import *

class FamilyTree(object):
    def __init__(self, familyTreeFileName):
        treeReader = TreeReader(familyTreeFileName)
        self.familyTree = treeReader.create_tree()

    # Finds parental relationships when given target is a direct ancestor of person
    # Generations will contain the number of generations between individuals
    # E.G. A parent and child have 1 generation between
    # Generations must be given a value of 0 to get sensical output
    # Returns true if target is direct ancestor of person
    # Generations remains 0 if function returns false
    def traverse_down_tree(self, person, target, generations):
        if person.name == target.name:
            return True
        
        currentGenerations = generations[0]
    
        for child in person.children:
            generations[0] += 1
            if not self.traverse_down_tree(child, target, generations):
                generations[0] = currentGenerations
            else:
                return True
        return False

    #Generations should be a list with two entries both 0
    #First generation entry will contain generations down the tree from common ancestor
    #Second Generations entry will contain generations up the tree
    #Direct Descendent relationship should be ruled out first by just use of
    #traversal down tree function first
    def traverse_up_tree(self, person, target, generations):
        currentGenerationDown = generations[0]
        generations[1] +=1
        #print(person.name)
        if person.father and self.traverse_down_tree(person.father, target, generations):
            return True
        else:
            generations[0] = currentGenerationDown
        #This is to account for half siblings
        if person.mother and self.traverse_down_tree(person.mother, target, generations):
            return True
        else:
            generations[0] = currentGenerationDown
        
        currentGenerationUp = generations[1]
    
        if person.father and self.traverse_up_tree(person.father, target,generations):
            return True
        else:
            generations[1] = currentGenerationUp
        
        if person.mother and self.traverse_up_tree(person.mother, target, generations):
            return True
        else:
            generations[1] = currentGenerationUp
                      
        return False

    def find_object(self, target):
        for individual in self.familyTree:
            if individual.name == target:
                return individual

    #This function will break if generations[0] is non integer or less than 1
    def add_greats(self, generations, relation):
        if generations == 1:
            return relation

        relation = 'Grand ' + relation
        
        #Grandparent is generations = 2 so skip adding greats
        while generations > 2:
            relation = 'Great ' + relation
            generations = generations - 1

        return relation

    def find_parental_relation(self, person, target, generations):
        if self.traverse_down_tree(person, target, generations):
            if person.gender == 'Male':
                return self.add_greats(generations[0], 'Father')
            elif person.gender == 'Female':
                return self.add_greats(generations[0], 'Mother')
            else:
                return self.add_greats(generations[0], 'Parent')            
        elif self.traverse_down_tree(target, person, generations):
            if person.gender == 'Male':
                return self.add_greats(generations[0], 'Son')
            elif person.gender == 'Female':
                return self.add_greats(generations[0], 'Daughter')
            else:
                return self.add_greats(generations[0], 'Child')
        else:
            return ''

    def find_nibling_relation(self, person, generations):
        if generations[0] == 1 and person.gender == 'Male':
            return self.add_greats(generations[1], 'Nephew')
        elif generations[0] == 1 and person.gender == 'Female':
            return self.add_greats(generations[1], 'Niece')
        elif generations[0] == 1:
            return self.add_greats(generations[1], 'Nibling')
        else:
            return ''

    def find_zeroth_relation(self, person, generations):
        if generations[1] == 1 and person.gender == 'Male':
            return self.add_greats(generations[0], 'Uncle')
        elif generations[1] == 1 and person.gender == 'Female':
            return self.add_greats(generations[0], 'Aunt')
        elif generations[1] == 1:
            return self.add_greats(generations[0], 'Aunt/Uncle')
        else:
            return ''

    #This should be it's own object or something
    def add_postscript(self, number):
        number = number % 10
        if number == 1:
            return 'st'
        elif number == 2:
            return 'nd'
        elif number == 3:
            return 'rd'
        else:
            return 'th'

    def generations_removed(self, generations):
        gap = abs(generations[0] - generations[1])
        if gap == 0:
            return ''
        elif gap == 1:
            return ' Once Removed'
        elif gap == 2:
            return ' Twice Removed'
        elif gap == 3:
            return ' Thrice Removed'
        else:
            return ' ' + str(gap) + ' Times Removed'

    def find_cousin_number(self, generations):
        relation = ''
              
        if generations[0] < generations[1]:
            gap = generations[0] - 1
            relation = str(gap) + self.add_postscript(gap) + ' Cousin'
        else:
            gap = generations[1] - 1
            relation = str(gap) + self.add_postscript(gap) + ' Cousin'
        return relation + self.generations_removed(generations)
            

    def find_non_parental_relation(self, person, target, generations):
        if self.traverse_up_tree(person, target, generations):
            relation = self.find_nibling_relation(person, generations)
            if relation:
                return relation
            relation = self.find_zeroth_relation(person, generations)
            if relation:
                return relation
            relation = self.find_cousin_number(generations)
            if relation:
                return relation
        else:
            return ''
        
    def find_relationship(self, personName, targetName):
        person = self.find_object(personName)
        target = self.find_object(targetName)
        if not person or not target:
            return 'Name not found'
        generations = [0,0]

        relation = self.find_parental_relation(person, target, generations)
        if relation:
            return relation

        relation = self.find_non_parental_relation(person, target, generations)
        if relation:
            return relation

        
        
    
        
    
