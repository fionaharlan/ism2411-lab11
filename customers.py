# Exercise 1
customer = {
    "name": "Khloe Acker",
    "email": "khloe@example.com",
    "tier": "gold",
    "ytd_spend": 1250.50
}

# Print each field individually using key access
print(customer["name"])
print(customer["email"])
print(customer["tier"])
print(customer["ytd_spend"])

# Print the whole dictionary
print(customer)

# Exercise 2

# Add a phone field
customer["phone"] = "813-555-0199"
print(customer)

# Update the tier to "platinum"
customer["tier"] = "platinum"
print(customer)

# Delete the email field with del
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
    "name": "Alice Smith",
    "tier": "platinum",
    "ytd_spend": 1250.50,
    "phone": "813-555-0199"
}

# Iterate using .items() to get both key and value
for key, value in customer.items():
    print(f"{key}: {value}")

# If you loop through a dictionary without .items(), python only iterates over the dictionary's keys. To get the values, you would have to use brackets inside the loop. Using `.items()` is cleaner because it gives you both the key and the value at the same time