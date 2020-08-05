#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb  7 19:31:37 2020

@author: William Guenneugues 
"""

import re
import urllib

#function findemail takes in url and returns list of all emails present on the url page, accounting for alternate email spellings
def findemail(url):
    #takes url and returns string of page
    s=urllib.request.urlopen(url).read().decode()
    #searches for email addresses
    matches = re.findall(r"(\w+(@| AT | at |\[AT\]|\[at\])\w+(\.| DOT | dot |\[DOT\]|\[dot\])(\w ?\.?)+)", s)
    #takes out unwanted elements from matches array
    emails=[]
    for m in matches:
        emails.append(m[0])
    return emails
