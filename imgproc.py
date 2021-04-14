# This Program was created to process multiple images stored in a directory at same time

import os, argparse
from PIL import Image, ImageFilter
parser = argparse.ArgumentParser(description="img: Image Processor // version 1.0")
parser.add_argument('-i','-input',help='Input Image File name',nargs='+',required=True)
parser.add_argument('-crop',help='Crop image based on LEFT, TOP, RIGHT, BOTTOM coordinates.',nargs=4)
parser.add_argument('-resize',help='Resize image to specified Width and Height.',nargs=2)
parser.add_argument('-blur',help='Blur the input image.',action='store_true')
parser.add_argument('-prefix',help='Add a user defined text before output file name (DEFAULT: img_).')
args = parser.parse_args()
proceed = True
files = []
filenames=[]
prefix = 'img_'
try:
    for file in args.i:
        files.append(Image.open(file))
        filenames.append(file)
except FileNotFoundError as error:
    proceed = False
    print(error)
if proceed:
    if args.blur:
        for index in range(0,len(files)):
            files[index]=files[index].filter(ImageFilter.BLUR)
    if not(args.crop is None):
        bounds=[]
        for i in range(0,len(args.crop)):
            bounds.append(int(args.crop[i]))
        for index in range(0,len(files)):
            files[index]=files[index].crop(bounds)
    if not(args.resize is None):
        for index in range(0,len(files)):
            files[index]=files[index].resize((int(args.resize[0]),int(args.resize[1])),Image.ANTIALIAS)
    if not(args.prefix is None):
        prefix = str(args.prefix)+'_'
if proceed:
    for index in range(0,len(files)):
        bname = prefix + os.path.basename(str(filenames[index]))
        dirname = os.path.dirname(os.path.abspath(str(filenames[index])))
        files[index].save(os.path.join(dirname,bname))
