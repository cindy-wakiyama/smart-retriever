# menu
# add item
# remove item
# retrieve item
# return item


#set inventory array
inventory = []

#menu options
def add_item():
    print("What item do you want to add to the inventory?")
    item = input()
    inventory.append(item)
  
def remove_item():
    print("What item do you want to remove from the inventory?")
    item = input()
    inventory.remove(item)

def retrieve_item():
    print("retrieve item")

def return_item():
    print("return item")

def menu():
    print("Choose an option: \n 1. Add item \n 2. Remove item \n 3. Retrive item \n 4. Return item \n")
    choice = input()
    if choice == "1":
        add_item()
    elif choice == "2":
        remove_item()
    elif choice == "3":
        retrieve_item()
    elif choice == "4":
        return_item()
    else:
        menu()

menu()



