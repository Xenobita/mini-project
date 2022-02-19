import csv

def main_menu():
    print('''Hello, welcome to the Xen\'s Music and Coffee app.
    [0] Exit app
    [1] Products Menu
    [2] Couriers Menu
    [3] Orders Menu''')

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
    print('''You are now in the ORDERS menu. What would you like to do?
    [0] Return to main menu
    [1] View all orders
    [2] Create new order
    [3] Update order status
    [4] STRETCH Update order details
    [5] STRETCH Delete order''')

def invalid_choice():
    print('''You have made an invalid selection.
    Returning to previous menu...\n''')

## Generalised functions
# TXT files
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

# Functional functions

# CSV functions (to replace txt ones)
def read_csv(filename):
    with open(filename, 'r') as file:
        file_contents = csv.DictReader(file)
        for row in file_contents:
            print(row)

def read_csv_with_idx_for_selection(filename, key):
    file_contents_list = []
    with open(filename, 'r', newline="") as file:
        file_contents = csv.DictReader(file)
        for row in file_contents:
            file_contents_list.append(row.get(key))
        print_as_indexed_list(file_contents_list)
    return file_contents_list

def selection_from_idx(filename, item_index):
    file_contents_list = []
    with open(filename, 'r') as file_contents:
        reader = csv.DictReader(file_contents)
        for row in reader:
            file_contents_list.append(row.get("Name"))
    selection_from_txt = str(file_contents_list[int(item_index)]).strip('\n')
    print(f'You have added {selection_from_txt} to this order.')

# Only to be used within while True loop to avoid repetition
def do_more_in_current_menu(current_menu, previous_menu):
    do_more = input(f'\nWould you like to return to the {current_menu} menu? (y/n): ')
    if do_more == 'y':
        print(f'Returning to {current_menu} menu...\n')
        return True
    elif do_more == 'n':
        print(f'Returning to {previous_menu} menu...\n')
        return False
    else:
        invalid_choice()
        return True

# Orders functions
def create_product_list_for_order():
    products_in_order = []
    while True:
        read_csv_with_idx_for_selection('products.csv', "Name")
        add_product_to_order = int(input('Please enter the number of a product in the order: '))
        products_in_order.append(add_product_to_order)
        selection_from_idx('products.csv', add_product_to_order)
        add_another_product = input('Would you like to add another product? (y/n): ')
        if add_another_product == "y":
            continue
        elif add_another_product == "n":
            break
        else:
            invalid_choice()
            continue
    return products_in_order


