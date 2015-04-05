# Jonathan Smith (c) 2015
# watermark.py

#Watermarks all images in a directory or just one with a message
#	given by the user 

import os
from PIL import Image, ImageDraw, ImageFont
trace = 1

all_files = raw_input('Watermark all JPEGs in directory? (y/n) ')
lst_files = []
if all_files == 'y':
	for file in os.listdir("./"):
		if file.endswith(".jpg"):
			lst_files.append(file)
else:
	img_name  = raw_input('What is the name of the file? ')
	lst_files.append(img_name)
if (trace): print lst_files

img_watermark = raw_input('What should the watermark be? ')

for x in lst_files:
	try:
		print "Trying to open ", x
		img = Image.open(x)

		#Change image name to reflect modification
		img_name_new = x.split('.')
		img_name_new[0] += '-edited'
		img_name_new = '.'.join(img_name_new)
		if (trace): print "New name: ", img_name_new
			
		#Define height and width of image to use for determining font size
		width = img.size[0]
		height = img.size[1]
		if (trace): print "Height: %d  Width: %d" %(height, width)

		#Determine font size (Only based on height for now)
		if (height > 4000):
			font_size = 120
		elif (height > 500):
			font_size = height/50
		else:
			font_size = height/10
		if (trace): print "Font Size: ", font_size

		font = ImageFont.truetype("Arial.ttf", font_size, encoding='unic')
		draw = ImageDraw.Draw(img)
		
		draw.text((0, 0), img_watermark, font=font)

		img.save(img_name_new)
		del img
	except:
		print("Couldn't find that file... sorry")

