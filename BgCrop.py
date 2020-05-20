from PIL import Image
import os
from sys import stdout
from timeit import default_timer as timer
import re
import PySimpleGUI as sg


def main_GUI():
    layout = [[sg.T('Choose an action:')],
    [sg.B("Crop Background")],
    [sg.B("Sort by direction")]]

    window = sg.Window('BgCrop V1.2', layout)
    event, values = window.read()
    window.close()
    return event, values


def bgcrop_GUI():
    layout = [[sg.T('Choose source and desination folders:')],
            [sg.T('Source:      '), sg.In(), sg.FolderBrowse()],
            [sg.T('Destination:'), sg.In(), sg.FolderBrowse()],
            [sg.Submit(),sg.Cancel()]]

    window = sg.Window('BgCrop V1.2', layout)
    event, values = window.read()
    window.close()
    return event, values


def isHorizonatl(cropped_img):
    width, height = cropped_img.size
    if width > height:
        return True
    else:
        return False


def imgCrop(img):
    w, h = img.size
    limit = 230
    overshoot = 20
    

    # get x coordinate
    for i in range(w-100):
        tenpx = [img.getpixel((pixel, 500)) for pixel in range(i,i+10)]
        avgR, avgG, avgB = 0, 0, 0
        for px in tenpx:
            avgR += px[0]/10
            avgG += px[1]/10
            avgB += px[2]/10
        if (avgR < limit) and (avgG < limit) and (avgB < limit):
            xcrop = i+overshoot
            break

    #get y coordinate
    for i in range(h-100):
        tenpx = [img.getpixel((500, pixel)) for pixel in range(i,i+10)]
        avgR, avgG, avgB = 0, 0, 0
        for px in tenpx:
            avgR += px[0]/10
            avgG += px[1]/10
            avgB += px[2]/10
        if (avgR < limit) and (avgG < limit) and (avgB < limit):
            ycrop = i+overshoot+30
            break

    # get w coordinate
    for i in range(w-100):
        tenpx = [img.getpixel((w-1-pixel, 500)) for pixel in range(i,i+10)]
        avgR, avgG, avgB = 0, 0, 0
        for px in tenpx:
            avgR += px[0]/10
            avgG += px[1]/10
            avgB += px[2]/10
        if (avgR < limit) and (avgG < limit) and (avgB < limit):
            wcrop = i+overshoot
            break

    # get h coordinate
    for i in range(h-100):
        tenpx = [img.getpixel((500, h-1-pixel)) for pixel in range(i,i+10)]
        avgR, avgG, avgB = 0, 0, 0
        for px in tenpx:
            avgR += px[0]/10
            avgG += px[1]/10
            avgB += px[2]/10
        if (avgR < limit) and (avgG < limit) and (avgB < limit):
            hcrop = i+overshoot
            break

    crp = img.crop((xcrop,ycrop,w-wcrop,h-hcrop))
    return crp


def main():
    event, values = main_GUI() # open GUI
    images = os.listdir(values[0]) 
    for image in images:
        photo = values[0] + "\\" + image 
        img = Image.open(photo)
        crpImg = imgCrop(img)
        Hdir = values[1] + "\\" + "Horizontal"
        Vdir = values[1] + "\\" + "Vertical"
        if isHorizonatl(crpImg):
            newpath =  Hdir
        else:
            newpath = Vdir
        if not os.path.exists(newpath): # check if the user already has the folders
            os.makedirs(newpath) # if not, create them
        crpImg.save(newpath + "\\" + re.sub(".jpg","",image) + "_crp.jpg")


if __name__ == "__main__":
    main()
