'''
Copyright (c) 2022 by Hosung.Kim <hyongak516@mail.hongik.ac.kr>
=====================
2022.03.06
Hosung.Kim
---------------------
ASCIIArt Version 1.0.0
---------------------
Issues

* 명암 대비 조절 (표준편차 이용)
=====================
'''

import cv2
import Util
from PIL import Image, ImageDraw, ImageFont
import numpy as np

# ASCII_CODE = " !\"#$%&'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\]^_`abcdefghijklmnopqrstuvwxyz{|}~"
# density = [0, 17, 27, 27, 29, 44, 47, 48, 52, 56, 62, 71, 73, 74, 76, 76, 82, 86, 88, 88, 94, 96, 98, 99, 102, 104, 104, 106, 109, 112, 114, 114, 115, 115, 116, 116, 116, 117, 117, 118, 118, 119, 120, 120, 122, 124, 127, 127, 128, 131, 134, 135, 136, 136, 137, 141, 141, 143, 144, 144, 146, 147, 148, 150, 150, 151, 153, 156, 158, 160, 160, 161, 162, 163, 163, 163, 164, 164, 165, 168, 172, 172, 173, 175, 177, 181, 181, 187, 189, 189, 190, 190, 196, 208, 255]

# 흑백픽셀 0~255 ASCII로 변환한 것
ASCII_CODE_PAINT = "@@@@@@@@@@@@@@@@@@@@@@@@QQQQQQQQQQQQQQQQQQQQQQQQQQQQQQ&&&&&&&&&00$NNBBBBWWMMM888DDOGGR%%%HH9#d6AKmmUUXXXS4hwPVZEkky55oa32jjeeeCCnuIIIfx]1FtzlJ7iivvvTTT()cc??LL||rrrr\\\\//***+++++<<>>=!!;;;;;~~~~~~~~^^^^^\"\"\"\",,::_________---------...'''`````````````         "

FILE_PATH = input("Enter the path to the image which you want to convert to ASCIIArt.\n=> ")
IMAGE_NAME = input("Enter the name of the image which you want to convert to ASCIIArt.\n=> ")
image = cv2.imread(FILE_PATH + IMAGE_NAME, cv2.IMREAD_GRAYSCALE)

IMAGE_HEIGHT, IMAGE_WIDTH = image.shape

font = ImageFont.truetype("CONSOLAB.TTF", 50)

STANDARD_TEXT_X, STANDARD_TEXT_Y = font.getsize(" ")
STANDARD_TEXT_Y = STANDARD_TEXT_X * 2

# 사진 리사이징
size = int(input("Enter the size of the TextArt you want. (1~10 will be suitable.)\n=> "))
TEXT_PIXEL_X = STANDARD_TEXT_X // size
TEXT_PIXEL_Y = STANDARD_TEXT_Y // size

TEXT_COUNT_X = IMAGE_WIDTH // TEXT_PIXEL_X
TEXT_COUNT_Y = IMAGE_HEIGHT // TEXT_PIXEL_Y

resizedImage = cv2.resize(image, (TEXT_COUNT_X, TEXT_COUNT_Y))

# 이미지 생성
image = Image.new('RGB', (TEXT_COUNT_X * STANDARD_TEXT_X, TEXT_COUNT_Y * STANDARD_TEXT_Y), (255, 255, 255))
draw = ImageDraw.Draw(image)

IMAGE_NAME = input("Enter the name you want the ASCIIArt to be saved under.\n=> ")

# 글씨 하나하나씩 그리기
progress = 0
text = ""
for j in range(TEXT_COUNT_Y) :
    for i in range(TEXT_COUNT_X) :
        progress += 1
        draw.text((STANDARD_TEXT_X * i, STANDARD_TEXT_Y * j), ASCII_CODE_PAINT[resizedImage[j][i]], fill=(0, 0, 0), font=font)
        text += ASCII_CODE_PAINT[resizedImage[j][i]]
        Util.printProgressBar(progress, TEXT_COUNT_X * TEXT_COUNT_Y)
    text += "\n"

image.save(f'{FILE_PATH}{IMAGE_NAME}.png')
f = open(f'{FILE_PATH}{IMAGE_NAME}.txt', 'w')
f.write(text)
f.close()
Util.printFinishMessage("ASCIIArt")
print(f"\033[97mASCIIArt is created successfully in the directory below.\n{FILE_PATH}{IMAGE_NAME}.png\n{FILE_PATH}{IMAGE_NAME}.txt")