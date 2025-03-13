from PIL import Image
import sys
import numpy
import os.path

# funkcia na konverziu obrazku cislice do TXT suboru
# image_path - cesta k obrazku
# output_folder - vystupny priecinok
#
# Pozn.: pixely budu normalizovane do rozsahu <0,1>
def img2txt(image_path: str, output_folder: str):
	with Image.open(image_path).convert('L') as im:
		data = numpy.asarray(im)
		data = data/255.0
		filename = os.path.basename(image_path)
		basename = os.path.splitext(filename)[0]
		output_path =  os.path.join(output_folder, basename + ".txt")
		numpy.savetxt(output_path, data, '%.2f')

# program sa ovlada z CMD
if len(sys.argv) != 3:
	print('Usage: python img2txt.py image_path output_folder')
else:
	img2txt(sys.argv[1], sys.argv[2])
