# logical operators are used to combine conditional statements
# and is the logical operator that returns True if both statements are true
# or is the logical operator that returns True if one of the statements is true
# not is the logical operator that returns True if the statement is false

print(80 > 10 and 80 < 10) #this will print False because 80 is greater than 10 but 80 is not less than 10
# the and operator returns True if both statements are true

print( 80 > 10 or 80 < 10) #this will print True because 80 is greater than 10 and 80 is not less than 10
# the or operator returns True if one of the statements is true

print (80 > 10 and not 80 < 10) #this will print True because 80 is greater than 10 and not 80 is not less than 10
# the not operator returns True if the statement is false