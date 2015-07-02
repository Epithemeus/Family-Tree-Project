# Finds parental relationships when given target is a direct ancestor of person
# Generations will contain the number of generations between individuals
# E.G. A parent and child have 1 generation between
# Generations must be given a value of 0 to get sensical output
# Returns true if target is direct ancestor of person
# Generations remains 0 if function returns false
def traverse_down_tree(person, target, generations):
    if person.name == target.name:
        return true
    currentGeneration = generations
    for child in person.children:
        if not traverseDownTree(child, target, generations + 1):
            generations = currentGenerations
    return False

#Work in progress!
def traverse_up_tree(person, target, generationsUp, generationsDown):
    currentGeneration = generationsDown
    if traverseDownTree(person.father, target, generationsDown):
        return True
    else:
        generationsDown = currentGeneration
    # Here I might need to account for half siblings with an elif
        
    currentGeneration = generationsUp
    
    if traverseUpTree(person.father, target, generationsUp + 1, generationsDown):
        return True
    else:
        generationsUp = currentGeneration
        
    if traverseUpTree(person.mother, target, generationsUp + 1, generationsDown):
        return True
    else:
        generationsUp = currentGeneration
                      
    return False
    
    
        
    
