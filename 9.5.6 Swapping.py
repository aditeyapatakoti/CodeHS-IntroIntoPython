def swap_lists(first, second):
    f = [second, first]
    print("After swap")
    print("list_one: " + str(f[0]))
    print("list_two: " + str(f[1]))

list_one = [1, 2, 3, 4, 5, 6]
list_two = [4, 5, 6]

print("Before swap")
print("list_one: " + str(list_one))
print("list_two: " + str(list_two))

swap_lists(list_one, list_two)
