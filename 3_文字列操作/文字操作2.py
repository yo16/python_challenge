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
ans = ''
def checkLine(str):
	global ans
	c7 = ''
	c7 = ''
	c6 = ''
	c5 = ''
	c4 = ''
	c3 = ''
	c2 = ''
	c1 = ''
	c0 = ''
	
	# １つ前の文字を対象にチェックする
	for c in str:
		# １つずつ後ろへ送る
		c8 = c7
		c7 = c6
		c6 = c5
		c5 = c4
		c4 = c3
		c3 = c2
		c2 = c1
		c1 = c0
		c0 = c
		
		# UUULUUUの場合、表示
		c8index = isUpperCase(c8)
		c7index = isUpperCase(c7)
		c6index = isUpperCase(c6)
		c5index = isUpperCase(c5)
		c4index = isLowerCase(c4)
		c3index = isUpperCase(c3)
		c2index = isUpperCase(c2)
		c1index = isUpperCase(c1)
		c0index = isUpperCase(c0)
		if (c0index < 0) and (c1index >= 0) and (c2index >= 0) \
		and (c3index >= 0) and (c4index >= 0) and (c5index >= 0) \
		and (c6index >= 0) and (c7index >= 0) and (c8index < 0):
			ans += c4
			print(c8+c7+c6+c5+c4+c3+c2+c1+c0)
# --------------------------------------


# ======================================
# メイン処理
# ======================================

# ファイルを読んでチェック
f = open('text.txt', 'r')
for line in f:
	checkLine(line)
f.close

print('----')
print(ans)