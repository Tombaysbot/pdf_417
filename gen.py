from pdf417gen import encode, render_image
import sys, argparse

parser = argparse.ArgumentParser(description='this script can make pdf 417 barcodes')
parser.add_argument('TEXT', type=str, help='defines text that you going to encode')
parser.add_argument('-o','--output', type=str, required=True, help='defines output path + file. e.g: -o Dir/pic.jpg')
args=parser.parse_args()
# Some data to encode
text = args.TEXT

# Convert to code words
codes = encode(text)

# Generate barcode as image
image = render_image(codes)  # Pillow Image object
image.save(args.output)