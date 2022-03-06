'''
2022.03.06
Hosung.Kim
----------
숫자 아트 테스트 버전
'''

import cv2

'''
0
10676
2958
7718
0.2770700636942675
=======
1
10676
1807
8869
0.16925814911952042
=======
2
10676
1987
8689
0.18611839640314726
=======
3
10676
2118
8558
0.198388909704009
=======
4
10676
2268
8408
0.212439115773698
=======
5
10676
2098
8578
0.19651554889471712
=======
6
10676
2559
8117
0.2396965155488947
=======
7
10676
1574
9102
0.14743349569127015
=======
8
10676
2836
7840
0.26564256275758713
=======
9
10676
2543
8133
0.2381978269014612
'''

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
FILE_PATH = "D:\Project\_Python\\"
img = cv2.imread(FILE_PATH + 'emilico.jpg', cv2.IMREAD_GRAYSCALE)

imageWidth, imageHeight = img.shape
product = ""

for w in range(imageWidth) :
    for h in range(imageHeight) :
        product += f"{img[w, h]}, "
    product = product[:-2]
    product += "\n"

print(imageWidth, imageHeight)

f = open(FILE_PATH + "emp.txt", 'w', encoding='utf-8')
f.write(product)
f.close()
cv2.imshow('image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()