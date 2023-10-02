LOOP = 3
total = 0

for i in range(LOOP):
    user_input = float(input(str(i + 1) + ". Please enter your test score: "))
    total = total + user_input

total = total / LOOP    
print ("Average score: " + str(total))
