# Product QR Code Generator (Python Project)

![Python](https://img.shields.io/badge/Python-3.x-blue.svg)  
![qrcode](https://img.shields.io/badge/Library-qrcode-green.svg)  
![Status](https://img.shields.io/badge/Status-Active-success.svg)

## Project Overview
This project generates a **QR code** containing detailed product information such as product name, ingredients, manufacture date, expiration date, harmful chemicals, and the number of days left until expiration.  
The generated QR code can be scanned by consumers to instantly view product details and ensure transparency.

## Key Features
- **Automatic Expiry Calculation:** Computes the number of days remaining until product expiration.
- **Detailed Product Information:** Encodes product details including ingredients and harmful chemicals.
- **QR Code Generation:** Creates a QR code image with embedded product data.
- **Download Support (Google Colab):** Allows easy downloading of the QR code for testing.

## Repository Contents
- `product_qr_code.py` – Main Python script for generating QR codes.
- `product_qr_code.png` – Example QR code image (generated output).
- `README.md` – Documentation for the project.

## Installation

1. Clone or download this repository.
2. Install dependencies:
   ```bash
   pip install qrcode[pil]
   ```

## Usage

### Run the script:
```bash
python product_qr_code.py
```

### Example Output:
```
✅ QR code generated and saved as 'product_qr_code.png'
```

### Scanning the QR Code:
When scanned, the QR code displays product information in the following format:
```
Product Name: Sample Product
Ingredients: Water, Sugar, Preservatives
Manufacture Date: 2024-01-01
Expiration Date: 2025-01-01
Days to Expire: 120
Harmful Chemicals: None
```

## Customization
You can easily customize the product information by modifying the variables in the script:
```python
product_name = "Your Product Name"
ingredients = "Ingredient1, Ingredient2, Ingredient3"
manufacture_date = "2024-01-01"
expiration_date = "2025-01-01"
harmful_chemicals = "None"
```

## Workflow
1. Define product details (name, ingredients, manufacture date, expiration date, chemicals).
2. Calculate days until expiration.
3. Combine all product information into a single string.
4. Generate a QR code containing the product data.
5. Save the QR code as an image (`product_qr_code.png`).
6. (Optional) Download the QR code in Google Colab.

## Tools and Technologies
- Python 3.x
- qrcode – Library for QR code generation
- Pillow (PIL) – Image processing
- Google Colab (Optional) – For testing and downloading QR codes

## File Structure
```
├── SmartLabel-QR.py          # Main Python script
├── product_qr_code.png         # Generated QR code image
└── README.md                   # Project documentation
```

## Author
Manoj Deepan M

