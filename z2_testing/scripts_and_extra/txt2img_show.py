from PIL import Image
import sys
import numpy
import matplotlib.pyplot as plt

# funkcia na zobrazenie obrazku, ktory je ulozeny v TXT formate s rozsahom hodnot v intervale <0,1>
# txt_path - cesta k obrazku v TXT formate
def txt2img(txt_path: str):
	img = list()

	f = open(txt_path, 'r')
	for line in f.readlines():
		pixels = line.split(' ')
		for pixel in pixels:
			img.append(float(pixel)*255)
	f.close()

	img = numpy.reshape(img, (28,28))
	img = Image.fromarray(numpy.uint8(img), mode='L')
	arr = numpy.asarray(img)
	plt.imshow(arr, cmap='gray', vmin=0, vmax=255)
	plt.show()


# program sa ovlada z CMD
if len(sys.argv) != 2:
	print('Usage: python txt2img.py txt_path')
else:
	txt2img(sys.argv[1])

