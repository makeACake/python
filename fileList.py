#!/usr/bin/python
# -*- coding: utf-8 -*-

import os

list = os.listdir(".")
ofStream = open('fileList.txt', 'w') # 書き込みモードで開く
str = ""

for file in list:
 str += file + '\n'

ofStream.write(str)
ofStream.close()
