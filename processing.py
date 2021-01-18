from PIL import Image
import pygame,sys,math
import pyautogui as pgui
import time

palette1 = [
    (155, 0, 0),
    (255, 165, 0),
    (0, 128, 0),
    (0, 0, 255),
    (108, 0, 108),
    (66, 45, 9),
    (102, 102, 102),
    (255, 0, 0),
    (255, 255, 0),
    (173, 216, 230),
    (255, 142, 210),
    (255, 226, 174),
    (204, 204, 204),
    (51, 51, 51),
    (225, 107, 0),
    (165, 255, 64),
    (40, 119, 215),
    (215, 0, 215),
    (94, 64, 13),
    (153, 153, 153),
    (0, 0, 0)
]

palette = [
    (3, 4, 94),
    (2, 62, 138),
    (0, 119, 182),
    (0, 150, 199),
    (0, 180, 216),
    (72, 202, 228),
    (144, 224, 239),
    (173, 232, 244),
    (202, 240, 248)
]

def rgb_diff(c1,c2):
    return ((c2[0]-c1[0])*0.3)**2+((c2[1]-c1[1])*0.59)**2+((c2[2]-c1[2])*0.11)**2

def find_closest(clr):

    best = rgb_diff(clr,palette[0])
    best_rgb = palette[0]

    for rgb in palette:
        if rgb_diff(rgb,clr) < best:
            best = rgb_diff(rgb,clr)
            best_rgb = rgb

    return best_rgb

def get_image(res):

    image = Image.open('image.png')
    size = width, height = image.size

    pixels = image.load()
    w,h = len(pixels), len(pixels[0])

    matrix = []

    for r in range(w):
        row = []
        for c in range(h):
            rgb = [0,0,0]
            cnt = 0

            for rr in range(r*int(w/res),(r+1)*int(w/res)):
                for cc in range(c*int(w/res),(c+1)*int(h/res)):
                    rgb = [a+b for a,b in zip(rgb,pixels[rr,cc])]
                    cnt+=1
            rgb = [min(int(a/cnt),255) for a in rgb]
            clr = find_closest(rgb)

            row.append(clr)
        matrix.append(row)

    return matrix

def get_dot_instructions(matrix):

    dictionary = {}

    for r in range(len(matrix)):
        for c in range(len(matrix[0])):
            if matrix[r][c] in dictionary:
                dictionary[matrix[r][c]].append((r*4+500,c*4+200))
            else:
                dictionary[matrix[r][c]] = [(r*4+500,c*4+200)]

    return dictionary


        

        
