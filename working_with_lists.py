#Operations on Lists
#1.Get the length of a list
#2.Select subsets of a list (called slicing)
#3.Count the number of times that an element appears in a list
#4.Sort a list of items

#1
list1 = range(2, 20, 3)
list1_len = len(list1)
print(list1_len)
#2
employees = ['Michael', 'Dwight', 'Jim', 'Pam', 'Ryan', 'Andy', 'Robert']
index4 = employees[4]
print(len(employees))
print(employees[3])

shopping_list = ['eggs', 'butter', 'milk', 'cucumbers', 'juice', 'cereal']
print(len(shopping_list))
last_element = shopping_list[-1]
element5 = shopping_list[5]
print(element5,last_element)

suitcase = ['shirt', 'shirt', 'pants', 'pants', 'pajamas', 'books']

beginning = suitcase[0:4]
print(beginning)
middle = suitcase[2:4]

suitcase = ['shirt', 'shirt', 'pants', 'pants', 'pajamas', 'books']
start = suitcase[:3]
end = suitcase[-2:]

#3
votes = ['Jake', 'Jake', 'Laurie', 'Laurie', 'Laurie', 'Jake', 'Jake', 'Jake', 'Laurie', 'Cassie', 'Cassie', 'Jake', 'Jake', 'Cassie', 'Laurie', 'Cassie', 'Jake', 'Jake', 'Cassie', 'Laurie']
jake_votes = votes.count('Jake')
print(jake_votes)

#sorting lists
### Exercise 1 & 2 ###
addresses = ['221 B Baker St.', '42 Wallaby Way', '12 Grimmauld Place', '742 Evergreen Terrace', '1600 Pennsylvania Ave', '10 Downing St.']

# Sort addresses here:

### Exercise 3 ###
names = ['Ron', 'Hermione', 'Harry', 'Albus', 'Sirius']
names.sort()

### Exercise 4 ###
cities = ['London', 'Paris', 'Rome', 'Los Angeles', 'New York']

sorted_cities = cities.sort()
addresses.sort()
print(addresses)
print(sorted_cities)

inventory = ['twin bed', 'twin bed', 'headboard', 'queen bed', 'king bed', 'dresser', 'dresser', 'table', 'table', 'nightstand', 'nightstand', 'king bed', 'king bed', 'twin bed', 'twin bed', 'sheets', 'sheets', 'pillow', 'pillow']

inventory_len = len(inventory)
first = inventory[0]
last = inventory[-1]
inventory_2_6 = inventory[2:6]

first_3 = inventory[:3]
twin_beds = inventory.count("twin bed")
inventory.sort()