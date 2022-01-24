#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan 21 22:19:22 2022

@author: yusa
"""

import matplotlib.pyplot as plt

def put_pixels(filename : str, x_offset : int, y_offset : int) -> str:
    
    img = plt.imread(filename)
    
    pixels = []
    
    y = y_offset
    for line in img:
        x = x_offset
        for pix in line:
            if len(pix) == 4:
                pixels.append((x, y, ( (int(pix[3]*255)<<24) + (int(pix[2]*255)<<16) + (int(pix[1]*255)<<8) + (int(pix[0]*255)<<0) )))
            else:
                pixels.append((x, y, ( (int(255)<<24) + (int(pix[2]*255)<<16) + (int(pix[1]*255)<<8) + (int(pix[0]*255)<<0) )))
            x += 1
        y += 1

    raw_pixels = []
    for pixel in pixels:
        raw_pixels.append(str((pixel[0]<<16) + (pixel[1]<<0) + (pixel[2]<<32)))
    
    pixstr = "["
    for raw_pixel in raw_pixels:
        pixstr += '"' + raw_pixel + '", '
    pixstr = pixstr[:-2] + "]"

    return pixstr

# Generate pixel string from PNG
pixstr = put_pixels("XCAD.png", 10, 80)

print(pixstr)


