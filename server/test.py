# -*- coding: utf-8 -*-
"""
Created on Sun Oct 23 13:30:14 2016

@author: peng
"""

from app import db
from app import signup, login, event_handler


#signup('admin8', 'passwd8')
#signup('admin4', 'passwd4')
#signup('admin3', 'passwd3')

print login('admin3', 'passwd3')
print login('admin3', 'passwd4')

#print event_handler('POST')

#print event_handler('GET')
