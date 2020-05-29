#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
Topic: 
Desc : 
"""


import sys
sys.stderr.write('it failed \n')
raise SystemExit(1)


"""
	相比上面的方法，简单有效的自定义抛出异常并退出
"""
raise SystemExit('it failed')
