#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 17 14:24:19 2019

@author: ian
"""


for prov in province_list:
    for mode in model_list:
        db_selected=db[(db.province==prov) & (db.model==mode)]
        series_original=pd.Series(db_selected.salesVolume)
        series=[]
        for i in series_original.index:
            series.append(series_original[i])
        model = ARIMA(series, order=(1,1,0))
        model_fit = model.fit(disp=0)
        forecast = model_fit.forecast(4)[0]
        for i in range(4):
            idx=form[(form.province==prov) & (form.model==mode) & (form.regMonth==i+1)].index.values
            submit.loc[idx,'forecastVolum']=max(int(forecast[i]),0)
        print(prov,mode)

submit.to_csv('submit.csv',sep=',',encoding='utf-8',index=None)