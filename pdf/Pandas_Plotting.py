# -*- coding: utf-8 -*-
"""
Created on Mon Apr  6 13:41:37 2020

@author: brayd
"""

# Part 1 - Customer Loan Data with Pandas
import pandas as pd

df1 = pd.read_csv('loan-data-v1.csv')

print(df1.dtypes)

df1_sorted = df1.sort_values(by='Days Delinquent', ascending = False)
print(df1_sorted)

df1_filtered = df1_sorted[df1_sorted['Days Delinquent'] >= 90]
print(df1_filtered)

df1_sliced = df1_filtered[['Name','State','Days Delinquent','Years as Customer']]
print(df1_sliced)

df1_sliced.to_csv('/Users/brayd/Documents/CIS 325/loan-data-v1-output.csv',index=False,header=True)

# Part 2 - Remote Data Access with Pandas
# 2.2 - Download Economic Data
import pandas_datareader.data as web
from datetime import datetime

start = datetime(2014, 1, 1) # start date
end = datetime(2018, 12, 31) # end date

# Download Stock Exchange Index (SEI) and Unemployment Rate (URATE) data
df_us = web.DataReader('ticker=SEIUS,URATEUS', 'econdb', start, end) # for USA 
df_ca = web.DataReader('ticker=SEICA,URATECA', 'econdb', start, end) # for Canada

# Change column names for df_us and df_ca
df_us.columns = ['stock', 'urate']
df_ca.columns = ['stock', 'urate']

df_us.to_csv('econ_us.csv')
df_ca.to_csv('econ_ca.csv')

# 2.3 - Processing Economic Data
df_us = pd.read_csv('econ_us.csv')
df_ca = pd.read_csv('econ_ca.csv')

def convert_datetime(df):
    df['TIME_PERIOD'] = pd.to_datetime(df['TIME_PERIOD'])
    df.set_index(['TIME_PERIOD'], inplace = True)
    return df
df_us = convert_datetime(df_us)
df_ca = convert_datetime(df_ca)

df_sei = pd.DataFrame(pd.concat([df_us['stock'],df_ca['stock']],axis=1,keys = ['US','CA']))

# 2.4 - Computing Statistics of Stock Exchange Index Data
returns = df_sei.pct_change()   # MoM Percent Changes for US and CA

ans1 = returns['US'].mean()     # average MoM SEI percent change for USA
ans2 = returns['CA'].mean()     # average MoM SEI percent change for Canada
ans3 = df_sei['US'].max()       # highest SEI for USA
ans4 = df_sei['US'].idxmax()    # date when the highest SEI for USA happened
ans5 = df_sei.loc[ans4, 'CA']   # SEI value for Canada on the same date (= your ans4)

# 2.5 - Plotting Stock Exchange Data Index Data
import seaborn as sns
# Set the figure size (width, height) in inches
sns.set(rc={'figure.figsize':(11, 4)})
# Plot DataFrame df_sei
ax1 = df_sei.plot(linewidth=2)
# Set y-axis label to be "Stock Exchange Index"
ax1.set_ylabel('Stock Exchange Index')

normalize = lambda x: (x - x.min()) / (x.max() - x.min())

df_sei_normalized = df_sei.apply(normalize)

sns.set(rc={'figure.figsize':(11, 4)})
ax1 = df_sei_normalized.plot(linewidth=2)
ax1.set_ylabel('Stock Exchange Index')










