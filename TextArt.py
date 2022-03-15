'''
Copyright (c) 2022 by Hosung.Kim <hyongak516@mail.hongik.ac.kr>
=====================
2022.03.06
Hosung.Kim
---------------------
TextArt Version 1.0.1
---------------------
Issues

* 배경이 흰색이라 사진이 전체적으로 뿌옇게 나옴
=====================
'''

import cv2
import Util
from PIL import Image, ImageDraw, ImageFont
import numpy as np


FILE_PATH = input("Enter the path to the image which you want to convert to TextArt.\n=> ")
IMAGE_NAME = input("Enter the name of the image which you want to convert to TextArt.\n=> ")
image = cv2.cvtColor(cv2.imread(FILE_PATH + IMAGE_NAME, cv2.IMREAD_COLOR), cv2.COLOR_BGR2RGB)

IMAGE_HEIGHT, IMAGE_WIDTH, IMAGE_CHANNEL = image.shape

text = input("Enter the text to be a base of TextArt.\n=> ")
text = text.replace(" ", "")
lenText = len(text)

# font = ImageFont.truetype("D2Coding-Ver1.3.2-20180524-all.ttc", 50)
font = ImageFont.truetype("CONSOLAB.TTF", 50)

STANDARD_TEXT_X, STANDARD_TEXT_Y = font.getsize(" ")
STANDARD_TEXT_Y = STANDARD_TEXT_X * 2

# 한글은 영어와 한글자당 크기가 다르므로 확인 후 계산
if Util.isKorean(text) :
    STANDARD_TEXT_X = STANDARD_TEXT_X * 2

# 사진 리사이징
size = int(input("Enter the size of the TextArt you want. (1~10 will be suitable.)\n=> "))
TEXT_PIXEL_X = STANDARD_TEXT_X // size
TEXT_PIXEL_Y = STANDARD_TEXT_Y // size

TEXT_COUNT_X = IMAGE_WIDTH // TEXT_PIXEL_X
TEXT_COUNT_Y = IMAGE_HEIGHT // TEXT_PIXEL_Y

resizedImage = cv2.resize(image, (TEXT_COUNT_X, TEXT_COUNT_Y))

# 명도 조절
brightness = 30
brightnessAry = np.full(resizedImage.shape, (brightness, brightness, brightness), dtype=np.uint8)
processedImage = cv2.subtract(resizedImage, brightnessAry)

# 이미지 생성
image = Image.new('RGB', (TEXT_COUNT_X * STANDARD_TEXT_X, TEXT_COUNT_Y * STANDARD_TEXT_Y), (255, 255, 255))
draw = ImageDraw.Draw(image)

IMAGE_NAME = input("Enter the name you want the TextArt to be saved under.\n=> ")

# 글씨 하나하나씩 그리기
progress = 0
for i in range(TEXT_COUNT_X) :
    for j in range(TEXT_COUNT_Y) :
        progress += 1
        draw.text((STANDARD_TEXT_X * i, STANDARD_TEXT_Y * j), text[(TEXT_COUNT_X * j + i) % lenText], fill=tuple(processedImage[j][i]), font=font)
        Util.printProgressBar(progress, TEXT_COUNT_X * TEXT_COUNT_Y)

image.save(f'{IMAGE_NAME}.png')
print("\033[97m\nTextArt is created successfully.")