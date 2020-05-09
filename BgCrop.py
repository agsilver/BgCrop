# -*- coding: utf-8 -*-
"""
Created on Fri May  8 17:53:43 2020

@author: user
"""

from PIL import Image, ImageChops

im = Image.open("test2.jpg")

w = im.size[0] - 1
h = im.size[1] - 1
bg = Image.new(im.mode, im.size, im.getpixel((w,h)))
diff = ImageChops.difference(bg, im)
diff = ImageChops.add(diff, diff, 2.0, -100)
bbox = diff.getbbox()
im = im.crop(bbox)
im.show()