#!/usr/bin/python
import os
import sys
import re 

class Mencoder():

	def addsubs(self, video, subtitles,font,size,delay,add,autoplay):
		output = video
		output_list= re.split(r'(.*\/)*', output)
		output=output_list[1]+"new_video.avi"
		if add=='no':
			return None

		common_params = "mencoder -oac copy -ovc lavc -sub " + subtitles + " -utf8"
		font_params = ""
		size_params = ""
		delay_params = ""

		if font != "":
			font_params = " -font " + font

		if size != "":
			size_params = " -subfont-text-scale " + size

		if delay != "":
			delay_params = " -delay " + delay

		#os.system(common_params + font_params + size_params + delay_params + " -o " + output + " " + video)

		#if autoplay == 'yes':
			#self.play(output)

	def play(self,output):
		os.system("mplayer "+output)
