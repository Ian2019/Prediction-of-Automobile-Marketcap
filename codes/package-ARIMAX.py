#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 17 14:26:01 2019

@author: ian
"""



import pyflux as pf
def inverse_difference(history, yhat, interval=1):
	return yhat + history[-interval]


for i in range(len(search)):
    idx=db[(db.province==search.iloc[i].province) & (db.model==search.iloc[i].model) & (db.regYear==search.iloc[i].regYear) & (db.regMonth==search.iloc[i].regMonth)].index.values
    db.loc[idx,'popularity']=search.iloc[i].popularity

for i in range(len(reply)):
    idx=db[(db.model==reply.iloc[i].model) & (db.regYear==reply.iloc[i].regYear) & (db.regMonth==reply.iloc[i].regMonth)].index.values
    db.loc[idx,'carCommentVolum']=reply.iloc[i].carCommentVolum
    db.loc[idx,'newsReplyVolum']=reply.iloc[i].newsReplyVolum

db.to_csv("new_database.csv")