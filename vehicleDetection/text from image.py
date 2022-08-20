from pytesseract import pytesseract
from PIL import Image
pytesseract.pytesseract.tesseract_cmd = r"C:\\Pytesseract\\tesseract.exe"
img=Image.open(r'C:\Users\P.Dhanashreenydhi\Downloads\images\sample.jpg')
text=pytesseract.image_to_string(img)
print(text)
