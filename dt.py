#!/usr/bin/python3
#
# 2つの日付の差分を求めるスクリプト
#
#Usage: python3 dt.py
#

import datetime
s1,s2=input("Input YYY1/M1/D1 YYY2/M2/D2:").split()
y1,m1,d1=(int(x) for x in s1.split('/'))
y2,m2,d2=(int(x) for x in s2.split('/'))
dt1 = datetime.datetime(y1, m1, d1)
print(dt1)
dt2 = datetime.datetime(y2, m2, d2)
print(dt2)
td = dt2 - dt1
print(td)
