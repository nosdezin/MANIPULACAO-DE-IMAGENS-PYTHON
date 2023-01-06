from PIL import Image, ImageFilter
import os
import numpy as np

INPUT_DIR = os.path.join('imagens')
OUTPUT_DIR = os.path.join('output')

def in_file(filename):
    return os.path.join(INPUT_DIR, filename)

def out_file(filename):
    return os.path.join(OUTPUT_DIR, filename)

def show_vertical(im1, im2):
    im = Image.fromarray(np.vstack((np.array(im1), np.array(im2))))
    im.show()
    return im

def show_horizontal(im1, im2):
    im = Image.fromarray(np.hstack((np.array(im1), np.array(im2))))
    im.show()
    return im