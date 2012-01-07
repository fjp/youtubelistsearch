#/usr/bin/python
# -*- coding: utf8 -*-

##################################################################
# Project Name: youtubelistsearch				#
# Author: Franz Pucher						#
# Email: franz.pucher@gmail.com					#
#								#
# Description:							#
# Opens multiple youtube chromium-browser-tabs searching	#
# for all line entries in a given text file (e.g. playlist.txt)	#
# The idea was a timesaving script that helps to find		#
# songs, stored in a text file, on the video platform youtube	#
# 								#
# Tested with Ubuntu 11.10, Chromium 15				#
#################################################################

import os
import urllib

path = raw_input("Enter path to playlist: ")
path = "/home/fjp/tmp/list" # comment this line out (just for testing)
print path

fopen = open(path, "r")


command = "chromium-browser http://www.youtube.com/results?search_query="

for line in fopen:
	posspace = line.find(" ")
	line = line[posspace+1:]	
	print(command+line)
	os.system(command+urllib.quote(line))

fopen.close()
