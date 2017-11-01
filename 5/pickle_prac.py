# -*- coding: utf-8 -*-

# pickle練習
# http://www.pythonchallenge.com/pc/def/peak.html
# banner.p
# 上記URLをブラウザで開いて、エディタへコピペすると
# 改行文字がcrlfになっているが、
# pickleのdumpファイルは改行文字はcr。
# だからコピペしたファイルは読めない。
# _pickle.UnpicklingError: the STRING opcode argument must be quoted

import pickle


fff = open('banner.p', 'rb')
# aaa = pickle.load(fff, fix_imports=True, encoding='bytes')
aaa = pickle.load(fff)
fff.close()


print(aaa)
# ２次的にスペースと#を並べるっぽい
print('--------------------')


# ファイル出力
f = open('out.txt', 'w')

cntRow = 0
for row in aaa:
	for col in aaa[cntRow]:
#		print(col)
		outStr = '>'
		for i in range(0,col[1]):
			f.write(col[0])
			outStr += col[0]
	f.write('x\n')
#		print(outStr)
	
	cntRow += 1

f.close()

