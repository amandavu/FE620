#!/usr/bin/env python
# coding: utf-8

# In[3]:


#QQ plot from AAPL

#import libraries

import scipy.stats as stats
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import yfinance as yf   


#=========================================

#downloading AAPL stock from jan 2024 to april 2025 

tickers = ['AAPL']
data = yf.download(tickers, start = '2024-01-02', end = '2025-4-17')

#=========================================

#taking closes 

data = data['Close']
df = pd.DataFrame(data)

#=========================================

#log returns (calculated previously)

df['Log Returns'] = np.log(df['AAPL']/df['AAPL'].shift(1))  

#dropping empty rows 

df = df.dropna()

#=========================================

#generating quantile plot 


plt.figure(figsize=(8,6))
stats.probplot(df['Log Returns'], dist="norm", plot=plt)

plt.title('QQ Plot - AAPL Log Returns')

plt.xlabel('Theoretical Quantiles')
plt.ylabel('Sample Quantiles')

plt.grid(True)
plt.show()


# In[ ]:




