#!/usr/bin/env python3
import requests
import json
import sys

def usage():
  print("Usage : ./main.py cur1 cur2")
if(len(sys.argv)<1):
  usage()

def convert(curto):
  response = requests.get("https://api.exchangerate-api.com/v4/latest/USD").text
  response = response.lower() 
  dict_obj = json.loads(response)
  rates = dict_obj.get('rates')
  curto = rates.get(curto)
  return curto
  
cur = sys.argv[1]

print(convert(cur))


