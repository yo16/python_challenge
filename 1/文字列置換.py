# -*- coding: utf-8 -*-

# 文字列置換
# http://www.pythonchallenge.com/pc/def/map.html
# 全部の文字を２つ進める。
originalStr = 'g fmnc wms bgblr rpylqjyrc gr zw fylb. \
rfyrq ufyr amknsrcpq ypc dmp. \
bmgle gr gl zw fylb gq glcddgagclr ylb rfyr\'q ufw rfgq rcvr gq qm jmle. \
sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj.'

originalStr = 'http://www.pythonchallenge.com/pc/def/map.html'

abc = 'abcdefghijklmnopqrstuvwxyzabc'

hintStr = ''
for c1 in originalStr:
	abcIndex = 0
	found = 0
	for c2 in abc:
		if c1 == c2:
			hintStr = hintStr + abc[abcIndex+2:abcIndex+3]
			found = 1
			break
		abcIndex = abcIndex + 1
	if found == 0:
		hintStr = hintStr + c1

print(hintStr)
