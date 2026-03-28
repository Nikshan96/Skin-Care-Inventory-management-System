import datetime
from write import write_invoice, save_products, generate_sale_invoice, generate_restock_invoice

def display_products(products):
    """
    Displays the list of available products in a formatted manner.

    Args:
        products (list): A list of dictionaries where each dictionary represents a product.

    Prints:
        - Product name, brand, quantity, selling price, and country of origin.
        - A message if no products are available.
    """
    if not products:
        print("\nNo products available.\n")
        return

    print("\nAvailable Products:")
    for i, p in enumerate(products):
        try:
            # Extract product details with default values if keys are missing
            name = p.get("name", "Unknown")
            brand = p.get("brand", "Unknown")
            quantity = p.get("quantity", 0)
            cost_price = p.get("cost_price", 0.0)
            country = p.get("country", "Unknown")

            # Calculate selling price (assumed to be double the cost price)
            selling_price = round(cost_price * 2, 2)

            print(f"{i+1}. {name} ({brand}) - {quantity} in stock - Rs. {selling_price} - {country}")
        except Exception as e:
            print(f"Error displaying product at index {i}: {e}")

    print()


def add_product(products):
    """
    Adds a new product to the product catalog.

    Args:
        products (list): A list of dictionaries where each dictionary represents a product.

    Prompts:
        - Product name, brand, quantity, cost price, and country of origin.

    Saves:
        - Updates the product list and saves it to the file.
    """
    name = input("Enter product name: ")
    brand = input("Enter brand name: ")

    # Input validation for quantity and cost price
    while True:
        try:
            quantity = int(input("Enter quantity: "))
            if quantity < 0:
                print("Quantity can't be negative. Try again.")
                continue
            break
        except ValueError:
            print("Invalid quantity. Please enter a valid number.")

    while True:
        try:
            cost_price = float(input("Enter cost price: "))
            if cost_price < 0:
                print("Cost price can't be negative. Try again.")
                continue
            break
        except ValueError:
            print("Invalid cost price. Please enter a valid number.")

    country = input("Enter country of origin: ")

    # Add new product to the list
    products.append({"name": name, "brand": brand, "quantity": quantity, "cost_price": cost_price, "country": country})

    # Save the updated products list
    save_products(products)
    print("Product added successfully.\n")


