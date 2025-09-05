import qrcode
from datetime import datetime

def calculate_days_to_expire(expiration_date: str) -> int:
    """
    Calculate the number of days from today until the expiration date.

    Args:
        expiration_date (str): Expiration date in 'YYYY-MM-DD' format.

    Returns:
        int: Number of days until expiration.
    """
    today = datetime.today()
    exp_date = datetime.strptime(expiration_date, '%Y-%m-%d')
    return (exp_date - today).days

# --- Product Information ---
product_name = "Sample Product"
ingredients = "Water, Sugar, Preservatives"
manufacture_date = "2024-01-01"
expiration_date = "2025-01-01"
harmful_chemicals = "None"

# Calculate days until the product expires
days_to_expire = calculate_days_to_expire(expiration_date)

# Combine all product data into a dictionary
product_data = {
    "Product Name": product_name,
    "Ingredients": ingredients,
    "Manufacture Date": manufacture_date,
    "Expiration Date": expiration_date,
    "Days to Expire": days_to_expire,
    "Harmful Chemicals": harmful_chemicals
}

# Convert dictionary to a string for QR code content
product_info_str = "\n".join(f"{key}: {value}" for key, value in product_data.items())

# --- Generate QR Code ---
qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
)
qr.add_data(product_info_str)
qr.make(fit=True)

# Create image and save to file
img = qr.make_image(fill='black', back_color='white')
img.save("product_qr_code.png")

print("✅ QR code generated and saved as 'product_qr_code.png'")

# to download the qr code
from google.colab import files
files.download("product_qr_code.png")
