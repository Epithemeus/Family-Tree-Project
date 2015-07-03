# Finds parental relationships when given target is a direct ancestor of person
# Generations will contain the number of generations between individuals
# E.G. A parent and child have 1 generation between
# Generations must be given a value of 0 to get sensical output
# Returns true if target is direct ancestor of person
# Generations remains 0 if function returns false
def traverse_down_tree(person, target, generations):
    if person.name == target.name:
        return True
    currentGenerations = generations[0]
    for child in person.children:
        generations[0] += 1
        if not traverse_down_tree(child, target, generations):
            generations[0] = currentGenerations
        else:
            return True
    return False

#Work in progress!
#Generations should be a list with two entries both 0
#First generation entry will contain generations down the tree from common ancestor
#Second Generations entry will contain generations up the tree
#Direct Descendent relationship should be ruled out first by just use of
#traversal down tree function first
def traverse_up_tree(person, target, generations):
    currentGenerationDown = generations[0]
    generations[1] +=1

    if person.father and traverse_down_tree(person.father, target, generations):
        return True
    else:
        generations[0] = currentGenerationDown
    #This is to account for half siblings
    if person.mother and traverse_down_tree(person.mother, target, generations):
        return True
    else:
        generations[0] = currentGenerationDown
        
    currentGenerationUp = generations[1]
    
    if person.father and traverse_up_tree(person.father, target,generations):
        return True
    else:
        generations[1] = currentGenerationUp
        
    if person.mother and traverse_up_tree(person.mother, target, generations):
        return True
    else:
        generations[1] = currentGenerationUp
                      
    return False
    
    
        
    
