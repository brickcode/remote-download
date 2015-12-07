#!python2.7/bin/python
#-*- coding: utf-8 -*-

import pycurl
import cStringIO
import sys
import threading
import sys

def toHex( number ):
	return '%02x' % number

def hit(number, name, typ):
	buf = cStringIO.StringIO()
	hex_n = toHex(number)
	url = 'http://'
	if(typ == 'M'):
		url += 'download.jw.org/files/media_magazines/'
	elif(typ == 'B'):
		url += 'download.jw.org/files/media_books/'
	url += hex_n + "/" + name
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

def search(name, typ):
	T = []
	for number in range(255 + 1):
		t = threading.Thread(target=hit, args=([number, name, typ]))
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

def magazines():
	m = ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12']
	lang = 'P_'
	prefix = '.pdf'
	year = sys.argv[1]
	typ = 'M'
	
	#year = '2015'
	for month in m:
		mobi = 'g_' + lang + year + month + prefix
		search(mobi, typ)
	for month in m:
		mobi = 'wp_' + lang + year + month + '01' + prefix
		search(mobi, typ)
	for month in m:
		mobi = 'w_' + lang + year + month + '15' + prefix
		search(mobi, typ)

def books():
	lang = '_P'
	prefix = '.mobi'
	typ = 'B'

	booklist = [
			'bh', # Czego naprawdę uczy Biblia
			'es14', # Codzienne badanie Pism 2014
			'es15', # Codzienne badanie Pism 2015
			'es16', # Codzienne badanie Pism 2016
			'hf', # Twoja rodzina może być szczęśliwa 
			'kr', # Królestwo Boże panuje
			'od', # Zorganizowani do spełniania woli Jehowy
			'sgd', # Pomoc do studium Słowa Bożego
			'igw', # Poznaj Słowo Boże
			'yb13', # Rocznik 2013
			'yb14', # Rocznik 2014
			'yb15', # Rocznik 2015
			'yb16', # Rocznik 2016
			'yc' # Ucz swoje dzieci
			]
	for mybook in booklist:
		book = mybook + lang + prefix
		search(book, typ)

	for mybook in booklist:
		book = mybook + lang + '.pdf'
		search(book, typ)

if __name__ == '__main__':
	#magazines()
	books()
