# Initialize an empty list to hold the to-do items
todo_list = []

# Prompt the user to add or remove items from the list
while True:
    action = input("Do you want to add or remove items from the list? (Type 'add' or 'remove', or 'exit' to quit) ")

    if action == "add":
        item = input("Enter the item you want to add to the list: ")
        todo_list.append(item)
        print(f"{item} added to to-do list.")

    elif action == "remove":
        item = input("Enter the item you want to remove from the list: ")
        if item in todo_list:
            todo_list.remove(item)
            print(f"{item} removed from to-do list.")
        else:
            print("Item not found in to-do list.")

    elif action == "exit":
        print("Goodbye!")
        break

    else:
        print("Invalid input. Please try again.")

    print("Current to-do list:")
    for item in todo_list:
        print("- " + item)
