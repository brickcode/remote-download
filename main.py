#!python2.7/bin/python

import pycurl
import cStringIO
import sys
import threading
import sys

def toHex( number ):
	return '%02x' % number

def hit(number, name):
	buf = cStringIO.StringIO()
	hex_n = toHex(number)
	url = 'http://download.jw.org/files/media_books/' +  hex_n + "/" + name
	c = pycurl.Curl()
	c.setopt(c.URL, url)
	c.setopt(c.NOBODY, 1)
	c.setopt(c.HEADERFUNCTION, buf.write)
	c.perform()
	test = c.getinfo(c.RESPONSE_CODE)
	if(test == 200):
		print(url)
	c.close()
	return test

def search(name):
	T = []
	for number in range(255):
		t = threading.Thread(target=hit, args=([number, name]))
		T.append(t)
		t.daemon = True
		t.start()
	for t in T:
		t.join()

def list_download():
	prefix = "_P.mp3.zip"	
	F = open("list.txt","r")
	for line in F.readlines():
		s_line = line[:-2] + prefix
		search(s_line)

if __name__ == '__main__':
	search(sys.argv[1])
