from pdf417gen import encode, render_image
import sys, argparse
import subprocess as sp

parser = argparse.ArgumentParser(description='this script can generate pdf 417 and Data Matrix barcodes')
parser.add_argument('TEXT', type=str, help='defines text that you going to encode')
parser.add_argument('-o','--output', type=str, required=True, help='defines output path + file. e.g: -o Dir/pic.jpg')
parser.add_argument('--p417', nargs='?', type=int, default=0, const=1, help= 'defines pdf417 generating')
parser.add_argument('--dmtx', nargs='?', type=int, default=0, const=1, help= 'defines Data Matrix generating')
args=parser.parse_args()
e = 0
if args.p417 == 1:
    if args.dmtx == 1:
        print("E:Choose only one p417 or dmtx")
        e = 1
if e == 0:
    if args.p417 == 1:
# Some data to encode
        text = args.TEXT

# Convert to code words
        codes = encode(text)

# Generate barcode as image
        image = render_image(codes)  # Pillow Image object
        image.save(args.output)
    if args.dmtx == 1:
        T=str(args.TEXT)
        O=str(args.output)
        res = ("echo '{}' | dmtxwrite -s s -o '{}'".format(T,O))
        print (str(res))
        sp.run(str(res), shell=True)
else:
    print("E:Script ended with error")