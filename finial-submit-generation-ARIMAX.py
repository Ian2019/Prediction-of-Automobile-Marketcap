#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 17 14:26:23 2019

@author: ian
"""

for prov in province_list:
    for mode in model_list:
        db_selected=db[(db.province==prov) & (db.model==mode)]
        model = pf.ARIMAX(data=db_selected, formula='salesVolume~1+popularity+carCommentVolum+newsReplyVolum', ar=1, ma=1, integ=1, family=pf.Normal())
        x = model.fit() 
        forecast_temp=model.predict_is(h=4,fit_once=False,fit_method="MLE")
        forecast=[]
        for i in forecast_temp.index:
            forecast.append(forecast_temp.loc[i,'Differenced salesVolume'])
        history=list(db_selected['salesVolume'])
        for i in range(4):
            forecast[i]=int(inverse_difference(history,forecast[i],interval=1))
            history.append(forecast[i])
        for i in range(4):
            idx=form[(form.province==prov) & (form.model==mode) & (form.regMonth==i+1)].index.values
            submit.loc[idx,'forecastVolum']=max(int(forecast[i]),0)
        print(prov,mode)