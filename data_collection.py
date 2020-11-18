# -*- coding: utf-8 -*-
"""
Created on Tue Nov 17 11:34:43 2020

@author: Nelson J Hwu
"""

import glassdoor_scraper as gs
import pandas as pd

path = "C:/Users/Nelson J Hwu/Documents/ds_salary_proj/chromedriver.exe"

df = gs.get_jobs('data scientist', 1000, False, path, 15)

df.to_csv('glassdoor_jobs_data_scientist.csv', index = False)