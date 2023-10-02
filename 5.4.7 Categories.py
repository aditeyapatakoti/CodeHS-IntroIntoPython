for i in range(3):
    cat = input("Enter a catagory: ")
    items = []
    for j in range(3):
        items.append(input("Enter something in that catagory: "))
    print(cat + ": " + " ".join(items))
