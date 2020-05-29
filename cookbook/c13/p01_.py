#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
Topic: 
Desc : 
"""

import fileinput



"""
	接收任何的输入
	打印：输入的内容
"""
def receiveAnyInput():
	with fileinput.input() as f:
		for line in f:
			print(line, end='')


def receiveFile():
	with fileinput.input('/etc/passwd') as f:
		for line in f:
			print(f.filename(), f.filelineno(), line, end=)

if __name__ == '__main__':
	receiveAnyInput()