
items = {
    'iPhone 13': {'price': 1000, 'quantity': 10},
    'MacBook Pro': {'price': 2000, 'quantity': 5},
    'AirPods Pro': {'price': 250, 'quantity': 2},
    'iPad Pro': {'price': 800, 'quantity': 15},
    'Apple Watch Series 7': {'price': 600, 'quantity': 3},
}
cart = {}
def main():
    while True:
        display_options()
        try:
            user_choice = int(input('Enter your choice: '))
            if user_choice not in [1, 2, 3, 4, 5]:
                print('please enter number between 1 and 5')
                continue
        except:
            print('invalid option')
            continue
        if user_choice == 1:
            view_available_items(items)
        elif user_choice == 2:
            view_cart()
        elif user_choice == 3:
            print(f'the total cart prise:{total_cart_prise()}$')
        elif user_choice == 4:
            clear_cart()
        else:
            print('THANK YOU FOR VISIT CODZILLA STORE!')
            break
def display_options():
    massege = '''
1.view available items
2.view cart
3.total cart prise
4.clear cart
5.Quite
'''
    print(massege)
def view_available_items(item_dect):
    for num,item in list(enumerate(item_dect)):
        if item_dect[item]['quantity'] == 0 :
            print(f'{num+1}. {item} ,{item_dect[item]["price"]}$ (not available now)')
        else:
            print(f'{num + 1}. {item} ,{item_dect[item]["price"]}$')
    try:
        num_purchase = int(input('Enter number of item to purchase(Enter 0 to return to previous list): '))
        if num_purchase < 0 or num_purchase > len(item_dect):
            print(f'enter a number between 0 and {len(item_dect)}')
            return
    except:
        print('invalid options')
        return
    if num_purchase == 0:
        return
    else:
        purchase_item = list(enumerate(item_dect))[num_purchase - 1][1]
        if item_dect[purchase_item]['quantity']==0:
            print('not available now')
            return
        else:
            print(f'Available Quantity : {item_dect[purchase_item]["quantity"]}')
        try:
            purchase_item_quantity = int(input('please enter the quantity: '))
            if purchase_item_quantity > item_dect[purchase_item]["quantity"]:
                print(f'sorry, we only have {item_dect[purchase_item]["quantity"]} for this item')
                return
            elif purchase_item_quantity < 1 :
                print('invalid option')
                return
        except:
            print('invalid option')
            return
        item_dect[purchase_item]["quantity"] -= purchase_item_quantity
        if purchase_item in cart:
             cart[purchase_item]['quantity'] += purchase_item_quantity
        else:
            purchase_item_info = {
                purchase_item: {
                    'price': item_dect[purchase_item]['price'],
                    'quantity': purchase_item_quantity,
                }
            }
            cart.update(purchase_item_info)
        print(f'{purchase_item} add to cart successfully')
def view_cart():
    if cart == {}:
        print('no item in cart')
    else:
        print('the cart:')
        print('-'*30)
        for num , item in list(enumerate(cart)):
                print(f'{num+1}. {item},{cart[item]["quantity"]} units x {cart[item]["price"]}$ = {cart[item]["quantity"]*cart[item]["price"]}$')
        print('-' * 30)
        print(f'the total: {total_cart_prise()}$')
def total_cart_prise():
    total = 0
    for item in cart:
        total += cart[item]["price"]*cart[item]['quantity']
    return total
def clear_cart():
    if cart == {}:
        print('no items in cart for clear it !!')
        return
    elif len(cart) == 1 :
        print('the item in cart before cleared:')
    else:
        print('the items in cart before cleared:')
    view_cart()
    choice = input('are you sure to clear cart(y,n): ')
    if choice == "y".lower():
        cart.clear()
        print('the cart cleared')
    elif choice == "n".lower():
        return
    else:
        print('inviled option')



if __name__ == main():
    main()