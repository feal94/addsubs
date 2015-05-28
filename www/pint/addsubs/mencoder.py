#!/usr/bin/python 
import os
import sys 

class Mencoder():
	
	def addsubs(self, video, subtitles,font,delay,add,size,autoplay):
		output="new"+video
		if add="No":
			return None
		if (size is None):
			if (font is None): 
				if (delay is None):  
					os.system("mencoder -oac copy -ovc lavc -sub "+subtitles+" -utf8 -o "+output+" "+video)
				else: 
					os.system("mencoder -oac copy -ovc lavc -sub "+subtitles+" -delay "+delay+" -utf8 -o "+output+" "+video)
			else: 
				if (delay is None):  
					os.system("mencoder -oac copy -ovc lavc -sub "+subtitles+" -font "+font+" -utf8 -o "+output+" "+video)
				else: 
					os.system("mencoder -oac copy -ovc lavc -sub "+subtitles+" -font "+font+" -delay "+delay+" -utf8 -o "+output+" "+video)
		else 
			if (font is None): 
				if (delay is None):  
					os.system("mencoder -oac copy -ovc lavc -sub "+subtitles+" -subfont-text-scale "+size+" -utf8 -o "+output+" "+video)
				else: 
					os.system("mencoder -oac copy -ovc lavc -sub "+subtitles+" -subfont-text-scale "+size+" -delay "+delay+" -utf8 -o "+output+" "+video)
			else: 
				if (delay is None):  
					os.system("mencoder -oac copy -ovc lavc -sub "+subtitles+" -subfont-text-scale "+size+" -font "+font+" -utf8 -o "+output+" "+video)
				else: 
					os.system("mencoder -oac copy -ovc lavc -sub "+subtitles+" -subfont-text-scale "+size+" -font "+font+" -delay "+delay+" -utf8 -o "+output+" "+video)
		
		if autoplay = "yes": 
			self.play(output)
			
	def play(self,output):
		os.system("mplayer "+output)
