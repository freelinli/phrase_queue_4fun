# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Date    		: 2021/05/19
# @Author  		: Freelin Li
# @Maintain  	: Freelin Li
# @File    		: pinyin.py
# @Description 	: get pinyin.
# @Dependency   : xpinyin (pip install xpinyin) refer to https://pypi.org/project/xpinyin/

import sys
from xpinyin import Pinyin

class PinYin():
	def __init__(self):
		self.Pin = Pinyin()

	def get_pin(self, str):	
		return self.Pin.get_pinyin(str, ' ')

	def get_pin_show_tone(self, str):
		return self.Pin.get_pinyin(str, ' ', tone_marks='marks')

	def get_pins(self, str):
		return self.Pin.get_pinyins(str, splitter=' ', tone_marks='marks')
	
	def get_initials(self, str):
		return self.Pin.get_initials(str)

	def get_first_initial(self, str):
		return self.Pin.get_initials(str)[0:1]

	# TODO it's better to get spell from network URI.
	# Because there are so many the same words with the differnet spell.

if __name__ == '__main__':
	string = u"爱沙尼亚"
	Pin = PinYin()
	print(Pin.get_pin(string))
	print(Pin.get_pin(string).split(" ")[0])
	print(Pin.get_pin_show_tone(string))
	print(Pin.get_pins(string))
	print(Pin.get_initials(string))
	print(Pin.get_first_initial(string))