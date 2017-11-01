# -*- coding: utf-8 -*-

# 文字操作
# http://www.pythonchallenge.com/pc/def/equality.html
# One small letter, surrounded by EXACTLY three big bodyguards on each of its sides.

abcU = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
def isUpperCase(c):
	if len(c) == 0:
		return -1
	return abcU.find(c)

abcL = 'abcdefghijklmnopqrstuvwxyz'
def isLowerCase(c):
	if len(c) == 0:
		return -1
	return abcL.find(c)


# --------------------------------------
# １行ごとにチェックする
# 小文字で、左右が大文字の文字の場合は、その文字を記憶する。
# 記憶方法は２次元配列。
# １次元目は、囲まれている文字のindex、
# ２次元目は、囲んでいる文字のindex
aSurrounded = [[0 for i in range(26)] for j in range(26)]
def checkLine(str):
	# ２つ前の文字
	c2 = ''
	# １つ前の文字
	c1 = ''
	# 今の文字
	c0 = ''
	
	# １つ前の文字を対象にチェックする
	for c in str:
		# １つずつ後ろへ送る
		c2 = c1
		c1 = c0
		c0 = c
		
		# c2、c0が大文字かつ、c1が小文字の場合、フラグを立てる
		c2index = isUpperCase(c2)
		c1index = isLowerCase(c1)
		c0index = isUpperCase(c0)
		if (c2index >= 0) and (c1index >= 0) and (c0index >= 0):
			aSurrounded[c1index][c2index] = 1
			aSurrounded[c1index][c0index] = 1
#			if c1index == 25:
#				print(c2+c1+c0)
# --------------------------------------


# ======================================
# メイン処理
# ======================================

# ファイルを読んで、2次元配列へ格納
f = open('text.txt', 'r')
for line in f:
	checkLine(line)
f.close

# ３つしかフラグが立っていない小文字を探す
for cL in range(26):
	upperCount = 0
	for cU in range(26):
		if aSurrounded[cL][cU] == 1:
			upperCount += 1
	if upperCount == 3:
		print(' ' + abcU[cL] + '*')
		# もう一度探す
		aryL = []
		for cU in range(26):
			if aSurrounded[cL][cU] == 1:
				aryL.append(cU)
				print(abcU[cU:cU+1] + ':' + abcL[cL[0]:cL[0]+1] + abcL[cL[1]:cL[1]+1] + abcL[cL[2]:cL[2]+1])
			else:
				print(abcU[cU:cU+1] + ':' + str(upperCount))
	else:
		print(abcU[cL] + ':' + str(upperCount))

print('--- end ---')
# なぜか全部26になっちゃう・・・

# → ま・ち・が・え・た！！
# UUULUUUな、Lを探せってことかーーーー
# ULUのUが３種類だと思ってた。
