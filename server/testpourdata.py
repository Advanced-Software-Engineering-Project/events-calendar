# -*- coding: utf-8 -*-
"""
Created on Mon Oct 31 16:48:22 2016

@author: peng
"""

import json
f = open('../scraper/events_data.json','r')
test = json.load(f)

print test[0]

