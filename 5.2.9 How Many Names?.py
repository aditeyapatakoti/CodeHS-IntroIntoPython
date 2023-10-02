names = int(input("How many names do you have? "))
name = ""
full_name = ""

for i in range(names):
    name = input(str(i + 1) + "Please enter your name: ")
    full_name = full_name + " " + name
    
print("Your full name is:" + full_name)
