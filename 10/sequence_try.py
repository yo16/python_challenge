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

# �P�O�̗v�f���玟�̗v�f���v�Z����
while len(a) < lastN+1:
	print("---")
	# ������
	nextNum = 0
	sPrevNum = str(prevNum)
	print("sPrevNum:"+sPrevNum)
	sNextNum = ""
	
	# ���l���P�������o��
	# �P�����̐�����N�Ƃ���
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
			# �����ꍇ�̓J�E���g�A�b�v
			curCount += 1
		else:
			print("diff!:" + str(prevN) + ":" + str(curN) + ":")
			# �Ⴄ�ꍇ��nextNum�ɐݒ肷�镶���񂪌��܂�
			sNextNum += str(prevN) + str(curCount)
			#print("sNextNum:"+sNextNum)
			# �J�E���g��������
			curCount = 1
		
		# �O�̕�����ݒ�
		prevN = curN
	
	sNextNum += str(curN) + str(curCount)
	print("sNextNum:"+sNextNum)
	nextNum = int(sNextNum)
	
	# �z��֊i�[
	a.append(sNextNum)
	prevNum = nextNum




print("str is >" + a[lastN] + "<")
print("len is >>" + str(len(a[lastN])) + "<<")
