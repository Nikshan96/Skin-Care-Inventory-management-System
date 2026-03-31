import datetime

def write_invoice(filename, lines):
    """
    Writes the given lines to a file.

    Args:
        filename (str): The name of the file to write the invoice to.
        lines (list): A list of strings, where each string is a line to be written to the file.

    Functionality:
        - Opens the specified file in write mode.
        - Writes each line from the `lines` list to the file.
    """
    with open(filename, "w") as file:
        for line in lines:
            file.write(line + "\n")


def save_products(products, filename="products.txt"):
    """
    Saves the product list to the specified file.

    Args:
        products (list): A list of dictionaries where each dictionary represents a product.
        filename (str): The name of the file to save the product data to (default is "products.txt").

    Functionality:
        - Iterates through the product list.
        - Formats each product as a comma-separated string.
        - Writes the formatted strings to the specified file.
    """
    with open(filename, "w") as file:
        for p in products:
            # Format product details as a single line
            line = f"{p['name']},{p['brand']},{p['quantity']},{p['cost_price']},{p['country']}"
            file.write(line + "\n")


def generate_unique_filename(prefix):
    """
    Generates a unique filename using the current timestamp.

    Args:
        prefix (str): A prefix for the filename (e.g., "sale" or "restock").

    Returns:
        str: A unique filename in the format "<prefix>_YYYYMMDD_HHMMSS.txt".

    Functionality:
        - Uses the current date and time to generate a timestamp.
        - Combines the prefix and timestamp to create a unique filename.
    """
    return f"{prefix}_{datetime.datetime.now().strftime('%Y%m%d_%H%M%S')}.txt"


def generate_sale_invoice(customer, product, paid_qty, free_qty, rate, total, vat_rate=0.18):
    """
    Generates a sale invoice and writes it to a file.

    Args:
        customer (str): The name of the customer.
        product (dict): A dictionary representing the product sold.
        paid_qty (int): The quantity of the product paid for by the customer.
        free_qty (int): The quantity of the product given for free.
        rate (float): The selling price per unit of the product.
        total (float): The total amount paid by the customer (excluding free items).
        vat_rate (float): The VAT rate to be applied (default is 18%).

    Functionality:
        - Calculates VAT and grand total.
        - Creates a formatted invoice with sale details.
        - Generates a unique filename for the invoice.
        - Writes the invoice to the file using `write_invoice`.
    """
    # Calculate VAT and grand total
    vat_amount = total * vat_rate
    grand_total = total + vat_amount

    # Generate a unique filename for the invoice
    filename = generate_unique_filename("sale")

    # Create the invoice lines
    lines = [
        "===============================",
        "          SALE INVOICE         ",
        "===============================",
        f"Customer Name: {customer}",
        f"Date: {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}",
        "-------------------------------",
        f"Product Name: {product['name']}",
        f"Brand: {product['brand']}",
        f"Quantity Sold: {paid_qty} (Paid)",
        f"Free Quantity: {free_qty}",
        f"Rate per Item: Rs. {rate:.2f}",
        "-------------------------------",
        f"Subtotal (excluding free items): Rs. {total:.2f}",
        f"VAT ({vat_rate * 100:.0f}%): Rs. {vat_amount:.2f}",
        f"Grand Total: Rs. {grand_total:.2f}",
        "===============================",
        "       Thank You for Shopping! ",
        "==============================="
    ]

    # Write the invoice to the file
    write_invoice(filename, lines)


def generate_restock_invoice(vendor, product, qty, rate, total):
    """
    Generates a restock invoice and writes it to a file.

    Args:
        vendor (str): The name of the vendor supplying the product.
        product (dict): A dictionary representing the product restocked.
        qty (int): The quantity of the product restocked.
        rate (float): The cost price per unit of the product.
        total (float): The total cost of the restocked products.

    Functionality:
        - Creates a list of invoice lines with restock details.
        - Generates a unique filename for the invoice.
        - Writes the invoice to the file using `write_invoice`.
    """
    filename = generate_unique_filename("restock")
    lines = [
        f"Vendor: {vendor}",
        f"Date: {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}",
        f"Product: {product['name']}",
        f"Brand: {product['brand']}",
        f"Quantity Restocked: {qty}",
        f"Rate: Rs. {rate}",
        f"Total: Rs. {total}"
    ]
    write_invoice(filename, lines)