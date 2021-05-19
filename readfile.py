# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Date    		: 2021/05/19
# @Author  		: Freelin Li
# @Maintain  	: Freelin Li
# @File    		: readfile.py
# @Description 	: read file.

import sys

sys.path.append(".")

class PyReadFile():
	def __init__(self, filename):
		self.filename = filename
		
		if isinstance(filename, str):
			with open(filename, 'r', encoding='utf8') as file:
				self.data  = file.readlines() 
				file.close()
		else:
			print("use str para!")	
	
	def read_data(self):	
			return self.data

	def write_data(self, file, jsondata):
		with open(file, 'w') as file:
			file.write(jsondata)
			file.close()

if __name__ == '__main__':
	fd = PyReadFile("chengyu.txt")
	data = fd.read_data()
	# print(data)
	itemnum = 0
	for item in data:
		itemnum += 1
		print(item)
	print("item sum :\t", itemnum) # 23148