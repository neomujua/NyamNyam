# -*- coding: utf-8 -*- 
from pytrends.request import TrendReq


def googleTrend(a):
    pytrend = TrendReq()
    pytrend.build_payload(kw_list=[a], timeframe='now 7-d')
    interest_over_time_df = pytrend.interest_over_time()
    semiResult = interest_over_time_df.head()
    #print(semiResult.ix[1][0]) #ix[0~4][0~1]
    sumOfChoice = 0
    for i in range(0,5):
        sumOfChoice += semiResult.ix[i][0]
    print(sumOfChoice)
    #print(semiResult)
    return sumOfChoice