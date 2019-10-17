#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 17 14:24:55 2019

@author: ian
"""


NRMSE=0
for prov in province_list:
    for mode in model_list:
        db_selected=db[(db.province==prov) & (db.model==mode)]
        series_original=pd.Series(db_selected.salesVolume)
        series=[]
        for i in series_original.index:
            series.append(series_original[i])
        dataset, validation = series[0:split_point], series[split_point:]
        model = ARIMA(dataset, order=(3,1,0))
        model_fit = model.fit(disp=0)
        forecast = model_fit.forecast(4)[0]
        sum=0
        mean=0
        for i in range(4):
            sum=sum+(forecast[i]-validation[i])*(forecast[i]-validation[i])
            mean=mean+validation[i]/4
        NRMSE=NRMSE+np.sqrt(sum/4)/mean

Score=1-NRMSE/(len(province_list)*len(model_list))
Score


