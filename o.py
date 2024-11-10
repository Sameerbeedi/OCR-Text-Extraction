import pytesseract
from PIL import Image

img_path = "data/flip2.png"
no_noise = "temp/no_noise.jpg"

img = Image.open(img_path)

try:
    ocr_result = pytesseract.image_to_string(img)
    print(ocr_result)
except Exception as e:
    print(f"Error: {e}")
