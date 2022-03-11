'''
=====================
2022.03.06
Hosung.Kim
---------------------
ASCIIArt Test Version
=====================
'''

import cv2
from PIL import Image, ImageDraw, ImageFont
import numpy as np
import json
from collections import OrderedDict

ASCII_CODE = " !\"#$%&'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\]^_`abcdefghijklmnopqrstuvwxyz{|}~"


denDict = OrderedDict()
with open("density.json", "r") as f:
    density = json.load(f)