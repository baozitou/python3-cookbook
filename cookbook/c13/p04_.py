#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
Topic: 
Desc : 
"""
import getpass

user = getpass.getuser()
passwd = getpass.getpass()

if user=='abc' & passwd=='abc':
	print('ok')
else:
	print('no')