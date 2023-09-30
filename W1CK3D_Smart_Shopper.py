# Initialize variables to store customer's total cost and itemization
total_cost = 0
customer_itemization = ""

# Get product details from user input
while True:
    product_name = input("Enter product name (or 'done' to finish): ")
    if product_name.lower() == 'done':
        break
    
    product_description = input("Enter product description: ")
    
    # Get product price; handle invalid inputs
    while True:
        try:
            product_price = float(input("Enter product price: $"))
            if product_price <= 0:
                raise ValueError
            break
        except ValueError:
            print("Invalid input. Please enter a valid positive price.")

    # Get quantity; handle invalid inputs
    while True:
        try:
            quantity = int(input("Enter quantity: "))
            if quantity <= 0:
                raise ValueError
            break
        except ValueError:
            print("Invalid input. Please enter a valid positive quantity.")

    # Calculate total price for this product and add it to the customer's total cost
    total_price = product_price * quantity
    total_cost += total_price

    # Add product details to itemization
    customer_itemization += f"{product_name}: {product_description} - ${product_price:.2f} x {quantity}\n"

# Calculate sales tax (assuming a fixed tax rate of 8.8%)
sales_tax_rate = 0.088
sales_tax = total_cost * sales_tax_rate

# Calculate final total cost including sales tax
final_total = total_cost + sales_tax

# Print receipt
print("\nCustomer Receipt:")
print(customer_itemization)
print(f"Total Cost: ${total_cost:.2f}")
print(f"Sales Tax (8.8%): ${sales_tax:.2f}")
print(f"Final Total: ${final_total:.2f}")
