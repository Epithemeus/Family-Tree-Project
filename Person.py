# parentsName should contain strings
# parent should contain links to corresponding parental object
# children should contain a list of links to child objects
class Person(object):
    def __init__(self, name, fathersName, mothersName, gender):
        self.mothersName = mothersName
        self.fathersName = fathersName
        self.gender = gender
        self.name = name
        self.father = None
        self.mother = None
        self.children = []
        
    def __str__(self):
        return self.name
