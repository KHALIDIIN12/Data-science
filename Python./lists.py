# lists are used to store multiple items in a single variable
# lists are created using square brackets []
# lists can contain any data type, including other lists

names = ['khalid', 'ahmed', 'muslims', 'qa']
print(names) # this will print the entire list
print(names[1]) # this will print the second item in the list
print(names[-1]) # this will print the last item in the list

names[0] = 'halid' # this will change the first item in the list to 'halid'
print(names) # this will print the entire list with the first item changed to 'halid'

## list methods
numbers = [1, 2, 3, 4, 5]
numbers.append(6) # this will add 6 to the end of the list
print(numbers) # this will print the entire list with 6 added to the end
# .append() is a method used when you want to add an item to the end of a list

numbers.insert(0, -1,) # this will add -1 to the beginning of the list
# the .insert() method is used when you want to add an item to a speficic indec in a list. 
numbers.remove(2) # this will remove the number 2 from the list

# len is a built-in function that returns the number of items in a list
print(len(numbers)) # this will print the length of the list, which is 6 because there are 6 items in the list