menu = {"classic pizza":299,
        "chicken burger":149,
        "butter garlic fries":75,
        "rose pasta":199,
        "paneer momos":120,
        "cappuccino":99,
        "cold coffee":149}

items = {1:"classic pizza",
        2:"chicken burger",
        3:"butter garlic fries",
        4:"rose pasta",
        5:"paneer momos",
        6:"cappuccino",
        7:"cold coffee"}



def cafeorder():
    total = 0

    print("Welcome to Py Cafe. Here's the menu,")
    print("1 - Classic Pizza\n2 - Chicken Burger\n3 - Butter Garlic Fries\n4 - Rose Pasta\n5 - Paneer Momos\n5 - Cappuccino\n7 - Cold Coffee")

    while True:
        item = int(input("\nPlease choose your order(1-6): "))
        print(f"{items[item]} added to order")

        if item in items:
            selected_item = items[item]
            price = menu[selected_item]
            total += price
        else:
            print("\nSorry item not in menu yet")

        more = input("\nDo you want to order anything else? (yes/no)- ").lower()

        if more == "no":
            break
    
    print(f"\nYour total bill is {total} rupees. Thank you for ordering with us!")

cafeorder()

