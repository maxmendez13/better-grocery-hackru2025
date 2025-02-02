import sys

# takes shoppers cart data and organizes it with

#fake data set for the sake of example
food_products = [
    {'item_id': 4011, 'item_name': 'Bananas', 'item_type': 'produce', 'aisle': 1, 'price': 3.99},
    {'item_id': 4025, 'item_name': 'Hass Avocados', 'item_type': 'produce', 'aisle': 1, 'price': 5.99},
    {'item_id': 514011, 'item_name': 'Vanilla Ice Cream', 'item_type': 'frozen', 'aisle': 18, 'price': 3.99},
    {'item_id': 3283, 'item_name': 'Honeycrisp Apples', 'item_type': 'produce', 'aisle': 1, 'price': 2.99},
    {'item_id': 654321, 'item_name': 'Black Beans', 'item_type': 'canned', 'aisle': 6, 'price': 4.50},
    {'item_id': 5461894, 'item_name': 'Brown Rice', 'item_type': 'grain', 'aisle': 9, 'price': 7.99},
    {'item_id': 211204, 'item_name': 'AA Batteries', 'item_type': 'electronics', 'aisle': 12, 'price': 5.39},
    {'item_id': 654650, 'item_name': 'Phone Charger', 'item_type': 'electronics', 'aisle': 12, 'price': 3.99},
    {'item_id': 251025, 'item_name': 'Ground Beef', 'item_type': 'meat', 'aisle': 10, 'price': 12.50},
    {'item_id': 415421, 'item_name': 'Campbells Soup', 'item_type': 'canned', 'aisle': 6, 'price': 3.99},
    {'item_id': 545341, 'item_name': 'Pork Shoulder', 'item_type': 'meat', 'aisle': 10, 'price': 13.99},
    {'item_id': 123456, 'item_name': 'Whole Milk', 'item_type': 'dairy', 'aisle': 3, 'price': 4.29},
    {'item_id': 234567, 'item_name': 'Cheddar Cheese', 'item_type': 'dairy', 'aisle': 3, 'price': 5.99},
    {'item_id': 345678, 'item_name': 'Greek Yogurt', 'item_type': 'dairy', 'aisle': 3, 'price': 6.49},
    {'item_id': 456789, 'item_name': 'Almond Milk', 'item_type': 'dairy', 'aisle': 3, 'price': 3.99},
    {'item_id': 567890, 'item_name': 'Cage-Free Eggs', 'item_type': 'dairy', 'aisle': 3, 'price': 4.99},
    {'item_id': 678901, 'item_name': 'Organic Tofu', 'item_type': 'produce', 'aisle': 2, 'price': 3.50},
    {'item_id': 789012, 'item_name': 'Carrots', 'item_type': 'produce', 'aisle': 1, 'price': 2.49},
    {'item_id': 890123, 'item_name': 'Broccoli', 'item_type': 'produce', 'aisle': 1, 'price': 3.29},
    {'item_id': 901234, 'item_name': 'Baby Spinach', 'item_type': 'produce', 'aisle': 1, 'price': 4.19},
    {'item_id': 101112, 'item_name': 'Frozen Pizza', 'item_type': 'frozen', 'aisle': 19, 'price': 8.99},
    {'item_id': 111213, 'item_name': 'Chicken Nuggets', 'item_type': 'frozen', 'aisle': 18, 'price': 7.99},
    {'item_id': 121314, 'item_name': 'Blueberries', 'item_type': 'produce', 'aisle': 1, 'price': 5.49},
    {'item_id': 131415, 'item_name': 'Raspberries', 'item_type': 'produce', 'aisle': 1, 'price': 6.99},
    {'item_id': 141516, 'item_name': 'Grapes', 'item_type': 'produce', 'aisle': 1, 'price': 4.59},
    {'item_id': 151617, 'item_name': 'Lettuce', 'item_type': 'produce', 'aisle': 1, 'price': 2.99},
    {'item_id': 161718, 'item_name': 'Canned Tuna', 'item_type': 'canned', 'aisle': 6, 'price': 3.79},
    {'item_id': 171819, 'item_name': 'Pasta', 'item_type': 'grain', 'aisle': 9, 'price': 2.49},
    {'item_id': 181920, 'item_name': 'Tomato Sauce', 'item_type': 'canned', 'aisle': 6, 'price': 3.29},
    {'item_id': 192021, 'item_name': 'Peanut Butter', 'item_type': 'canned', 'aisle': 7, 'price': 4.99},
    {'item_id': 202122, 'item_name': 'Jelly', 'item_type': 'canned', 'aisle': 7, 'price': 3.99},
    {'item_id': 212223, 'item_name': 'Cereal', 'item_type': 'grain', 'aisle': 9, 'price': 5.99},
    {'item_id': 222324, 'item_name': 'Oatmeal', 'item_type': 'grain', 'aisle': 9, 'price': 3.49},
    {'item_id': 232425, 'item_name': 'Trail Mix', 'item_type': 'snack', 'aisle': 5, 'price': 6.29},
    {'item_id': 242526, 'item_name': 'Potato Chips', 'item_type': 'snack', 'aisle': 5, 'price': 4.49},
    {'item_id': 252627, 'item_name': 'Granola Bars', 'item_type': 'snack', 'aisle': 5, 'price': 3.99},
    {'item_id': 262728, 'item_name': 'Chocolate Bar', 'item_type': 'snack', 'aisle': 5, 'price': 2.99},
    {'item_id': 272829, 'item_name': 'Energy Drink', 'item_type': 'beverage', 'aisle': 4, 'price': 3.49},
    {'item_id': 282930, 'item_name': 'Orange Juice', 'item_type': 'beverage', 'aisle': 4, 'price': 4.99},
    {'item_id': 292931, 'item_name': 'Bottled Water', 'item_type': 'beverage', 'aisle': 4, 'price': 1.99},
    {'item_id': 303132, 'item_name': 'Soda', 'item_type': 'beverage', 'aisle': 4, 'price': 2.99},
    {'item_id': 313233, 'item_name': 'Coffee Beans', 'item_type': 'beverage', 'aisle': 4, 'price': 9.99},
    {'item_id': 323334, 'item_name': 'Green Tea', 'item_type': 'beverage', 'aisle': 4, 'price': 5.49},
    {'item_id': 333435, 'item_name': 'Shampoo', 'item_type': 'personal care', 'aisle': 11, 'price': 6.99},
    {'item_id': 343536, 'item_name': 'Toothpaste', 'item_type': 'personal care', 'aisle': 11, 'price': 3.99},
    {'item_id': 353637, 'item_name': 'Body Wash', 'item_type': 'personal care', 'aisle': 11, 'price': 5.49},
    {'item_id': 363738, 'item_name': 'Deodorant', 'item_type': 'personal care', 'aisle': 11, 'price': 4.99},
    {'item_id': 373839, 'item_name': 'Dish Soap', 'item_type': 'household', 'aisle': 13, 'price': 2.99},
    {'item_id': 383940, 'item_name': 'Laundry Detergent', 'item_type': 'household', 'aisle': 13, 'price': 12.99},
    {'item_id': 393041, 'item_name': 'Paper Towels', 'item_type': 'household', 'aisle': 13, 'price': 7.99},
    {'item_id': 403142, 'item_name': 'Toilet Paper', 'item_type': 'household', 'aisle': 13, 'price': 8.99},
    {'item_id': 413243, 'item_name': 'Light Bulbs', 'item_type': 'household', 'aisle': 13, 'price': 6.49},
    {'item_id': 423344, 'item_name': 'Dog Food', 'item_type': 'pet', 'aisle': 15, 'price': 19.99},
    {'item_id': 433445, 'item_name': 'Cat Food', 'item_type': 'pet', 'aisle': 15, 'price': 17.99},
    {'item_id': 443546, 'item_name': 'Fish Food', 'item_type': 'pet', 'aisle': 15, 'price': 6.99},
    {'item_id': 453647, 'item_name': 'Bird Seed', 'item_type': 'pet', 'aisle': 15, 'price': 9.49},
    {'item_id': 463748, 'item_name': 'Dog Treats', 'item_type': 'pet', 'aisle': 15, 'price': 4.99},
    {'item_id': 473849, 'item_name': 'Cat Litter', 'item_type': 'pet', 'aisle': 15, 'price': 14.99},
    {'item_id': 483950, 'item_name': 'Frozen Berries', 'item_type': 'frozen', 'aisle': 18, 'price': 6.99},
    {'item_id': 494051, 'item_name': 'Frozen Vegetables', 'item_type': 'frozen', 'aisle': 18, 'price': 4.99},
    {'item_id': 504152, 'item_name': 'Beef Steak', 'item_type': 'meat', 'aisle': 10, 'price': 15.99},
    {'item_id': 514253, 'item_name': 'Chicken Breast', 'item_type': 'meat', 'aisle': 10, 'price': 8.99},
    {'item_id': 524354, 'item_name': 'Salmon Fillet', 'item_type': 'meat', 'aisle': 10, 'price': 13.99},
    {'item_id': 534455, 'item_name': 'Turkey Sausage', 'item_type': 'meat', 'aisle': 10, 'price': 6.99},
    {'item_id': 544556, 'item_name': 'Bacon', 'item_type': 'meat', 'aisle': 10, 'price': 7.99},
    {'item_id': 554657, 'item_name': 'Maple Syrup', 'item_type': 'canned', 'aisle': 7, 'price': 9.99},
    {'item_id': 564758, 'item_name': 'Olive Oil', 'item_type': 'canned', 'aisle': 7, 'price': 12.99},
    {'item_id': 574859, 'item_name': 'Soy Sauce', 'item_type': 'canned', 'aisle': 7, 'price': 3.99},
    {'item_id': 584960, 'item_name': 'Hot Sauce', 'item_type': 'canned', 'aisle': 7, 'price': 2.99},
    {'item_id': 594061, 'item_name': 'Balsamic Vinegar', 'item_type': 'canned', 'aisle': 7, 'price': 5.99},
    {'item_id': 604162, 'item_name': 'Whole Wheat Bread', 'item_type': 'baked', 'aisle': 8, 'price': 3.99},
    {'item_id': 614263, 'item_name': 'Bagels', 'item_type': 'baked', 'aisle': 8, 'price': 4.49},
    {'item_id': 624364, 'item_name': 'Croissants', 'item_type': 'baked', 'aisle': 8, 'price': 5.99},
    {'item_id': 634465, 'item_name': 'Muffins', 'item_type': 'baked', 'aisle': 8, 'price': 4.99},
    {'item_id': 644566, 'item_name': 'Baguette', 'item_type': 'baked', 'aisle': 8, 'price': 3.49},
    {'item_id': 654667, 'item_name': 'Pita Bread', 'item_type': 'baked', 'aisle': 8, 'price': 2.99},
    {'item_id': 664768, 'item_name': 'Brown Rice', 'item_type': 'grain', 'aisle': 9, 'price': 6.99},
    {'item_id': 674869, 'item_name': 'Quinoa', 'item_type': 'grain', 'aisle': 9, 'price': 7.99},
    {'item_id': 684970, 'item_name': 'Couscous', 'item_type': 'grain', 'aisle': 9, 'price': 4.49},
    {'item_id': 695071, 'item_name': 'Barley', 'item_type': 'grain', 'aisle': 9, 'price': 3.79},
    {'item_id': 705172, 'item_name': 'Cornmeal', 'item_type': 'grain', 'aisle': 9, 'price': 2.99}
]


item_priority = [
    {'item_type':'produce', 'priority_level':1},
    {'item_type':'canned', 'priority_level':1},
    {'item_type':'meat', 'priority_level':2},
    {'item_type':'frozen', 'priority_level':3},
    {'item_type':'pet', 'priority_level':1},
    {'item_type':'grain', 'priority_level':2},
    {'item_type':'household', 'priority_level':1},
    {'item_type':'dairy', 'priority_level':2},
    {'item_type':'personal care', 'priority_level':2},
    {'item_type':'beverage', 'priority_level':2},
    {'item_type':'electronic', 'priority_level':1},
    {'item_type':'snack', 'priority_level':1},
    {'item_type':'baked', 'priority_level':0}
]

def sortingByAisle(e):
    return e['aisle']

food_products.sort(key=sortingByAisle)
#print(food_products)

def sortingByPriorityLevel(e):
    return e['priority_level']

item_priority.sort(key=sortingByPriorityLevel)
#print(item_priority)

cart = []

def item_catalogue():
    #use the dictionary and output it in a readable format
    #maybe a line that checks the item product and when it sees a new product type it outputs it
    uniqueType = ""
    for x in food_products:
        if uniqueType != x.get('item_type'):
            uniqueType = x.get('item_type')
            print("\n--------------"+uniqueType+"--------------")
        for key, value in x.items():
            
            if key == 'item_name' or key == 'price':
                sys.stdout.write(f"{value} ")
        sys.stdout.write('\n')


def add_to_cart():
    flag = True
    while flag:
        answer = input("Enter the name or ID of the item you would like to add to your cart\nEnter 'Q' to quit\n")
        if answer.lower() == 'q':
            flag = False
            continue
        check = 'item_id'
        try:
            val = int(answer)
        except ValueError:
            check = 'item_name'
        
        if check == 'item_id':
            answer = int(answer)
        # when it's item_id only check id when name only check name
        for x in food_products:
            if x.keys()[x.values().index(answer)] != None:
                cart.append(x.get("item_id"))
                break
    


# portion where person does shopping
def main():
    flag = True
    while flag:
        print('Hello welcome to RiteShop! Select one of the following: \n1 Look at items \n2 Add item to cart \n3 Check cart \n4 Generate shopping list \n5 Quit')
        answer = input()
        try:
            val = int(answer)
        except ValueError:
            print("Please enter a valid option")
            continue

        answer = int(answer)
        if answer == 1:
            item_catalogue()
        elif answer == 2:
            add_to_cart()
        elif answer == 3:
            ajsdkajsd
        elif answer == 4:
            asjdkasdjl
        elif answer == 5:
            print("Thank you for using RiteShop!")
            flag = False
        else:
            print("Please enter a valid option")


main()