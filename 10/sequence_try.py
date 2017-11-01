# -*- coding: utf-8 -*-
import os
# pythonchallenge 10
# 2016/1/4
#
#a = [1, 11, 21, 1211, 111221, 
#len(a[30]) =?

prevNum = 1
a = [prevNum]

lastN = 30

# １つ前の要素から次の要素を計算する
while len(a) < lastN+1:
	print("---")
	# 初期化
	nextNum = 0
	sPrevNum = str(prevNum)
	print("sPrevNum:"+sPrevNum)
	sNextNum = ""
	
	# 数値を１桁ずつ取り出す
	# １文字の数字はNとする
	curN = int(sPrevNum[:1])
	prevN = curN
	print("curN:" + str(curN))
	curCount = 1
	for i in range(1,len(sPrevNum)):
		print("loop:"+str(i))
		
		curN = int(sPrevNum[i:i+1])
		print("curN:" + str(curN))
		if prevN == curN:
			print("same!:" + str(prevN))
			# 同じ場合はカウントアップ
			curCount += 1
		else:
			print("diff!:" + str(prevN) + ":" + str(curN) + ":")
			# 違う場合はnextNumに設定する文字列が決まる
			sNextNum += str(prevN) + str(curCount)
			#print("sNextNum:"+sNextNum)
			# カウントを初期化
			curCount = 1
		
		# 前の文字を設定
		prevN = curN
	
	sNextNum += str(curN) + str(curCount)
	print("sNextNum:"+sNextNum)
	nextNum = int(sNextNum)
	
	# 配列へ格納
	a.append(sNextNum)
	prevNum = nextNum




print("str is >" + a[lastN] + "<")
print("len is >>" + str(len(a[lastN])) + "<<")
