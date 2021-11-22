checklist=[]

def create(item):
    checklist.append(item)

    return "added {} to checlist".format(item)
    
def read(index):
    print(checklist[index])

    return checklist[index]
    
def update(index, item):
    
    old = checklist[index]
    
    checklist[index]= item
    
    return "changed {} to ()".format(old, item)
    
def destroy(index):
    
    removed = checklist[index]
    
    checklist.pop(index)    
    
    return "removed {} from checklist".format(removed)

def all_items(list):
    
    items=[]

    for el in checklist:
        print(el)
        items.append(el)
    
    return items
def checked(index):
    
    unchecked = checklist[index]
    
    checklist[index]="% " + unchecked
    
    return checklist[index]

def user_input(prompt):

    entry=input(prompt)

    return entry

def user_choice():
    
    editing=True
    while editing:

    choice=user_input("What function do you want to use? Enter C for create, R for read, U for update, D for destory. ")

    if choice == "C" or "c":
        item=user_input("What item do you want to creat?Type out the name of your desired item.")

        create(item)

        continue
    elif choice =="R" or "r":
        
        index=user_input("what item do you wish to read? Give a number for the position of the item.")
        
        read(index)
        
        continue
        
    elif choice =="U" or "u":
        
        update_index=user_input("What item do you wish to update? Give a number for the positon of the item.")
        
        new_item=user_input("Type out the name of your new item. ")
        
        update(update_index, new_item)
        
        continue
        
    elif choice =="D" or "d":
        
        delete_index=user_input("What item do you wish to destroy? Give a number for the positon of the item.")
        
        destroy(delete_index)
        continue
        

    else:

        end=user_input("Do you want to quit? Enter Y for yes or N for no.")

        if end== "Y" or "y":
            print(checklist)
            editing=False
        else:

            continue

            

def test():
    create("purple sox")
    create("red cloak")

    print(read(0))
    print(read(1))

    update(0, "purple socks")
    destroy(1)

    print(read(0))
    print(all_items())
    print(checked[0])
    print(user_input("Working? "))
    user_choice()

while editing:
    user_choice()
