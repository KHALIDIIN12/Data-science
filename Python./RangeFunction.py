# range function is used to generate a sequence of numbers. 
# It can take one, two, or three arguments: start, stop, and step. 
# The start argument is the first number in the sequence, 
# the stop argument is the last number in the sequence (exclusive), 
# and the step argument is the difference between each number in the sequence.

numbers = range(6) # this will generate a sequence of numbers from 0 to 5
for number in numbers:
   print(number) # this will print each number in the sequence one by one

List = range(6, 11) # this will generate a sequence of numbers starting rom 6 to 10
for integers in List:
    print(integers) # this will print each number in the sequence one by one

numbers = range(2, 11, 3) # this will generate a sequence of numbers starting from 2 to 10 with a step of 3
for range in numbers:
    print(range) # this will print each number in the sequence one by one