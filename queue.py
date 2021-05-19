# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Date    		: 2021/05/19
# @Author  		: Freelin Li
# @Maintain  	: Freelin Li
# @File    		: pinyin.py
# @Description 	: get pinyin.
# @Dependency   : xpinyin (pip install xpinyin) refer to https://pypi.org/project/xpinyin/

import copy

import sqlite_utils

from pinyin import PinYin
from readfile import PyReadFile
from dblib import DBlib


def producedb():
	Pin = PinYin()
	PinDb = DBlib("database.db")
	print(PinDb.table_names())
	PinDb.table_dropall()

	fd = PyReadFile("chengyu.txt")
	data = fd.read_data()
	# print(data)
	phraselist = []
	itemnum = 0
	for item in data:
		itemnum += 1
		# print(item)
		(phrase, reference)= item.split("    ")

		phraselist.append(
			{'id': itemnum, 'phrase': phrase, 'firstchar': Pin.get_pin(phrase).split(" ")[0][0:1], 
			'firstword':  Pin.get_pin(phrase).split(" ")[0], 'spell':  Pin.get_pin(phrase), 'reference': reference})
	# print(phraselist)
	PinDb.insertlist(phraselist)
	# TODO try to use more processes. Dividing the serial number

	print("item sum :\t", itemnum) # 23148


def queue_run(phrase, deep):
	Pin = PinYin()
	PinDb = DBlib("database.db")
	dictlist = []
	deepnum = 0
	errornum = 0
	print(PinDb.table_names())
	
	lastword = Pin.get_pin(phrase).split(" ")[-1:][0]
	print("LAST WORD:", lastword)
	# PinDb.printall()
	# print("--------------------")
	while deepnum < deep:
		try:
			dictlist = PinDb.getitembykeyvalue("firstword", lastword)
			print(dictlist[0])
			lastdictlist = copy.deepcopy(dictlist)
			lastword = Pin.get_pin(dictlist[0]['phrase']).split(" ")[-1:][0]
			print(lastword)
		except:
			print("getitembykeyvalue or get_pin is incorrect")
			lastdictlist.pop(0)
			# print(lastdictlist)

			# back to the latest word to find another route
			lastword = Pin.get_pin(lastdictlist[0]['phrase']).split(" ")[-1:][0]
			errornum += 1

			if errornum > 10:
				print("deep number:\t", deepnum)
				break

			
		else:
			deepnum += 1
			errornum = 0
			print("LAST WORD:", lastword)
	print("deep number:\t", deepnum)

if __name__ == '__main__':

	# producedb()
	queue_run("昏天黑地", 512)
	