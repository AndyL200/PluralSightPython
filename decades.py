amount = 10
tax = 0.06
total = amount + amount*tax
print(total)

my_name = input("What is your name?\n")
greeting = "Hello " + my_name
print(greeting)


age = int(input("How old are you?\n"))

decades = int(age/10)
remainder = age%10

print("You are " + str(decades) + " decades old and " + str(remainder) + " years")