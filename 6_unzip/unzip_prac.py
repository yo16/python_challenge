# -*- coding: utf-8 -*-

# unzip練習
# http://www.pythonchallenge.com/pc/def/channel.html

import os
import os.path
import zipfile
import re

fileName = 'channel'

# フォルダがなかったら作成してunzip
if not os.path.isdir(fileName) :
	os.mkdir(fileName)
	
	# unzip
	fZip = zipfile.ZipFile(fileName+'.zip', 'r')
	fZip.extractall(fileName)
	fZip.close


# zipを解凍した中に、readme.txtがあって
# それを読むと・・・
#welcome to my zipped list.
#
#hint1: start from 90052
#hint2: answer is inside the zip
# こう書いてある。
# インチキだけど、これを使う
nothing = 90052
listFileName = []

foundSomething = False
while not foundSomething:
	print(nothing)
	listFileName.append(nothing)
	
	fText = open(fileName + '/' + str(nothing) + '.txt')
	textLine = fText.read()
	fText.close()
	
	objMatch = re.search('Next nothing is ([0-9]+)', textLine)
	if objMatch:
		tupleMatch = objMatch.groups(1)
		nothing = tupleMatch[0]
	else:
		print('FOUND*' + textLine)
		foundSomething = True


#46145.txt
#Collect the comments.



print('--------------')

fZip = zipfile.ZipFile(fileName+'.zip', 'r')

strComments = ''
for l in listFileName:
	bComment = fZip.getinfo('%s.txt' % str(l)).comment
	print(bComment.decode('ascii'))
	strComments += bComment.decode('ascii')

fZip.close

print(strComments)
# ****************************************************************
# ****************************************************************
# **                                                            **
# **   OO    OO    XX      YYYY    GG    GG  EEEEEE NN      NN  **
# **   OO    OO  XXXXXX   YYYYYY   GG   GG   EEEEEE  NN    NN   **
# **   OO    OO XXX  XXX YYY   YY  GG GG     EE       NN  NN    **
# **   OOOOOOOO XX    XX YY        GGG       EEEEE     NNNN     **
# **   OOOOOOOO XX    XX YY        GGG       EEEEE      NN      **
# **   OO    OO XXX  XXX YYY   YY  GG GG     EE         NN      **
# **   OO    OO  XXXXXX   YYYYYY   GG   GG   EEEEEE     NN      **
# **   OO    OO    XX      YYYY    GG    GG  EEEEEE     NN      **
# **                                                            **
# ****************************************************************
#  **************************************************************

# hockey.htmlを見ると
# it's in the air. look at the letters.

# → oxygen.html
 