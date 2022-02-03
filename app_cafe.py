from cafe_menus import *
import os
import time

while True:
    main_menu()

    menu_selection = input('\nPlease enter number of your choice here: ')

    if menu_selection == '0':
        exit_app()
        break

    elif menu_selection == '1':
        while True:
            products_menu()
            menu_selection = input('\nPlease enter the number of your choice here: ')
            if menu_selection == '0':
                return_main()
                break # This gets the app to return to the start
            elif menu_selection == '1':
                read_file_sorted('products.txt')
            elif menu_selection == '2':
                add_item('products.txt')
                read_file('products.txt')
            elif menu_selection == '3':
                update_item('products.txt')
            elif menu_selection == '4':
                delete_item('products.txt')
            else:
                invalid_choice()
                continue

            do_more = input('Would you like to return to the PRODUCTS menu? (y/n): ')
            if do_more == 'y':
                print('Returning to PRODUCTS menu...\n')
                continue
            elif do_more == 'n':
                print('Returning to MAIN menu...\n')
                break
            else:
                invalid_choice()
                continue

    elif menu_selection == '2':
        while True:
            couriers_menu()
            menu_selection = input('\nPlease enter the number of your choice here: ')
            if menu_selection == '0':
                return_main()
                break
            elif menu_selection == '1':
                read_file_sorted('couriers.txt')
            elif menu_selection == '2':
                add_item('couriers.txt')
                read_file('couriers.txt')
            elif menu_selection == '3':
                update_item('couriers.txt')
            elif menu_selection == '4':
                delete_item('couriers.txt')
            else:
                invalid_choice()
                continue

            do_more = input('Would you like to return to the COURIERS menu? (y/n): ')
            if do_more == 'y':
                print('Returning to COURIERS menu...\n')
                continue
            elif do_more == 'n':
                print('Returning to MAIN menu...\n')
                break
            else:
                invalid_choice()
                continue  
    else:
        invalid_choice()