from read import read_products
from operation import display_products, add_product, restock_product, sell_product

def main():
    """
    Main function to run the WeCare Skin Product System.

    This program allows users to:
    1. Display the list of available products.
    2. Add a new product to the catalog.
    3. Restock an existing product.
    4. Sell a product with the "Buy 3 Get 1 Free" scheme.
    5. Exit the system.

    The program reads product data from a file and provides a menu-driven interface
    for performing operations on the product catalog.

    Features:
    - Displays the list of products with details such as name, brand, quantity, and price.
    - Allows users to add new products to the catalog.
    - Enables restocking of existing products by updating their quantity and cost price.
    - Implements a "Buy 3 Get 1 Free" scheme for selling products.
    - Ensures data persistence by saving updates to the product file.
    """
    # Define the file path to the product data file
    filename = r"D:\Year 1\FOC\Coursework\products.txt"  # Replace with the correct file path

    # Load product data from the file
    products = read_products(filename)

    # Menu-driven interface for user interaction
    while True:
        # Display the main menu
        print("Welcome to WeCare Skin Product System")
        print("1. Display Products")
        print("2. Add New Product")
        print("3. Restock Product")
        print("4. Sell Product")
        print("5. Exit")
        Select = input("Enter your choice: ")

        # Handle user selection
        if Select == '1':
            # Display the list of available products
            display_products(products)
        elif Select == '2':
            # Add a new product to the catalog
            add_product(products)
        elif Select == '3':
            # Restock an existing product
            restock_product(products)
        elif Select == '4':
            # Sell a product with the "Buy 3 Get 1 Free" scheme
            sell_product(products)
        elif Select == '5':
            # Exit the system
            print("Thank you for using WeCare System.")
            break
        else:
            # Handle invalid input
            print("Invalid choice. Try again.\n")

# Entry point of the program
if __name__ == "__main__":
    main()
