# pdf_417
This is a short script for generating pdf417 barcodes.

arguments:
-h  help

positional arguments:
[TEXT TO ENCODE]

optional arguments:
-o --output
type of barcode --p417 or --dmtx

example:

python3 gen.py "Hello World" -o "barcode.jpg" --dmtx

to encode data matrix you should have a libdmtx0b or libdmtx0a (based on your distro, for kali i use libdmtx0b); and libdmtx-dev

sudo apt-get install libdmtx0b

sudo apt-get install libdmtx-dev
