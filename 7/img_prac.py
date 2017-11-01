# -*- coding: utf-8 -*-

# image練習
# http://www.pythonchallenge.com/pc/def/oxygen.html

# PIL = Python Image Library
from PIL import Image


imgOxygen = Image.open('oxygen.png')
imgWidth, imgHeight = imgOxygen.size


# 白黒になる高さを調べる
y = 0
while True:
	col = imgOxygen.getpixel((0, y))
	if( col[0] == col[1] == col[2] ):
		break;
	y += 1

print('gray-scale pos(y):' + str(y))


# 白黒のマスの横方向に見て、色が変わったら文字へ変換
retChars = []
x = 0
colOld = -1
while x < imgWidth:
	col = imgOxygen.getpixel((x, y))
	if( col[0] == col[1] == col[2] ):
		# 灰色だったら、色をchrとして変換
		retChars.append(col[0])
	
	colOld = col[0]
	
	# 同じ色が続くこともあるので、幅分横へ動かす
	x += 7

# 文字列を出力
retStr = ''
for c in retChars:
	# print(chr(c))
	retStr += chr(c)

print(retStr)
#smart guy, you made it. the next level is [105, 110, 116, 101, 103, 114, 105, 116, 121]


# これをもう一度エンコードして・・・
chars2 = [105, 110, 116, 101, 103, 114, 105, 116, 121]
retStr = ''
for c in chars2:
	retStr += chr(c)

print(retStr)
#integrity