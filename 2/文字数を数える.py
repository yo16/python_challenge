# -*- coding: utf-8 -*-

# 文字数を数える
# http://www.pythonchallenge.com/pc/def/ocr.html


# --------------------------------------
# ハッシュにカウントアップ
hCharCount = {}
aChars = []
def countUpThisChar(c):
	if c in hCharCount:
		hCharCount[c] = hCharCount[c] + 1
	else:
		hCharCount[c] = 1
		aChars.append(c)
# --------------------------------------

# --------------------------------------
# ハッシュに、１文字ごと件数を持つ
def countChar(str):
	# １文字ごとに分ける
	for c in str:
		countUpThisChar(c)
# --------------------------------------


# ======================================
# メイン処理
# ======================================

f = open('text.txt', 'r')

for line in f:
	countChar(line)

f.close

#for hk in hCharCount.keys():
for hk in aChars:
	print(hk + ':' + str(hCharCount[hk]))

