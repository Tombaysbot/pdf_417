from pdf417gen import encode, render_image
import sys

if len(sys.argv) == 1:
	print ("use '-h' to help")
else:

	if len(sys.argv) > 3:
		print ("too many arguments")
	else:

		if str(sys.argv[1]) == "-h":
			print ("""Script created by Tombays
arguments:
-h  help
positional arguments:
[TEXT TO ENCODE]
[OUTPUT FILE NAME.jpg/.png]

example:

python3 gen.py "Hello World" "barcode.jpg"
""")
		else:

# Some data to encode
			text = str(sys.argv[1])

# Convert to code words
			codes = encode(text)

# Generate barcode as image
			image = render_image(codes)  # Pillow Image object
			image.save(str(sys.argv[2]))
