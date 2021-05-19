# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Date    		: 2021/05/19
# @Author  		: Freelin Li
# @Maintain  	: Freelin Li
# @File    		: dblib.py
# @Description 	: database. 
# @Dependency   : sqlite-utils (pip install sqlite-utils) refer to https://pypi.org/project/sqlite-utils/

import sqlite_utils
import copy

class DBlib():
	def __init__(self, filename):
		self.db = sqlite_utils.Database(filename)
		self.table = "dictionaries"
		self.itemlist = []
	def table_names(self):
		return self.db.table_names()

	def table_drop(self, tablename):
		self.db[tablename].drop()
	
	def table_dropall(self):
		namelist = self.table_names()
		for name in namelist:
			self.db[name].drop()

	def updatepk(self, pkstring):
		self.db[self.table].transform(pk = pkstring)

	def insert(self, uid, phrase, firstchar, firstword, spell, reference):
		try:
			self.getitembyword(uid)
		except:
			self.db[self.table].insert_all([
		    {"id": uid, "phrase": phrase, "firstchar": firstchar, "firstword": firstword,
		    "spell": spell, "reference": reference},
			], pk="id")
			
		else:
			print("exist")

	def insertlist(self, phraselist):
		self.db[self.table].insert_all(phraselist, pk="id")

	def printall(self):
		for row in self.db[self.table].rows:
			print(row)

	def getitembyword(self, word):
		return self.db[self.table].get(word)

	def getitembykeyvalue(self, columns, value):
		self.db[self.table].enable_fts([columns])
		self.itemlist.clear()
		for item in self.db[self.table].search(value):
			self.itemlist.append(item)
		self.db[self.table].disable_fts()
		return self.itemlist

if __name__ == '__main__':
	# db = sqlite_utils.Database("demo_database.db")
	# This line creates a "dogs" table if one does not already exist:
	# db["dogs"].insert_all([
	#     {"id": 1, "age": 4, "name": "Cleo"},
	#     {"id": 2, "age": 2, "name": "Pancakes"}
	# ], pk="id")
	# for row in db["dogs"].rows:
	# 	print(row)
	# print("")
	# for row in db["dogs"].rows_where(select='name, age'):
	# 	print(row)
	# print("")
	# for row in db["dogs"].rows_where("age > 1", order_by="age"):
	# 	print(row)

	# print("")

	PinDb = DBlib("database.db")
	print(PinDb.table_names())
	PinDb.table_dropall()
	PinDb.insert(0, u"地老天荒", "d", "di", "di lao tian huang", "很久很久啊")
	PinDb.insert(1, u"皇天在上", "h", "huang", "huang tian zai shang", "很久很久啊")
	PinDb.insert(2, u"上天入地", "s", "shang", "shang tian ru di", "很久很久啊")
	PinDb.insert(3, u"地动山摇", "d", "di", "di dong shan yao", "很久很久啊")
	PinDb.printall()
	print("--------------------")
	print(PinDb.table_names())
	PinDb.updatepk("spell")
	print(PinDb.getitembyword("di lao tian huang"))
	print("--------------------")
	print(PinDb.table_names())
	# PinDb.updatepk("firstword")
	# print(PinDb.getitembyword("di"))
	print("--------------------------------------000000000")
	print(PinDb.getitembykeyvalue("firstword", "di"))
	
