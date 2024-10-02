
print("****** Welcome to TODO list! ******\n")
list = []
print("What would you like to perform?\n")
print("1. Add an item")
print("2. View all items")
print("3. Remove an item")
print("4. Exit")
choice = int(input("Enter your choice(1/2/3/4): \n"))

while True:
    if choice == 1:
        item = input("Enter your task: \n")
        list.append(item)
    elif choice == 2:
        print(list)
    elif choice == 3:
        item = input("Enter your task: \n")
        if item in list:
            list.remove(item)
        else:
            print("Item not found.")
    elif choice == 4:
        break
    else:
        print("Invalid choice")
    print("What would you like to perform?")
    print("1. Add an item")
    print("2. View all items")
    print("3. Remove an item")
    print("4. Exit")
    choice = int(input("Enter your choice(1/2/3/4): "))