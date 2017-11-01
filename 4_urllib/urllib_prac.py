# -*- coding: utf-8 -*-

# urllib練習
# http://www.pythonchallenge.com/pc/def/linkedlist.php
# urllib may help. DON'T TRY ALL NOTHINGS, since it will never 
# end. 400 times is more than enough.
# linkedlist.php?nothing=12345

import urllib.request as req
import re

proxy = req.ProxyHandler({'http' : 'http://proxy.unisys.co.jp:8080'})
auth = req.HTTPBasicAuthHandler()
opener = req.build_opener(proxy, auth, req.HTTPHandler)
req.install_opener(opener)
urlBase = 'http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing='

# 繰り返し！
nextVal = '12345'
nextVal = '8022'
for i in range(0, 200):
	conn = req.urlopen(urlBase + nextVal)
	str0 = conn.read()
	str0 = str0.decode('utf-8')
	
	m = re.search("and the next nothing is ([0-9]+)", str0)
	if not m:
		print(str0)
		break;
	
	tupl1 = m.groups(1)
	str1 = tupl1[0]
	print(str(i) + ':' + nextVal + '->' + str1 + '  ' + str0);
	
	nextVal = str1
	conn.close()

print('end')

