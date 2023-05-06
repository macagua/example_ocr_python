"""Program for extract text since images files.

Program for extract text using OCR (Optical Character Recognition)
technique since images files

Source:
    https://www.geeksforgeeks.org/python-reading-contents-of-pdf-using-ocr-optical-character-recognition/
"""

import os

from PIL import Image
from pytesseract import image_to_string

# Path of the input image
DATA_PATH = os.path.dirname(os.path.abspath(__file__)) +\
    os.sep + "data" + os.sep
FILE_NAME = "invoice_parts"
IMG_FILE = DATA_PATH + f"{FILE_NAME}.jpg"
TEXT_FILE = DATA_PATH + f"{FILE_NAME}.txt"

# Open the file in append mode so that
# All contents of an image are added to the same file
with open(TEXT_FILE, "a", encoding="utf-8") as output_file:
    # Recognize the text as string in image using pytesserct
    TEXT_EXTRACTED = str(((image_to_string(Image.open(IMG_FILE), lang='eng+spa'))))

    # To remove this, we replace every '-\n' to ''.
    TEXT_EXTRACTED = TEXT_EXTRACTED.replace("-\n", "")

    # Finally, write the processed text to the file.
    output_file.write(TEXT_EXTRACTED)
