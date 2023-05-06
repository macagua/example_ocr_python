"""Program for extract text using OCR (Optical Character Recognition)
technique since pdf files

Source:
    https://www.geeksforgeeks.org/python-reading-contents-of-pdf-using-ocr-optical-character-recognition/
"""

import os
from tempfile import TemporaryDirectory

from pdf2image import convert_from_path
from PIL import Image
from pytesseract import image_to_string

# Path of the Input pdf
DATA_PATH = os.path.dirname(os.path.abspath(__file__)) +\
    os.sep + "data" + os.sep
FILE_NAME = "invoice_parts"
PDF_FILE = DATA_PATH + f"{FILE_NAME}.pdf"
TEXT_FILE = DATA_PATH + f"{FILE_NAME}.txt"

# Store all the pages of the PDF in a variable
image_file_list = []

# Read in the PDF file at 500 DPI
pdf_pages = convert_from_path(PDF_FILE, 500)

# Create a temporary directory to hold our temporary images.
with TemporaryDirectory() as temp_dir:
    # Part 1 - START : Converting PDF to images
    # Iterate through all the pages stored above
    for page_enumeration, page in enumerate(pdf_pages, start=1):
        # enumerate() "counts" the pages for us.

        # Create a file name to store the image
        file_name = f"{temp_dir}\\page_{page_enumeration:03}.jpg"

        # Save the image of the page in system
        page.save(file_name, "JPEG")
        image_file_list.append(file_name)
    # Part 1 - END

    # Part 2 - START: Recognizing text from the images using OCR
    # Open the file in append mode so that
    # All contents of all images are added to the same file
    with open(TEXT_FILE, "a", encoding="utf-8") as output_file:
        # Iterate from 1 to total number of pages
        for image_file in image_file_list:
            # Recognize the text as string in image using pytesserct
            TEXT_EXTRACTED = str(((image_to_string(Image.open(image_file)))))

            # To remove this, we replace every '-\n' to ''.
            TEXT_EXTRACTED = TEXT_EXTRACTED.replace("-\n", "")

            # Finally, write the processed text to the file.
            output_file.write(TEXT_EXTRACTED)
    # Part 2 - END
