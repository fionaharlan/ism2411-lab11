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