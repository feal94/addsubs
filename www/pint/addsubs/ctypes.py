#!/usr/bin/python 
import os
import sys 

class mencoder():
	
	def addsubs(self, video, subtitles,output,size,autoplay):
		if (! output): 
			output="new"+video
		if (! size): 
			os.system("mencoder -oac copy -ovc lavc -sub "+subtitles+" -utf8 -o "+output+" "+video)
		else: 
			os.system("mencoder -oac copy -ovc lavc -sub "+subtitles+" -subfont-text-scale "+size+" -utf8 -o "+output+" "+video)
		if autoplay = "yes": 
			self.play(output)
			
	def play(self,output):
		os.system("mplayer "+output)

video="/home/alvarofeal/Desktop/prueba.avi"
subtitles="/home/alvarofeal/Desktop/subtitles.srt"

os.system("mplayer /home/alvarofeal/Desktop/addsubs.avi")
