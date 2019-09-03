#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Aug 30 14:14:29 2019

@author: ian
"""

import requests
import json
inp = 'insert your keyword'
response = requests.get('https://www.instagram.com/explore/tags/'+inp+'/?__a=1')
data = response.json()
print(data)
print(type(data))
file_object = open(str(inp)+'.json', 'w')

json.dump(data, file_object)
