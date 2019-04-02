# -*- coding: utf-8 -*- 
from pytrends.request import TrendReq


def googleTrend(a, b):
    pytrend = TrendReq()
    pytrend.build_payload(kw_list=[a,b], timeframe='now 7-d')
    interest_over_time_df = pytrend.interest_over_time()
    print(interest_over_time_df.head())