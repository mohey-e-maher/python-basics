# ------------------------------------------------------
# 1 - Write a program that counts up the number of vowels [a, e, i, o, u]
# contained in the string
# ------------------------------------------------------

strings= input("input the the sentence:")
counter = 0
for i in strings:
    if i == 'a':
        counter+=1
    elif i == 'e':
        counter+=1
    elif i == 'i':
        counter+=1
    elif i == 'o':
        counter+=1
    elif i == 'u':
        counter+=1
print(f"the number of the vowels in the sentence is: {counter}")