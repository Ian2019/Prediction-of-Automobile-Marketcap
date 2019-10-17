#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 17 14:26:54 2019

@author: ian
"""




NRMSE=0
for prov in province_list:
    for mode in model_list:
        db_selected=db[(db.province==prov) & (db.model==mode)]
        dataset, validation = db_selected[0:split_point], db_selected[split_point:]
        series=[]
        for i in validation.index:
            series.append(validation.loc[i,'salesVolume'])
        model = pf.ARIMAX(data=dataset, formula='salesVolume~1+popularity+carCommentVolum+newsReplyVolum', ar=1, ma=1, integ=1, family=pf.Normal())
        x = model.fit() 
        forecast_temp=model.predict_is(h=4,fit_once=False,fit_method="MLE")
        forecast=[]
        for i in forecast_temp.index:
            forecast.append(forecast_temp.loc[i,'Differenced salesVolume'])
        history=list(db_selected['salesVolume'])
        for i in range(4):
            forecast[i]=int(inverse_difference(history,forecast[i],interval=1))
            history.append(forecast[i])
        sum=0
        mean=0
        for i in range(4):
            sum=sum+(forecast[i]-series[i])*(forecast[i]-series[i])
            mean=mean+series[i]/4
        NRMSE=NRMSE+np.sqrt(sum/4)/mean
        print(prov,mode)
Score=1-NRMSE/(len(province_list)*len(model_list))
Score

