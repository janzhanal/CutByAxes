#!/usr/bin/python

import sys, getopt
from PIL import Image

#potreba dopsat zakladni help, mozna i dodelat cestu, kam se nasklada narezany obrazek
#pouziti: python3 crop.py cesta_k_obrazku cesta_k_template
#template: obsahuje pomerne vzdalenosti na osach, nadefinuji si sami

def main():
    tiff = sys.argv[1]
    templates = sys.argv[2]
    opened_tiff = Image.open(tiff)
    width, height = opened_tiff.size
    templ = (get_template(templates))
    crop(tiff, width, height, templ, transfer(width,height,templ)[0], transfer(width,height,templ)[1] )

"""
Get axes settings from loaded template
"""
def get_template (template_paths):
    axes = []
    i=0
    with open(template_paths) as file:
        for line in file:
            axes.insert(i,line.split())
            i += 1
    return axes

"""
Crop one box from whole image
"""
def crop (tiff_path, im_width, im_height, templ, x_unit, y_unit):
    print (im_width, im_height) #debug
    top = 0
    left = 0
    opened_image = Image.open(tiff_path)
    for stepx in templ[0]:
        right = stepx
        top = 0
        for stepy in templ[1]:
            bottom = stepy
            testovaci = opened_image.crop((int(left)*x_unit, int(top)*y_unit, int(right)*x_unit-1, int(bottom)*y_unit))
            obr = (tiff_path, right, "x", bottom, ".jpg")
            name = ("".join(obr))
            #print ("left=",int(left)*x_unit,"top=", int(top)*y_unit,"right=", int(right)*x_unit-1,"bottom=", int(bottom)*y_unit)
            testovaci = testovaci.save(str(name))
            
            top = stepy
        left = stepx
        
        
    return

"""
Get main unit (image size / template size)
"""
def transfer (im_width,im_height,templ):
    x_size = len(templ[0])
    y_size = len(templ[1])
    x_unit = im_width // int(templ[0][x_size-1])
    y_unit = im_height // int(templ[1][y_size-1])
    return (x_unit, y_unit)

if __name__ == "__main__":
   main()