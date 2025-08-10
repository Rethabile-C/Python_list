#creating an empty list
my_list = []
print(my_list)

#append elements to the list

my_list.append(10)
my_list.append(20) 
my_list.append(30)
my_list.append(40)

print(my_list)

#nsert the value 15 at the second position
my_list.insert(1, 15)

print(my_list)

#extend my_list with another list
my_list.extend([50, 60, 70])

print(my_list)

#remove the last element on my_list
del my_list[-1]

print(my_list)

#sort my_list in ascending order

my_list.sort()

print(my_list)

#find and print the index of the value 30 in my_list
index_of_30 = my_list.index(30)
print(f"The index of 30 in my_list is: {index_of_30}")
