"""Program for extract text using OCR (Optical Character Recognition) technique since images files

Source:
    https://www.geeksforgeeks.org/python-reading-contents-of-pdf-using-ocr-optical-character-recognition/
"""

import os
from pytesseract import image_to_string
from PIL import Image

# Path of the input image
DATA_PATH = os.path.dirname( os.path.abspath(__file__) ) + os.sep + "data" + os.sep
FILE_NAME = 'invoice_parts'
IMG_FILE = DATA_PATH + f"{FILE_NAME}.jpg"
TEXT_FILE = DATA_PATH + f"{FILE_NAME}.txt"

# Open the file in append mode so that
# All contents of an image are added to the same file
with open(TEXT_FILE, "a") as output_file:
    # Recognize the text as string in image using pytesserct
    text = str( ( ( image_to_string( Image.open(IMG_FILE) ) ) ) )

    # To remove this, we replace every '-\n' to ''.
    text = text.replace("-\n", "")

    # Finally, write the processed text to the file.
    output_file.write(text)
