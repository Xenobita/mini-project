from cafe_menus import *
import os
import time

while True:
    print(main_menu())

    menu_selection = input('\nPlease enter number of your choice here: ')

    if menu_selection == '0':
        print(exit_app())
        break

    elif menu_selection == '1':
        while True:
            print(products_menu())
            menu_selection = input('\nPlease enter the number of your choice here: ')
            if menu_selection == '0':
                print(return_main())
                break
            elif menu_selection == '1':
                read_csv('products.csv')
            elif menu_selection == '2':
                print(add_new_product(set_currency))
            elif menu_selection == '3':
                print(update_function('products.csv', 'product', update_product_prompts, product_fieldnames))
            elif menu_selection == '4':
                delete_function('products.csv', 'product', product_fieldnames)
            else:
                invalid_choice()
                continue

            if do_more_in_current_menu('PRODUCTS', "MAIN") == False:
                break

    elif menu_selection == '2':
        while True:
            couriers_menu()
            menu_selection = input('\nPlease enter the number of your choice here: ')
            if menu_selection == '0':
                print(return_main())
                break
            elif menu_selection == '1':
                read_csv('couriers.csv')
            elif menu_selection == '2':
                print(add_new_courier())
            elif menu_selection == '3':
                print(update_function('couriers.csv', 'courier', update_courier_prompts, courier_fieldnames))
            elif menu_selection == '4':
                delete_function('couriers.csv', 'courier', courier_fieldnames)
            else:
                invalid_choice()
                continue

            if do_more_in_current_menu('COURIERS', "MAIN") == False:
                break

    elif menu_selection == '3':
        while True:
            orders_menu()
            menu_selection = input('\nPlease enter the number of your choice here: ')
            if menu_selection == '0':
                print(return_main())
                break
            elif menu_selection == '1':
                read_csv('orders.csv')
            elif menu_selection == '2':
                print(add_new_order())
            # elif menu_selection == '3':
            #     ## TODO UPDATE ORDER STATUS
            elif menu_selection == '4':
                print(update_function('orders.csv', 'order', update_order_prompts, order_fieldnames))
            elif menu_selection == '5':
                delete_function('orders.csv', 'order', order_fieldnames)
            else:
                invalid_choice()
                continue

            if do_more_in_current_menu('ORDERS', "MAIN") == False:
                break

    else:
        invalid_choice()