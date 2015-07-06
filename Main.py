from FamilyTree import *
from tkinter import *
from tkinter.filedialog import *

root = Tk()
root.withdraw()

familyTreeFileName = askopenfilename()

if familyTreeFileName:
    familyTree = FamilyTree(familyTreeFileName)
else:
    print('Fanfic is usually terrible')

#FamilyTree = FamilyTree('RoyalFamily.csv')

personName = input('Enter a name\n')
targetName = input('Enter another name\n')

relation = familyTree.find_relationship(personName, targetName)
if relation:
    print('\n' + personName + ' is ' + targetName + '\'s ', end = '')
    print(relation)
else:
    print('Some people have index toes longer than their big toe')


