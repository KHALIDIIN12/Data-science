int() #used when you want to convert a value to an integer 
float() #used when you want to convert a value to a float
str() #used when you want to convert a value to a string
bool() #used when you want to convert a value to a boolean

#CONVERTING  A STRING TO AN INTEGER
Birth_year = input("which year were you born? ")
current_year = 2026
Age =  current_year - int(Birth_year)#this converts the string "what is your age?" to an integer
print("your age is" , Age)

