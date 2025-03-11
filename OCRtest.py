import pytesseract
from PIL import Image

# Tesseract のパスを設定（Windows の場合）
pytesseract.pytesseract.tesseract_cmd = r"C:\Users\s\AppData\Local\Programs\Tesseract-OCR\tesseract.exe"

# 画像を開く
image = Image.open(r"C:\Users\s\Pictures\test2.jpg")

# OCRで文字認識
text = pytesseract.image_to_string(image, lang="eng+jpn")

print(text)