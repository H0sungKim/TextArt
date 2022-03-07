'''
2022.03.06
Hosung.Kim
----------
TextArt Test Version
'''

import cv2

'''
space : 0
!
"
#
$
%
&
'
(
)
*
+
,
-
.
/
0 : 0.2770700636942675
1 : 0.16925814911952042
2 : 0.18611839640314726
3 : 0.198388909704009
4 : 0.212439115773698
5 : 0.19651554889471712
6 : 0.2396965155488947
7 : 0.14743349569127015
8 : 0.26564256275758713
9 : 0.2381978269014612
:
;
<
=
>
?
@
A
B
C
D
E
F
G
H
I
J
K
L
M
N
O
P
Q
R
S
T
U
V
W
X
Y
Z
[
\
]
^
_
`
a
b
c
d
e
f
g
h
i
j
k
l
m
n
o
p
q
r
s
t
u
v
w
x
y
z
{
|
}
~
'''

FILE_PATH = ""
image = cv2.imread(FILE_PATH + 'vincent.jpg', cv2.IMREAD_GRAYSCALE)

imageHeight, imageWidth = image.shape
product = ""

# for w in range(imageWidth) :
#     for h in range(imageHeight) :
#         product += f"{img[h, w]}, "
#     product = product[:-2]
#     product += "\n"

print(imageWidth, imageHeight)

size = 2
textPixelX = 68 // size
textPixelY = 157 // size

textCountX = imageWidth // textPixelX
textCountY = imageHeight // textPixelY

# textCountX = [textPixelX] * (imageWidth // textPixelX)
# textCountY = [textPixelY] * (imageHeight // textPixelY)
#
# imageWidth % textPixelX % len(textCountX)
#
# for i in range(len(textCountX)) :
#     textCountX[i] += imageWidth % textPixelX // len(textCountX)
# for i in range(len(textCountY)) :
#     textCountY[i] += imageHeight % textPixelY // len(textCountY)
#
# for i in range(imageWidth % textPixelX % len(textCountX)) :
#     textCountX[i] += 1
# for i in range(imageHeight % textPixelY % len(textCountY)) :
#     textCountY[i] += 1
# product += str(textCountX)
# product += "\n"
# product += str(textCountY)
# print(sum(textCountX), sum(textCountY))

processedImage = cv2.resize(image, (textCountX, textCountY))





f = open(FILE_PATH + "emp.txt", 'w', encoding='utf-8')
f.write(product)
f.close()
# cv2.imshow('image', image)
cv2.imshow('image', processedImage)
cv2.waitKey(0)
cv2.destroyAllWindows()