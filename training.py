# this frist line in python file and i will comment it 
# this frist line in python file and i will comment it 

######### data types & variables #########

# there is no variables start with numbers
# and it's not allowed to use any special character
# there's no spaces in variables

# int
new = 1
# float
y =2.5
# string
z = "hello my friends"
# boolean
bn =True

######### print syntax #########
print('hello my friends')
print(3.4,"printing variable 1:",new) #space between them
print("hi","to my fav",end=' | ')
print('here we go again')
print("-------------------------------------")

######### scanning \ READING function #########

inputted= input('put here message to get it again :')
print("this the message for you:",'\n',">>",inputted)

######### we Could do an Arithmatic Operations #########
value1= 6 
value2= 7
result =((value1+value2)*value2)/value2
# to create power (x power y)
power= value1 ** value2
# to create divition without decimal numbers
intonly = value1 // value2
# to back with remindre use (%)

# to use input to get integer number not a string we use type casting
number =input('put a number:')
print(int(number) -6)

######### string methods #########

# all words are in upper case
welk='hello'.upper()
# all words are in lower case
welk='hello'.lower()
# all words are capitalized 
welk='hello'.capitalize()
# count function to know how many times the string exict
print('heLLo'.lower().count('ll'))
# know the type of the variable
print(type(welk))
# we could do multiplication on strings 
number='2'
HMT=6
print(number * HMT)

######### cinditional operators #########

# equality ?
pirnt(value1 == value2)
# not equal
print(value1 != value2)
# is greater than??
print(value1 > value2)

######### if /else /elif #########
value1= input("get the v1:")
# elif function come in the middle between if and else
if(value1 == value2):
    print('hello mis amego')
elif value1==6:
    print("sixxxxxxxxxxxx")
else:
    print("bye mis amego")

######### collections (list & tupels) #########

