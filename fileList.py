#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
import commandPronpt

def fileListInFolder(path):
    list = os.listdir(path)
    ofStream = open('fileList.txt', 'w') # 書き込みモードで開く
    str = ""

    for file in list:
        str += file + '\n'

    ofStream.write(str)
    ofStream.close()

folderPath = commandPronpt.commandLine()
print folderPath
fileListInFolder(folderPath)
