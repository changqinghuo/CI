import pandas
from qstkutil import DataAccess as da
import numpy as np
import math
import copy
import qstkutil.qsdateutil as du
import datetime as dt
import qstkutil.DataAccess as da
import qstkutil.tsutil as tsu
import qstkstudy.EventProfiler as ep
import sys
import matplotlib.pyplot as plt
from pylab import *

bechmark = sys.argv[2]
symbols = []
symbols.append(str(bechmark))

dataobj = da.DataAccess('Yahoo')
startday = dt.datetime(2011,1,1)
endday = dt.datetime(2011,12,31)
timeofday = dt.timedelta(hours=16)
timestamps = du.getNYSEdays(startday, endday, timeofday)
close = dataobj.get_data(timestamps, symbols, 'close')
close = (close.fillna(method='ffill')).fillna(method='backfill')

value_file = open(sys.argv[1])
print sys.argv[1]
values = []
for line in value_file:
    values.append(float(line.split(',')[-1]))
plt.clf()
pricedat = close.values # pull the 2D ndarray out of the pandas object
pricedat = pricedat / pricedat[0,:]
print pricedat
base = values[0]
for i in range(len(values)):
    values[i] = values[i]/base
print values
plt.plot(timestamps,pricedat)
plt.plot(timestamps,values)
symbols = ['$SPX','Vaule']
plt.legend(symbols)
plt.ylabel('Adjusted Close')

plt.xlabel('Date')
savefig('adjustedclose.pdf',format='pdf')

