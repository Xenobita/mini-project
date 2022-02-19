# Old lists below in case the worst happens
# ['green tea', 'lemon tea', 'redbush tea', 'breakfast tea', 'strawberry leaf tea', 'raspberry leaf tea', 'peppermint tea', 'flat white', 'americano (hot)', 'americano (cold)']

# ['Zagreus', 'Hades', 'Charon', 'Chaos', 'Megaera', 'Alecto', 'Tisiphone', 'Thanatos', 'Hypnos']

# Name,Address,Phone Number,Courier,Order Status
# Xan,"43 Pride Apartments, Hubbu Lane, BF9 4SL",039459292405,3,PENDING
# Asia,"72 Brummie Lane, Birmingham, BR9 3DS",07922503449,4,PENDING
# Sam,"53 Havistock Close, Leicestershire, LE2 4FF",02339601332,3,PENDING
# Ari,"1369-393 Floor 4, Pandari Apt, Mapo-gu, South Korea",06895027593,4,PENDING
# Chem,"100b End of the Lane, Stockport, ST4 105",07956103486,4,PENDING
#############################################################
# Function take txt file in ['list',] form and output as list with line breaks
# Run this when you accidentally delete your list again
###########################################################
# take something from one file and saves it to a new file
# def save_to_file(original_file, new_file):
#     with open(new_file, 'w') as new_file:
#         new_file.write(''.join(original_file))
#         new_file.write('\n')

# original_file = open('products_list.txt', 'r')
# contents = original_file.read()
# print(contents)

# # remove_padding_from_list()
# save_to_file(contents.replace("', '", "\n").replace("['", "").replace("']", "").title(), 'products.txt')
############################################################
def invalid_choice():
    print('''You have made an invalid selection.
    Returning to previous menu...\n''')

#########################################################
# Working from text files
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

# add_item('products.txt')
# read_file('products.txt')
# update_item('products.txt')
# delete_item('products.txt')


###########################################################################################
# Week 3 stuff 

# Selecting from files
def read_file_with_idx(filename):
    file_contents_list = []
    with open(filename, 'r') as file_contents:
        for item in file_contents:
            file_contents_list.append(item)
    print_as_indexed_list(file_contents_list)
        

def courier_selection(filename, item_index):
    file_contents_list = []
    with open(filename, 'r') as file_contents:
        reader = csv.DictReader(file_contents)
        for row in reader:
            file_contents_list.append(row.get("Name"))
    selection_from_txt = str(file_contents_list[int(item_index)]).strip('\n')
    print(f'You have added {selection_from_txt} to this order.')

def display_selection_from_csv(filename, item_index):
    file_contents_list = []
    with open(filename, 'r') as file_contents:
        reader = csv.DictReader(file_contents)
        for row in reader:
            customer_name = row.get('Name')
            order_status = row.get('Order Status')
            name_and_status = [customer_name, order_status]
            file_contents_list.append(name_and_status)
            # file_contents_list.append(row)
    order_name = str(file_contents_list[int(item_index)][0]).strip('\n').strip("['").strip("']")
    order_status = str(file_contents_list[int(item_index)][1]).strip('\n').strip("['").strip("']")
    print(f'{order_name}\'s order is currently {order_status}.')

# read_file_with_idx()
# item_index = int(input('\nPlease enter the number of the courier you would like to assign this order to: '))
# courier_selection('couriers.txt', item_index)

########################################################

import csv
from pprint import pp

def add_order():
    with open('orders.csv', 'a', newline="") as file_contents:
        writer = csv.writer(file_contents)
        user_input = []
        customer_name = input('Enter customer name: ')
        user_input.append(customer_name)
        customer_address = input('Enter customer\'s address: ')
        user_input.append(customer_address)
        customer_phone_number = input('Enter customer\'s phone number: ')
        user_input.append(customer_phone_number)
        read_file_with_idx('couriers.txt')
        item_index = int(input('\nPlease enter the number of the courier you would like to assign this order to: '))
        courier_selection('couriers.txt', item_index)
        user_input.append(item_index)
        order_status = "PENDING"
        user_input.append(order_status)
        print('Order is currently PENDING')
        writer.writerow(user_input)

# TODO Complete update status function; find a way to pop particular entry out of a dictionary, change a value in it, then put the entry back into a dictionary
def update_status():
    with open('orders.csv', 'r+', newline="") as file_contents:
        file_contents_list = []
        reader = csv.DictReader(file_contents)
        for row in reader:
            customer_name = row.get('Name')
            customer_address = row.get('Address')
            customer_phone_number = row.get('Phone Number')
            courier = row.get('Courier')
            order_status = row.get('Order Status')
            ordered_products = row.get('Products')
            order_details = [customer_name, customer_address, customer_phone_number, courier, order_status]
            file_contents_list.append(order_details)
            # file_contents_list.append(row)
        print_as_indexed_list(file_contents_list)
        update_order_selection = input('\nPlease enter the number of the order you would like to update: ')
        display_selection_from_csv('orders.csv', update_order_selection)
        read_file_with_idx('status.txt')
        updated_status_index = (input('\nPlease enter the number for the updated status: '))
        
# view_csv('orders.csv')
# add_order()
# update_status()

# read_file_with_idx('status.txt')
# display_selection_from_csv('orders.csv', 3)

#######################################################
# Reading from csv

def read_csv(filename):
    with open(filename, 'r') as file:
        file_contents = csv.DictReader(file)
        for row in file_contents:
            # print(row)
            print(file_contents)
        # return file_contents

def read_csv_with_idx(filename):
    file_contents_list = []
    with open(filename, 'r', newline="") as file:
        file_contents = csv.DictReader(file)
        for row in file_contents:
            file_contents_list.append(row)
        print_as_indexed_list(file_contents_list)

# read_csv('couriers.csv')
# read_csv_with_idx('couriers.csv')

########################################################
# WEEK FOUR DO-OVER
from fieldnames import *

def add_to_CSV(filename, fieldnames_from_csv, item_to_add, category_name):
    with open(filename, 'a', newline="") as file_contents:
        writer = csv.DictWriter(file_contents, fieldnames = fieldnames_from_csv)
        writer.writerow(item_to_add)
    return f'Your {category_name} has been added'

# Function that will be good to use for selecting within other functions
def read_csv_with_idx_for_selection(filename, key):
    file_contents_list = []
    with open(filename, 'r', newline="") as file:
        file_contents = csv.DictReader(file)
        for row in file_contents:
            file_contents_list.append(row.get(key))
        print_as_indexed_list(file_contents_list)
    return file_contents_list

# Used to display what the user chose from an index of the file passed in
def selection_from_idx(filename, item_index, key_from_csv):
    file_contents_list = []
    with open(filename, 'r') as file_contents:
        reader = csv.DictReader(file_contents)
        for row in reader:
            file_contents_list.append(row.get(key_from_csv))
    selection_from_txt = str(file_contents_list[int(item_index)]).strip('\n')
    return f'You have added {selection_from_txt} to this order.'


## ORDER FUNCTIONS
def create_product_list_for_order():
    products_in_order = []
    while True:
        read_csv_with_idx_for_selection('products.csv', "Name")
        add_product_to_order = int(input('Please enter the number of a product in the order: '))
        products_in_order.append(add_product_to_order)
        selection_from_idx('products.csv', add_product_to_order, 'Name')
        add_another_product = input('\nWould you like to add another product? (y/n): ')
        if add_another_product == "y":
            continue
        elif add_another_product == "n":
            break
        else:
            invalid_choice()
            continue
    return products_in_order

def select_courier_for_order():
    read_csv_with_idx_for_selection('couriers.csv', "Name")
    courier_index = int(input('\nPlease enter the number of the courier you would like to assign this order to: '))
    print(selection_from_idx('couriers.csv', courier_index, 'Name'))
    return courier_index



# ADDING FUNCTIONS
def add_new_product(currency_symbol):
    input_keys_and_prompts = {
        'Name': 'Enter product name: ',
        'Price': f'Enter the price of the product: {currency_symbol}'
    }

    new_product = {}

    for input_key in input_keys_and_prompts:
        new_input = input(input_keys_and_prompts.get(input_key))
        new_product[input_key] = new_input
        
    print(add_to_CSV('products.csv', product_fieldnames, new_product, 'product'))
    

def add_new_courier():
    input_keys_and_prompts = {
        'Name': 'Enter courier name: ',
        'Phone Number': 'Enter the courier\'s phone number:'
    }

    new_courier = {}

    for input_key in input_keys_and_prompts:
        new_input = input(input_keys_and_prompts.get(input_key))
        new_courier[input_key] = new_input
        
    print(add_to_CSV('couriers.csv', courier_fieldnames, new_courier, 'courier'))

def add_new_order():
    input_keys_and_prompts = {
        'Customer Name' : 'Enter customer name: ',
        'Address': 'Enter the customer\'s full address: ',
        'Phone Number' : 'Enter the customer\'s phone number: ',
        'Products' : 'Press return key to select products for this order.\n',
        'Courier' : '''Products added to order.
Press return key to select a courier for this order\n''',
        'Order Status' : "Your order is currently PENDING"
    }

    new_order = {}

    for input_key in input_keys_and_prompts:
        new_input = input(input_keys_and_prompts.get(input_key))
        if input_key == 'Products':
            new_order[input_key] = create_product_list_for_order()
        elif input_key == "Courier":
            new_order[input_key] = select_courier_for_order()
        elif input_key == "Order Status":
            new_order[input_key] = "PENDING"
        else:
            new_order[input_key] = new_input
        
    print(add_to_CSV('orders.csv', order_fieldnames, new_order, 'order'))

