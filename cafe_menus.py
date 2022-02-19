import csv
from fieldnames import *
from entry_prompts import *
## To set currency, see entry_prompts.py

def main_menu():
    return('''Hello, welcome to the Xen\'s Music and Coffee app.
    [0] Exit app
    [1] Products Menu
    [2] Couriers Menu
    [3] Orders Menu''')

def exit_app(): # Stops the app altogether
    return('The app will now close') 

def products_menu():
    return('''You are now in the PRODUCTS menu. What would you like to do?
    [0] Return to main menu
    [1] View all products (in alphabetical order)
    [2] Add a new product
    [3] STRETCH Update a product
    [4] STRETCH Delete a product''')

def return_main():
        return ('Returning to MAIN menu\n')

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

########################
# Reading Functions
# TXT functions
def read_txt_file_with_index(file_name):
    file_contents_list = []
    with open(file_name, 'r') as file_contents:
        for item in file_contents:
            file_contents_list.append(item)
    return file_contents_list

# Indexing function
def print_as_indexed_list(file_contents_list):
    for idx, val in enumerate(file_contents_list):
        print(idx, str(val).strip('\n'))

# csv functions (to replace txt ones)
def read_csv(filename):
    with open(filename, 'r') as file:
        file_contents = csv.DictReader(file)
        for row in file_contents:
            print(row)

def read_full_csv_with_idx(filename):
    file_contents_list = []
    with open(filename, 'r', newline="") as file:
        file_contents = csv.DictReader(file)
        for row in file_contents:
            file_contents_list.append(row)
        print_as_indexed_list(file_contents_list)
    return file_contents_list

def write_to_csv(filename, field_names, updated_list):
    with open (filename, 'w', newline='') as file:
        writer = csv.DictWriter(file, fieldnames = field_names)
        writer.writeheader()
        writer.writerows(updated_list)

# Function that returns an specifiec key's value with an index from a csv
def read_abridged_csv_with_idx_for_selection(filename, key):
    file_contents_list = []
    with open(filename, 'r', newline="") as file:
        file_contents = csv.DictReader(file)
        for row in file_contents:
            file_contents_list.append(row.get(key))
        print_as_indexed_list(file_contents_list)
    return file_contents_list

# Appends entry to end of csv file
def add_to_csv(filename, fieldnames_from_csv, item_to_add, category_name):
    with open(filename, 'a', newline="") as file_contents:
        writer = csv.DictWriter(file_contents, fieldnames = fieldnames_from_csv)
        writer.writerow(item_to_add)
    return f'Your {category_name} has been added'

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

# Order-unique functions
def create_product_list_for_order():
    products_in_order = []
    while True:
        read_abridged_csv_with_idx_for_selection('products.csv', "Name")
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

def select_courier_for_order():
    read_abridged_csv_with_idx_for_selection('couriers.csv', "Name")
    courier_index = int(input('\nPlease enter the number of the courier you would like to assign this order to: '))
    print(selection_from_idx('couriers.csv', courier_index, 'Name'))
    return courier_index

def selection_from_idx(filename, item_index, key_from_csv):
    file_contents_list = []
    with open(filename, 'r') as file_contents:
        reader = csv.DictReader(file_contents)
        for row in reader:
            file_contents_list.append(row.get(key_from_csv))
    selection_from_csv = str(file_contents_list[int(item_index)]).strip('\n')
    return f'You have added {selection_from_csv} to this order.'

# ADDING FUNCTIONS
def add_new_product(set_currency):
    add_product_prompts

    new_product = {}

    for csv_key in add_product_prompts:
        user_input_value = input(add_product_prompts.get(csv_key))
        if csv_key == "Price":
            new_product[csv_key] = float(user_input_value)
        else:
            new_product[csv_key] = user_input_value
        
    return(add_to_csv('products.csv', product_fieldnames, new_product, 'product'))

def add_new_courier():
    add_courier_prompts

    new_courier = {}

    for csv_key in add_courier_prompts:
        user_input_value = input(add_courier_prompts.get(csv_key))
        new_courier[csv_key] = user_input_value
        
    return(add_to_csv('couriers.csv', courier_fieldnames, new_courier, 'courier'))

def add_new_order():
    add_order_prompts

    new_order = {}

    for csv_key in add_order_prompts:
        user_input_value = input(add_order_prompts.get(csv_key))
        if csv_key == 'Products':
            new_order[csv_key] = create_product_list_for_order()
        elif csv_key == "Courier":
            new_order[csv_key] = select_courier_for_order()
        elif csv_key == "Order Status":
            new_order[csv_key] = "PENDING"
        else:
            new_order[csv_key] = user_input_value
        
    return(add_to_csv('orders.csv', order_fieldnames, new_order, 'order'))

## Update functions
def show_selection_for_action(item_index, file_contents_list, category_name, action):
    entry_for_update = file_contents_list[int(item_index)]
    return f'''This is the {category_name} you will be {action}. 
    {entry_for_update}'''

def update_function(filename, category_name, category_prompts, fieldnames):
    while True:
        file_contents_list = read_full_csv_with_idx(filename)
        update_index = int(input(f'\nPlease enter the number of the {category_name} you would like to update: '))
        if update_index >= len(file_contents_list):
            print('You have entered an invalid number. Please try again')
            continue
        print(show_selection_for_action(update_index, file_contents_list, category_name, 'updating'))
        
        category_prompts

        for csv_key in category_prompts:
            user_input_value = input(category_prompts.get(csv_key))
            if user_input_value == "":
                pass
            elif csv_key == "Products":
                category_prompts[csv_key] = create_product_list_for_order()
            elif csv_key == "Courier":
                category_prompts[csv_key] = select_courier_for_order()
            else:
                file_contents_list[update_index][csv_key] = user_input_value
        
        write_to_csv(filename, fieldnames, file_contents_list)
        break
    return f'Your {category_name} has been updated'

### Testing update function
# print(update_function_template('products.csv', 'product', product_prompts, product_fieldnames))

### Delete function
def delete_function(filename, category_name, fieldnames):
    while True:
        file_contents_list = read_full_csv_with_idx(filename)
        delete_index = int(input(f'\nPlease enter the number of the {category_name} you would like to delete: '))
        if delete_index >= len(file_contents_list):
            print('You have entered an invalid number. Please try again')
            continue
        print(show_selection_for_action(delete_index, file_contents_list, category_name, 'deleting'))
        if confirmation('delete', category_name) == False:
            continue
        else:
            del file_contents_list[delete_index]
            
            write_to_csv(filename, fieldnames, file_contents_list)
            return f'Your {category_name} has been deleted'

def confirmation(action, category_name):
    confirm_action = input(f'Are you sure you want to {action} this {category_name}? (y/n): ')
    if confirm_action == 'y':
        return True
    elif confirm_action == 'n':
        return False
    else:
        invalid_choice()
        return True
