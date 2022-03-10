import cv2
from PIL import Image, ImageDraw, ImageFont
from PyQt5.QtWidgets import QGridLayout, QLabel, QPushButton, QWidget, QApplication, QMainWindow
import sys

# ASCII_CODE = " !\"#$%&'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\]^_`abcdefghijklmnopqrstuvwxyz{|}~"
# font = ImageFont.truetype("D2Coding-Ver1.3.2-20180524-all.ttc", 50)
# f = open("emp.txt", 'w', encoding='utf-8')
#
# testString = "김 호성뷁ㅎㅗ"
#
# num = 0
# product = ""
# for i in testString :
#
#     image = Image.new('RGB', font.getsize(i), (255, 255, 255))
#     draw = ImageDraw.Draw(image)
#     product += i + " : " + str(font.getsize(i)) + "\n"
#     draw.text((0, 0), i, fill="black", font=font)
#     image.save(f'/Users/kihoon.kim/Hosung/data/photos/temp/test{num}.png')
#     num += 1
# #
# f.write(product)
# f.close()


# class MainWindow(QWidget) :
#     def __init(self) :
#         super().__init__()
#         self.filePath = ""
#         self.setAcceptDrops(True)
#         self.initUI()
#
#
#     def initUI(self) :
#         self.setWindowTitle('TextArt')
#         gridLayout = QGridLayout()
#         self.setLayout(gridLayout)
#
#         label = QLabel(self, "hi")
#         gridLayout.addWidget(label, 0, 0)
#
#         button = QPushButton("Edit", self)
#         gridLayout.addWidget(button, 1, 0)
#         button.clicked.connect(self.buttonClicked())
#
#         self.show()
#
#     def dropEvent(self, event) :
#         if event.mimeData().hasUrls():
#             event.accept()
#         else:
#             event.ignore()
#
#     def dropEvent(self, event):
#         files = [u.toLocalFile() for u in event.mimeData().urls()]
#         for f in files:
#             print(f)
#             self.inputLine.setText(f)
#             self.filePath = f
#
#     def buttonClicked(self) :
#         event = 0


# if __name__ == '__main__':
#    app = QApplication(sys.argv)
#    ex = MainWindow()
#    print("H")
#    sys.exit(app.exec_())

'''
pyqt5 drag and drop
사진 대비  https://deep-learning-study.tistory.com/121
pdf pyfpdf
'''

def isKorean(text) :
    korCount = 0
    for i in text :
        if (ord(i) >= ord("ㄱ") and ord(i) <= ord("ㅣ")) or (ord(i) >= ord("가") and ord(i) <= ord("힣")) :
            korCount += 1
    if korCount == 0 :
        return False
    elif korCount == len(text) :
        return True
    else :
        print("한글은 영어, 숫자, 특수기호와 함께 사용이 불가능합니다.")

FILE_PATH = ""
image = cv2.cvtColor(cv2.imread(FILE_PATH + 'mom.jpeg', cv2.IMREAD_COLOR), cv2.COLOR_BGR2RGB)
# image = cv2.imread(FILE_PATH + 'vincent.jpg', cv2.IMREAD_COLOR)

IMAGE_HEIGHT, IMAGE_WIDTH, IMAGE_CHANNEL = image.shape

text = "엄마사랑해요"
text = text.replace(" ", "")
lenText = len(text)

font = ImageFont.truetype("D2Coding-Ver1.3.2-20180524-all.ttc", 50)

STANDARD_TEXT_X, STANDARD_TEXT_Y = font.getsize(" ")
STANDARD_TEXT_Y = STANDARD_TEXT_X * 2

if isKorean(text) :
    STANDARD_TEXT_X = STANDARD_TEXT_X * 2

size = 4
TEXT_PIXEL_X = STANDARD_TEXT_X // size
TEXT_PIXEL_Y = STANDARD_TEXT_Y // size

TEXT_COUNT_X = IMAGE_WIDTH // TEXT_PIXEL_X
TEXT_COUNT_Y = IMAGE_HEIGHT // TEXT_PIXEL_Y

processedImage = cv2.resize(image, (TEXT_COUNT_X, TEXT_COUNT_Y))


print(f"{TEXT_COUNT_X}, {TEXT_COUNT_Y}")
print(f"{STANDARD_TEXT_X}, {STANDARD_TEXT_Y}")


image = Image.new('RGB', (TEXT_COUNT_X * STANDARD_TEXT_X, TEXT_COUNT_Y * STANDARD_TEXT_Y), (255, 255, 255))
draw = ImageDraw.Draw(image)

# #글씨 하나하나씩 그리기
for i in range(TEXT_COUNT_X) :
    for j in range(TEXT_COUNT_Y) :
        draw.text((STANDARD_TEXT_X * i, STANDARD_TEXT_Y * j), text[(TEXT_COUNT_X * j + i) % lenText], fill=tuple(processedImage[j][i]), font=font)

# draw.text((0, 0), "dd", fill=tuple(processedImage[][]), font=font)


image.save('test.png')
print("finished")
#
# cv2.imshow('image', processedImage)
# cv2.waitKey(0)
# cv2.destroyAllWindows()