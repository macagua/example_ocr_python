# OCR since pdf files

This program for extract text using OCR (Optical Character Recognition) technique since pdf files.

## Install

```console
sudo apt-get update
sudo apt-get install build-essential libpoppler-cpp-dev pkg-config python3-dev
sudo apt install tesseract-ocr
virtualenv venv
source venv/bin/activate
pip install -U pip
pip install -r requirements/pdfs.txt
cd pdfs
```

## Run Exmaples

### Extract text

```console
python extract_text.py
```
