print("-" * 30)

print("    Welcome")

print("-" * 30)

a = input()
print(a)

name = input("Please type your name : ")
print(name)
age = input("Type your age: ")
#validations
ageInt = int(age)

print("Hi, " + name)
print("You will turn, " + str(ageInt + 1))

# String Methods
name_length = len(name) #return lenght
print ("There are " + str(name_length) +  "letters in your name")

print(name.upper()) # to upper
print(name.lower())
print(name.replace('D', 'Z')) # replace letters or words inside

print('D' in name )
