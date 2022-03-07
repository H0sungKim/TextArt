import cv2

# ASCII_CODE = " !\"#$%&'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\]^_`abcdefghijklmnopqrstuvwxyz{|}~"
# font = ImageFont.truetype("D2Coding-Ver1.3.2-20180524-all.ttc", 50)
# f = open("emp.txt", 'w', encoding='utf-8')
#
# num = 0
# product = ""
# for i in ASCII_CODE :
#
#     image = Image.new('RGB', font.getsize(i), (255, 255, 255))
#     draw = ImageDraw.Draw(image)
#     product += i + " : " + str(font.getsize(i)) + "\n"
#     draw.text((0, 0), i, fill="black", font=font)
#     image.save(f'/Users/kihoon.kim/Hosung/data/photos/temp/{num}.png')
#     num += 1
#
# f.write(product)
# f.close()


FILE_PATH = ""
# image = cv2.cvtColor(cv2.imread(FILE_PATH + 'vincent.jpg', cv2.IMREAD_COLOR), cv2.COLOR_BGR2RGB)
image = cv2.imread(FILE_PATH + 'vincent.jpg', cv2.IMREAD_COLOR)

imageHeight, imageWidth, imageChannel = image.shape

processedImage = cv2.resize(image, ('''write x, y here'''))

cv2.imshow('image', processedImage)
cv2.waitKey(0)
cv2.destroyAllWindows()

text = "Hosung.Kim"
