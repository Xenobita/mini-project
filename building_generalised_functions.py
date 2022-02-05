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
        add_item = input('What would you like to add? ').title
        file_contents.write(add_item.title() + '\n')

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

# Old lists below in case the worst happens
# ['green tea', 'lemon tea', 'redbush tea', 'breakfast tea', 'strawberry leaf tea', 'raspberry leaf tea', 'peppermint tea', 'flat white', 'americano (hot)', 'americano (cold)']

# ['Zagreus', 'Hades', 'Charon', 'Chaos', 'Megaera', 'Alecto', 'Tisiphone', 'Thanatos', 'Hypnos']

###########################################################################################
# Week 3 stuff 

def select_courier(self):
    file_contents_list = []
    with open('couriers.txt', 'r') as file_contents:
        for item in file_contents:
            file_contents_list.append(item)
    print_as_indexed_list(file_contents_list)
    courier_index = int(input('\nPlease enter the number of the courier you would like to assign this order to: '))
    courier_choice = str(file_contents_list[int(courier_index)]).strip('\n')
    return f'You have selected {courier_choice} for this order.'


