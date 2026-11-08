# 1. Bracket notation will crash a program if the key does not exist. this is good for debugging because it will show exactly where the error is. .get() gives you a backup value instead of crashing, which is better for optional or messier data.
# 2. The pattern reminds me of an Excel PivotTable, where you can summarize data by categories. Python handles bigger datasets faster and more efficiently than excel without making you drag formulas across a spreadsheet.


# Exercise 1
customer = {
    "name": "Khloe Acker",
    "email": "khloe@example.com",
    "tier": "gold",
    "ytd_spend": 1250.50
}

print(customer["name"])
print(customer["email"])
print(customer["tier"])
print(customer["ytd_spend"])

print(customer)

# Exercise 2

customer["phone"] = "813-555-0199"
print(customer)

customer["tier"] = "platinum"
print(customer)

del customer["email"]
print(customer)

# Exercise 3

email_result = customer.get("email", "no email on file")
print(email_result)

try:
    print(customer["email"])
except KeyError:
    print("KeyError caught: 'email' key does not exist in this dictionary.")

# exercise 4

customer = {
    "name": "Khloe Acker",
    "tier": "platinum",
    "ytd_spend": 1250.50,
    "phone": "813-555-0199"
}

# Iterate using .items() to get both key and value
for key, value in customer.items():
    print(f"{key}: {value}")

# If you loop through a dictionary without .items(), python only iterates over the dictionary's keys. To get the values, you would have to use brackets inside the loop. Using `.items()` is cleaner because it gives you both the key and the value at the same time

# exercise 5

tier_discounts = {
    "bronze": 0, 
    "silver": 0.05, 
    "gold": 0.10, 
    "platinum": 0.15
}

customer = {
    "name": "Khloe Acker",
    "tier": "platinum",
    "ytd_spend": 1250.50,
    "phone": "813-555-0199"
}

tier = customer.get("tier", "bronze")
discount_rate = tier_discounts.get(tier, 0)

original_price = 200.00
discount = original_price * discount_rate
final_price = original_price - discount

print(f"Tier: {tier}")
print(f"Discount Rate: {discount_rate * 100}%")
print(f"Final Price for $200 purchase: ${final_price:.2f}")

# exercise 6 

customers = [
    {"name": "Khloe Acker", "tier": "platinum", "ytd_spend": 1250.50},
    {"name": "Bob", "tier": "silver", "ytd_spend": 450.00},
    {"name": "Rob", "tier": "bronze", "ytd_spend": 120.00}
]

purchase_amount = 300.00

for customer in customers:
    tier = customer.get("tier", "bronze")
    discount_rate = tier_discounts.get(tier, 0)
    discount = purchase_amount * discount_rate
    
    print(f"Name: {customer['name']} | Tier: {tier.capitalize()} | Discount on ${purchase_amount:.2f}: ${discount:.2f}")

# exercise 7 

catalog = {
    "Widget A": {"price": 9.99, "stock": 150},
    "Gadget C": {"price": 49.99, "stock": 8}
}

for product, details in catalog.items():
    stock_level = details["stock"]
    
 
    if stock_level < 20:
        print(f"LOW STOCK ALERT: {product} only has {stock_level} units left")
    else:
        print(f"{product} has enough stock.")

# exercise 8

transactions = [
    {"region": "South", "amount": 300}, 
    {"region": "North", "amount": 150}, 
    {"region": "South", "amount": 200}
]

regional_sales = {}

for tx in transactions:
    region = tx["region"]
    amount = tx["amount"]
    
    regional_sales[region] = regional_sales.get(region, 0) + amount

print("Sales Summary by Region:")
for region in sorted(regional_sales.keys()):
    print(f"{region}: {regional_sales[region]}")