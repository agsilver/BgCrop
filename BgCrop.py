from PIL import Image, ImageChops
import os
import re

def imgCrop(img):
    w, h = img.size
    limit = 230
    ycrop = 0
    #get y coordinate
    for i in range(h-100):
        tenpx = [img.getpixel((500, pixel)) for pixel in range(i,i+10)]
        avgR = 0
        avgG = 0
        avgB = 0
        for px in tenpx:
            avgR += px[0]/10
            avgG += px[1]/10
            avgB += px[2]/10
        # avgRGB = (avgR, avgG, avgB)
        if (avgR < limit) and (avgG < limit) and (avgB < limit):
            ycrop = i+50
            break

    # get x coordinate
    for i in range(w-100):
        tenpx = [img.getpixel((pixel, 500)) for pixel in range(i,i+10)]
        avgR = 0
        avgG = 0
        avgB = 0
        for px in tenpx:
            avgR += px[0]/10
            avgG += px[1]/10
            avgB += px[2]/10
        # avgRGB = (avgR, avgG, avgB)
        if (avgR < limit) and (avgG < limit) and (avgB < limit):
            xcrop = i+10
            break

    # get w coordinate
    for i in range(w-100):
        tenpx = [img.getpixel((w-1-pixel, 500)) for pixel in range(i,i+10)]
        avgR = 0
        avgG = 0
        avgB = 0
        for px in tenpx:
            avgR += px[0]/10
            avgG += px[1]/10
            avgB += px[2]/10
        # avgRGB = (avgR, avgG, avgB)
        if (avgR < limit) and (avgG < limit) and (avgB < limit):
            wcrop = i+10
            break

    # get h coordinate
    for i in range(h-100):
        tenpx = [img.getpixel((500, h-1-pixel)) for pixel in range(i,i+10)]
        avgR = 0
        avgG = 0
        avgB = 0
        for px in tenpx:
            avgR += px[0]/10
            avgG += px[1]/10
            avgB += px[2]/10
        # avgRGB = (avgR, avgG, avgB)
        if (avgR < limit) and (avgG < limit) and (avgB < limit):
            hcrop = i+10
            break

    crp = img.crop((0+xcrop,0+ycrop,w-wcrop,h-hcrop))
    return crp

path = os.path.abspath(os.path.dirname((__file__)))
images = os.listdir(path+"\\Photos\\")
currImg = ''
for image in images:
    photo = path + "\\Photos\\" + image
    img = Image.open(photo)
    crpImg = imgCrop(img)
    crpImg.save(path + "\\Cropped\\" + re.sub(".jpg","",image) + "_crp.jpg")