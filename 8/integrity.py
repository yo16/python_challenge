# -*- coding: utf-8 -*-

# integrity
# http://www.pythonchallenge.com/pc/def/integrity.html
# Where is the missing link?
# un: 'BZh91AY&SYA\xaf\x82\r\x00\x00\x01\x01\x80\x02\xc0\x02\x00 \x00!\x9ah3M\x07<]\xc9\x14\xe1BA\x06\xbe\x084'
# pw: 'BZh91AY&SY\x94$|\x0e\x00\x00\x00\x81\x00\x03$ \x00!\x9ah3M\x13<]\xc9\x14\xe1BBP\x91\xf08'

import bz2

un = b'BZh91AY&SYA\xaf\x82\r\x00\x00\x01\x01\x80\x02\xc0\x02\x00 \x00!\x9ah3M\x07<]\xc9\x14\xe1BA\x06\xbe\x084'
pw = b'BZh91AY&SY\x94$|\x0e\x00\x00\x00\x81\x00\x03$ \x00!\x9ah3M\x13<]\xc9\x14\xe1BBP\x91\xf08'

un2 = bz2.decompress(un)
pw2 = bz2.decompress(pw)

print(un2.decode('ascii') + '/' + pw2.decode('ascii'))
#huge/file

# fBz = bz2.BZ2File('un.txt','r')
# bzline = fBz.read()
# fBz.close()
#print(bzline)

# huge/file
