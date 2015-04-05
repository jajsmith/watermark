# Jonathan Smith (c) 2015
# watermark.py

#Watermarks all images in a directory or just one with a message
#	given by the user 

import sys, os
from PIL import Image, ImageDraw, ImageFont
trace = 0

img_name  = raw_input('What is the name of the file? ')

try:
	img = Image.open(img_name)

	#Change image name to reflect modification
	img_name_new = img_name.split('.')
	img_name_new[0] += '-edited'
	img_name_new = '.'.join(img_name_new)
	if (trace): print "New name: ", img_name_new
		
	#Define height and width of image to use for determining font size
	try:
		width = img.size[0]
		height = img.size[1]
		if (trace): print "Height: %d  Width: %d" %(height, width)
	except:
		print "Couldn't do size"

	#Determine font size (Only based on height for now)
	if (height > 4000):
		font_size = 60
	else:
		font_size = height/80
	if (trace): print "Font Size: ", font_size

	font = ImageFont.truetype("Arial.ttf", font_size, encoding='unic')
	draw = ImageDraw.Draw(img)
	
	img_watermark = raw_input('What should the watermark be? ')
	draw.text((0, 0), img_watermark, font=font)

	img.save(img_name_new)
except:
	print("Couldn't find that file... sorry")

