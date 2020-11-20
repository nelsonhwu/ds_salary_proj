# -*- coding: utf-8 -*-
"""
Created on Thu Nov 19 16:22:30 2020

@author: Nelson J Hwu
"""

import requests
from data_input_da import data_in

URL = 'http://127.0.0.1:5000/predict'
headers = {"Content-Type": "application/json"}
data = {"input": data_in}

r = requests.get(URL,headers=headers, json=data) 

r.json()