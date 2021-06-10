import datetime
import os
from dotenv import load_dotenv
load_dotenv()
from pandas import read_csv

csv_filepath = "data/products.csv"
products_df = read_csv(csv_filepath)



products1 = products_df.to_dict("records")



#please refer to csv file at data/products.csv instead- commenting out hard-coded list of products
# products = [
#     {"id":1, "name": "Chocolate Sandwich Cookies", "department": "snacks", "aisle": "cookies cakes", "price": 3.50},
#     {"id":2, "name": "All-Seasons Salt", "department": "pantry", "aisle": "spices seasonings", "price": 4.99},
#     {"id":3, "name": "Robust Golden Unsweetened Oolong Tea", "department": "beverages", "aisle": "tea", "price": 2.49},
#     {"id":4, "name": "Smart Ones Classic Favorites Mini Rigatoni With Vodka Cream Sauce", "department": "frozen", "aisle": "frozen meals", "price": 6.99},
#     {"id":5, "name": "Green Chile Anytime Sauce", "department": "pantry", "aisle": "marinades meat preparation", "price": 7.99},
#     {"id":6, "name": "Dry Nose Oil", "department": "personal care", "aisle": "cold flu allergy", "price": 21.99},
#     {"id":7, "name": "Pure Coconut Water With Orange", "department": "beverages", "aisle": "juice nectars", "price": 3.50},
#     {"id":8, "name": "Cut Russet Potatoes Steam N' Mash", "department": "frozen", "aisle": "frozen produce", "price": 4.25},
#     {"id":9, "name": "Light Strawberry Blueberry Yogurt", "department": "dairy eggs", "aisle": "yogurt", "price": 6.50},
#     {"id":10, "name": "Sparkling Orange Juice & Prickly Pear Beverage", "department": "beverages", "aisle": "water seltzer sparkling water", "price": 2.99},
#     {"id":11, "name": "Peach Mango Juice", "department": "beverages", "aisle": "refrigerated", "price": 1.99},
#     {"id":12, "name": "Chocolate Fudge Layer Cake", "department": "frozen", "aisle": "frozen dessert", "price": 18.50},
#     {"id":13, "name": "Saline Nasal Mist", "department": "personal care", "aisle": "cold flu allergy", "price": 16.00},
#     {"id":14, "name": "Fresh Scent Dishwasher Cleaner", "department": "household", "aisle": "dish detergents", "price": 4.99},
#     {"id":15, "name": "Overnight Diapers Size 6", "department": "babies", "aisle": "diapers wipes", "price": 25.50},
#     {"id":16, "name": "Mint Chocolate Flavored Syrup", "department": "snacks", "aisle": "ice cream toppings", "price": 4.50},
#     {"id":17, "name": "Rendered Duck Fat", "department": "meat seafood", "aisle": "poultry counter", "price": 9.99},
#     {"id":18, "name": "Pizza for One Suprema Frozen Pizza", "department": "frozen", "aisle": "frozen pizza", "price": 12.50},
#     {"id":19, "name": "Gluten Free Quinoa Three Cheese & Mushroom Blend", "department": "dry goods pasta", "aisle": "grains rice dried goods", "price": 3.99},
#     {"id":20, "name": "Pomegranate Cranberry & Aloe Vera Enrich Drink", "department": "beverages", "aisle": "juice nectars", "price": 4.25}
# based on data from Instacart: https://www.instacart.com/datasets/grocery-shopping-2017


def to_usd(my_price):
    """
    Converts a numeric value to usd-formatted string, for printing and display purposes.

    Param: my_price (int or float) like 4000.444444

    Example: to_usd(4000.444444)

    Returns: $4,000.44
    """
    return f"${my_price:,.2f}" #> $12,000.71



#Accept a user input value, store it in a variable, and print it. HINT: use the input() function

product_ids=[]
for p in products1:
    product_ids.append(str(p["id"]))

selected_ids=[]
while True:
    selected_id = input("Please enter a product identifier and hit 'enter'; write 'DONE' when there are no more items: ")
    if selected_id.upper() == "DONE":
        break
    else:
        if str(selected_id) in product_ids:
            selected_id=str(selected_id)
            selected_ids.append(selected_id)
        else:
            print("That ID is not valid, please enter another.")
print("-------------")
print("NORA'S GROCERY")
now= datetime.datetime.now()
now_formatted=now.strftime("%Y-%m-%d %H:%M:%S %p")
print("CHECKOUT AT:", now_formatted)
print("-------------")
if len(selected_ids)==0:
    print("No Items")
else:
    print("SELECTED PRODUCTS:")


#create a list of matching product ids by looping through the products list and seeing if each ID is in the selected_list list.  
matching_products=[]
subtotal=[]
for p in products1:
    if str(p["id"]) in selected_ids:
        matching_products.append(p)
for product in matching_products:
    product_name=product["name"]
    price_num=product["price"]
    price_str=to_usd(product["price"])
    subtotal.append(price_num)
    print(f"...{product_name} ({price_str})")

print("-------------")
subtotal_sum=to_usd(sum(subtotal))
print(f"SUBTOTAL: {subtotal_sum}")
tax_from_env=float(os.environ["TAX_RATE"])
tax_raw=tax_from_env*sum(subtotal)
tax=to_usd(tax_from_env*sum(subtotal))
print(f"TAX: {tax}")
total=to_usd(sum(subtotal)+tax_raw)
print(f"TOTAL: {total}")
print("-------------")
print("THANKS, SEE YOU AGAIN SOON!")
print("-------------")

