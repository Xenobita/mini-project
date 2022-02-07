
def main_menu():
    print('''Hello, welcome to the Xen\'s Music and Coffee app.
    [0] Exit app
    [1] Products Menu
    [2] Couriers Menu''')

def exit_app(): # Stops the app altogether
    print('The app will now close') 

def products_menu():
    print('''You are now in the PRODUCTS menu. What would you like to do?
    [0] Return to main menu
    [1] View all products (in alphabetical order)
    [2] Add a new product
    [3] STRETCH Update a product
    [4] STRETCH Delete a product''')

def return_main():
        print('Returning to main menu\n')

def couriers_menu():
    print('''You are now in the COURIERS menu. What would you like to do?
    [0] Return to main menu
    [1] View all couriers (in alphabetical order)
    [2] Add a new courier
    [3] STRETCH Update a courier
    [4] STRETCH Delete a courier''')

def orders_menu():
    print(''' You are now in the ORDERS menu. What would you like to do?
    [0] Return to main menu
    [1] View all orders
    [2] Create new order
    [3] Update order status
    [4] Update order details
    [5] Delete order''')

def invalid_choice():
    print('''You have made an invalid selection.
    Returning to previous menu...\n''')

## Generalised functions
def read_file_sorted(file_name):
    file_contents_list = []
    with open(file_name, 'r') as file_contents:
        for item in file_contents:
            file_contents_list.append(item)
    print(''.join(sorted(file_contents_list)))

def read_file(file_name):
    file_contents_list = []
    with open(file_name, 'r') as file_contents:
        for item in file_contents:
            file_contents_list.append(item)
    print(''.join(file_contents_list))

def add_item(file_name):
    file_contents_list = []
    with open(file_name, 'r+') as file_contents:
        for item in file_contents:
            file_contents_list.append(item)
        add_item = input('What would you like to add? ')
        file_contents.write(add_item.title() + '\n')
    print(f'{add_item.title()} successfully added.\nThis is your updated list: \n')

def print_as_indexed_list(file_contents_list):
    for idx, val in enumerate(file_contents_list):
        print(idx, str(val).strip('\n'))

def update_item(file_name):
    file_contents_list = []
    with open(file_name, 'r') as file_contents:
        for item in file_contents:
            file_contents_list.append(item)
        while True:
            print_as_indexed_list(file_contents_list)
            update_index = int(input('\nPlease enter the number of the item you would like to update: '))
            if update_index >= len(file_contents_list):
                print('You have entered an invalid number. Please try again')
                continue
            item_to_update = str(file_contents_list[int(update_index)]).strip('\n')
            update_item_with = input(f'You have selected {item_to_update}. Please enter the updated name: ')
            file_contents_list[int(update_index)] = update_item_with.title() 
            with open(file_name, 'w') as file_contents:
                for item in file_contents_list:
                    item = item.rstrip()
                    file_contents.write(item + '\n')
            print(f'{item_to_update} successfully updated to {update_item_with.title()}')
            break

def delete_item(file_name):
    file_contents_list = []
    with open(file_name, 'r') as file_contents:
        for item in file_contents:
            file_contents_list.append(item)
        while True:
            print_as_indexed_list(file_contents_list)
            delete_index = int(input('\nPlease enter the number of the item you would like to delete: '))
            if delete_index >= len(file_contents_list):
                print('You have entered an invalid number. Please try again.')
                continue
            item_to_delete = str(file_contents_list[int(delete_index)]).strip('\n')
            delete_item_confirmation = input(f'Are you sure you want to delete {item_to_delete}? (y/n): ')
            if delete_item_confirmation == "y":
                print(f'{item_to_delete} successfully deleted.')
                del(file_contents_list[int(delete_index)])
                break
            elif delete_item_confirmation == "n":
                print('Returning to list')
                continue
            else:
                invalid_choice()
                # print('Returning to list') I need to figure out what to write here and create a different invalid choice for indexes?
                continue
    with open(file_name, 'w') as file_contents:
        for item in file_contents_list:
            item = item.rstrip()
            file_contents.write(item + '\n')