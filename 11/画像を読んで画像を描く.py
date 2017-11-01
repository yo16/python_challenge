# -*- coding: utf-8 -*-

# pythonchallenge lv11
# http://www.pythonchallenge.com/pc/return/5808.html
# 

from PIL import Image, ImageDraw


# 問題の画像
imgQ = Image.open("cave.jpg")
qWidth, qHeight = imgQ.size


# 解答の画像
canvas1 = Image.new("RGB", (qWidth, qHeight), "#ffffff")
pix1 = canvas1.load()	# create the pixel map
canvas2 = Image.new("RGB", (qWidth, qHeight), "#ffffff")
pix2 = canvas2.load()	# create the pixel map
canvas3 = Image.new("RGB", (qWidth, qHeight), "#ffffff")
pix3 = canvas3.load()	# create the pixel map
canvas4 = Image.new("RGB", (qWidth, qHeight), "#ffffff")
pix4 = canvas4.load()	# create the pixel map
canvas5 = Image.new("RGB", (qWidth, qHeight), "#ffffff")
pix5 = canvas5.load()	# create the pixel map



for i in range(0, qWidth):
	for j in range(0, qHeight):
		# 問題の画像のpixelを取得
		qRgb = imgQ.getpixel((i, j))
		aryRgb = (qRgb[0], qRgb[1], qRgb[2])
		
		if (i % 2 == 0) and (j % 2 == 0):
			# 偶数同士の場合
			pix1[i/2, j/2] = aryRgb
		elif (i % 2 == 1) and (j % 2 == 1):
			# 奇数同士
			pix2[(i+1)/2, (j+1)/2] = aryRgb
		elif (i%2 == 0) and (j%2 == 1):
			# 偶数 奇数
			pix3[i/2, (j+1)/2] = aryRgb
		else:
			# 奇数 偶数
			pix4[(i+1)/2, j/2] = aryRgb


canvas1.save("ans1.jpg")
canvas2.save("ans2.jpg")
# →どっちもぼんやり出る
# → evil

canvas3.save("ans3.jpg")
canvas4.save("ans4.jpg")
# →元の絵がはっきり出る

# マージするのが正解なのか？
# → めんどくさいからいいや