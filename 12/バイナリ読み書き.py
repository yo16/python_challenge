# -*- coding: utf-8 -*-

# pythonchallenge lv12
# http://www.pythonchallenge.com/pc/return/evil.html
# 画像のevil1.jpgから推測して
# evil2.jpgってやると
# not jpg .gfxって書いてあるjpgが出る
# evil2.gfxってやるとバイナリファイルをdlできる。


# 出力するファイルを開く
outfilesH = {}
outfileNum = 5
exts = ('jpg', 'png', 'gif', 'png', 'jpg')
for i in range( outfileNum ):
	outfilesH[i] = open('outfile' + str(i) + '.' + exts[i], 'wb')


# 入力ファイル（バイナリ）を開いて読む
infileName = 'evil2.gfx'
infileH = open(infileName, 'rb')
gfx = infileH.read()


# バイナリファイルを開く
#for b in range(0, len(gfx)):	# １バイトずつのループ
#	# １バイトずつ出力してみる
#	print(gfx[b])
# ・・・
# 0
# 0
# 0
# 0
# 55
# 0
# 0
# 0
# 0
# 38
# 15
# 0
# 0
# 0
# 62
# 255
# 0
# 0
# 0
# 177
# 217
# → ５バイトずつ、何かあるみたいなので
#    ５つのファイルへ順番に出力する(deal)


for b in range( 0, len( gfx ), outfileNum ):	# インデックスの加算を+5にする
	for i in range( outfileNum ):
		outfilesH[i].write( gfx[b + i].to_bytes(1,'big') )


# ファイルを閉じる
infileH.close()
for i in range( outfileNum ):
	outfilesH[i].close()



# できたファイルを順番に
# 0:dis
# 1:pro
# 2:port
# 3:ional（途中から壊れている。IEだと結構見える。）
# 4:ityの打ち消し
#
# →disproportional