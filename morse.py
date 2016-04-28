#!/bin/python

from array import *
import sys

# change codes when using other input then . and -
# code space, if found will be used as a space. 
# also linebreak \n is used as a space. 
code_short	= '.' 
code_long	= '-'
code_space	= '/'
woorden		= ""
output		= ""


# first in array = 0!
morse = [code_short+code_long,code_long+code_short+code_short+code_short,code_long+code_short+code_long+code_short,code_long+code_short+code_short,code_short,code_short+code_short+code_long+code_short,code_long+code_long+code_short,code_short+code_short+code_short+code_short,code_short+code_short,code_short+code_long+code_long+code_long,code_long+code_short+code_long,code_short+code_long+code_short+code_short,code_long+code_long,code_long+code_short,code_long+code_long+code_long,code_short+code_long+code_long+code_short,code_long+code_long+code_short+code_long,code_short+code_long+code_short,code_short+code_short+code_short,code_long,code_short+code_short+code_long,code_short+code_short+code_short+code_long,code_short+code_long+code_long,code_long+code_short+code_short+code_long,code_long+code_short+code_long+code_long,code_long+code_long+code_short+code_short,code_long+code_long+code_long+code_long+code_long,code_short+code_long+code_long+code_long+code_long,code_short+code_short+code_long+code_long+code_long,code_short+code_short+code_short+code_long+code_long,code_short+code_short+code_short+code_short+code_long,code_short+code_short+code_short+code_short+code_short,code_long+code_short+code_short+code_short+code_short,code_long+code_long+code_short+code_short+code_short,code_long+code_long+code_long+code_short+code_short,code_long+code_long+code_long+code_long+code_short,code_long+code_long+code_short+code_short+code_long+code_long,'\n','  ']

codes = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z','0','1','2','3','4','5','6','7','8','9',',',' ','\n']

print
print "morse.py - roughly made script"
print 

if len(sys.argv) != 3:
	print "Usage: ./morse.py d(ecode)/e(ncode) file"
	exit()

if sys.argv[1]=='d': 
	print "---------------------decode---------------------"
	print "file: %s" % sys.argv[2]
	print
	tekst = [line.strip() for line in open(sys.argv[2], 'r')] #split morse lines
	for tekstregel in tekst: #split morse words
	 print tekstregel
	 woorden=str.split(tekstregel)
	 for woord in woorden: #split morse
	  output+=codes[morse.index(woord)]
	print
	print "decoded: "
	print
	print output

	
if sys.argv[1]=='e':
	print "---------------------Encode---------------------"
	print "file: %s" % sys.argv[2]
	print
	tekst = [line.strip() for line in open(sys.argv[2], 'r')] #split text
	for tekstregel in tekst:
	 # print tekstregel
	 tekstUpper = tekstregel.upper()
	 print tekstregel
	 i=0
	 while i < len(tekstUpper):
	  output+=morse[codes.index(tekstUpper[i])]+" "
	  i+=1
        print output
		
