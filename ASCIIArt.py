'''
=====================
2022.03.06
Hosung.Kim
---------------------
ASCIIArt Test Version
---------------------
Issues

정확히 안 맞아떨어지는 색값에 대해서 어떻게 할지
=====================
'''

import cv2
from PIL import Image, ImageDraw, ImageFont
import numpy as np
import json
from collections import OrderedDict

ASCII_CODE = " !\"#$%&'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\]^_`abcdefghijklmnopqrstuvwxyz{|}~"



denDict = OrderedDict()
with open("density2.json", "r") as f:
    density = json.load(f)


print(density)