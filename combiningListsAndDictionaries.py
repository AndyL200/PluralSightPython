menus = [ ['Eggs','Bagels','Coffee'], 
          ['BLT','PBJ','TrkySand'], 
          ['Soup','Slime','Chum'] ]
#List of lists

print('Breakfast menu', menus[0])
print('Breakfast item 1', menus[0][1]) #like a 2-Dimensional Array

menus = {
    'Breakfast' : ['Eggs','Bagels','Coffee'],
    'Lunch' : ['BLT','PBJ','TrkySand'],
    'Dinner' : ['Soup','Slime','Chum'] 
}
# A Dictionary of Lists

for name, menu in menus.items(): 
    print(name, ':', menu) #can see the key with its list value

#Representing people
person = {'name' : 'Sarah Smith',
          'city': 'Orlando',
          'age' : 100
          }
