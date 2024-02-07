
# ------------------------------------------------------
# 7 - Ask the user for his name then confirm that he has entered his name
# (not an empty string/integers). then proceed to ask him for his email and
# print all this data- (Bonus) check if it is a valid email or not
# ------------------------------------------------------

name=input("\n enter your name please: ")
if name == "":
    print("\n Error : you didn't input the name in right way")
    exit()
email = input("\n enter your Email: ")

print("-----------------------------------------")
if "gmail.com" in email:
    print(f" your name is {name} \n your email is: {email}")
else:
    print("\n sorry you entered incorrect email")