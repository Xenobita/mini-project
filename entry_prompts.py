set_currency = '£'
add_product_prompts = {
    'Name': 'Enter product name: ',
    'Price': f'Enter the price of the product: {set_currency}'
}

add_courier_prompts = {
    'Name': 'Enter courier name: ',
    'Phone Number': 'Enter the courier\'s phone number:'
}

add_order_prompts = {
        'Customer Name' : 'Enter customer name: ',
        'Address': 'Enter the customer\'s full address: ',
        'Phone Number' : 'Enter the customer\'s phone number: ',
        'Products' : 'Press return key to select products for this order.\n',
        'Courier' : '''Products added to order.
Press return key to select a courier for this order\n''',
        'Order Status' : "Your order is currently PENDING"
    }

update_product_prompts = {
    'Name': 'Enter the updated name (press return key to leave unchanged): ',
    'Price': f'Enter the updated price (press return key to leave unchanged): {set_currency}'
    }

update_courier_prompts = {
    'Name': 'Enter courier name (press return key to leave unchanged): ',
    'Phone Number': 'Enter the courier\'s phone number (press return key to leave unchanged): '
    }

update_order_prompts = {
    'Customer Name' : 'Enter customer\'s updated name (press return key to leave unchanged): ',
    'Address': 'Enter the customer\'s updated full address: (press return key to leave unchanged): ',
    'Phone Number' : 'Enter the customer\'s updated phone number (press return key to leave unchanged): ',
    'Products' : 'Press return key to view IDs of products in this order.\n ',
    'Courier' : 'Press return key to view the courier assigned this order\n',
    'Order Status' : "Press return key to update the status of the order.\n"
    }