# Playing with lists, names
friends = ['swaroop','ansh','shaurya','vedant','piyush','sanket']
print(friends[0].title())
print(friends[1].upper())
print(friends[3].lower())
# Greetings 
print(f"Happy Birthday !! {friends[0].title()} brother.")
print(f"You are my friend {friends[1].title()}.")
print(f"Hi {friends[2].title()}, How are you?")
print(f"{friends[3].title()}, did she remembered me today ?")
print(f"Where do you live {friends[4].title()}?")

# Modifing lists
family = ['prashant','pranita','pratik','madhukar','jaishri']
family[4] = 'jayshree'
print(family)

# Adding elements to lists
family.append('sakharam')
print(family)

# Inserting elements to lists 
family.insert(5,'sakhrabai')
print(family)

# Removing elements from lists
del family[5]
print(family)

# Popping elements from lists
family.append('sakhrabai')
popped_family = family.pop()
print(family)
print(popped_family)
pop_fam_1 = family.pop(5)
print(family)
print(pop_fam_1)
print(f"\nMr. {pop_fam_1.title()} was my Grandfather.")

# Removing an item by value 
family.remove('prashant')
print(family)
family.insert(0, 'prashant')
family.append('madhukar')
print(family)
family.remove('madhukar')
print(family)  # remove() removes only the initial value, recurring same value is'nt removed

# Operations using a variable for a value
sister = 'pranita'
family.remove(sister)
print(family)
family.append(sister)
print(family)
del family[4]
print(family)
family.insert(1,sister)
print(family)

# ORGANISING LISTS 
# Sorting a list permanently with sort() method 
#family.sort()
#print(family)
#family.sort(reverse = True)
#print(family)

# Sorting a list temporarily with sorted() function
print(sorted(family))
print(sorted(family, reverse = True))
print(family)

#  Printing the list in reverse order (permanent)
family.reverse()   # reverse order 
print(family)
family.reverse()   # original order
print(family) 

# Printing the length of the lists (using len() function)
print(len(family))

# Do it yourself 
visit_places = ['malibu','birmingham','las vegas','dubai','tiruvanathpuram','paris','munich']
print(visit_places)
print(sorted(visit_places))
print(visit_places)
print(sorted(visit_places, reverse = True))
print(visit_places)

visit_places.reverse()
print(visit_places)
visit_places.reverse()
print(visit_places)

visit_places.sort()
print(visit_places)
visit_places.sort(reverse = True)
print(visit_places)

print(len(visit_places))

