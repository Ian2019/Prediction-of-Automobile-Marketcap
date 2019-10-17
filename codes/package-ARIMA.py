#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 17 14:23:42 2019

@author: ian
"""

import pandas as pd
from statsmodels.tsa.arima_model import ARIMA
import numpy as np
db=pd.read_csv("train_sales_data.csv")
form=pd.read_csv("evaluation_public.csv")
submit=pd.read_csv("submit_example.csv")
search=pd.read_csv("train_search_data.csv")
reply=pd.read_csv("train_user_reply_data.csv")
province_list=list(set(db.province))
model_list=list(set(db.model))

split_point = 20