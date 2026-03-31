def read_products(filename):
    """
    Reads product data from a file and returns a list of product dictionaries.

    Args:
        filename (str): The path to the file containing product data.

    Returns:
        list: A list of dictionaries where each dictionary represents a product with the following keys:
              - "name" (str): The name of the product.
              - "brand" (str): The brand of the product.
              - "quantity" (int): The available stock quantity.
              - "cost_price" (float): The cost price of the product.
              - "country" (str): The country of origin.

    Prints:
        - Skips and logs invalid lines that do not match the expected format.
        - Logs errors for lines with invalid data types.
        - Displays the total number of products loaded.
    """
    products = []  # Initialize an empty list to store product data

    try:
        # Open the file in read mode
        with open(filename, "r") as file:
            # Read the file line by line
            for line_number, line in enumerate(file, start=1):
                # Split the line into parts using a comma as the delimiter
                parts = line.strip().split(",")
                
                # Check if the line has exactly 5 parts
                if len(parts) != 5:
                    print(f"Skipping invalid line {line_number}: '{line.strip()}'")
                    continue
                
                try:
                    # Extract product details and convert to appropriate data types
                    name, brand, quantity, cost_price, country = parts
                    products.append({
                        "name": name,
                        "brand": brand,
                        "quantity": int(quantity),
                        "cost_price": float(cost_price),
                        "country": country
                    })
                except ValueError as e:
                    # Handle errors in data conversion (e.g., invalid integers or floats)
                    print(f"Error in line {line_number}: {e}")
    except FileNotFoundError:
        # Handle the case where the file does not exist
        print(f"Error: File '{filename}' not found.")
    
    # Print the total number of products loaded
    print(f"Loaded {len(products)} products.")
    
    return products
