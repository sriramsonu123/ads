# -*- coding: utf-8 -*-

"""
Created on Sun Mar  5 16:01:49 2023

@author: sriram
"""
import matplotlib.pyplot as plt
import pandas as pd
url = 'https://drive.google.com/file/d/14zkBKvx027rg4Xf6H3EFbtCNKMedk4qT/view?usp=drivesdk'
data = pd.read_csv("https://drive.google.com/uc?export=download&id="+url.split('/')[-2])
data = data.drop(columns=['Series Name', 'Series Code',
                 'Country Code'])
data = data.dropna()

data = data.rename(columns={'Country Name': 'Country'})
print(data)

x = data['Country']

y = data['2010 [YR2010]']

# bar graph of year 2010
plt.figure(figsize=(10, 6))
plt.bar(x, y, label='Military Expenditure')
plt.xlabel('Country')
plt.ylabel('Military expenditure')
plt.title('Bar graph of Military Expenditure in year 2014')
plt.legend()
plt.show()
# pie chart of year 2014
plt.figure(figsize=(8, 5))
plt.pie(data['2014 [YR2014]'], labels=data['Country'])
plt.title('pie chart of Military Expenditure in year 2014')
plt.show()
# pie chart of year 2020
plt.figure(figsize=(8, 5))
plt.pie(data['2020 [YR2020]'], labels=data['Country'])
plt.title('pie chart of Military Expenditure in year 2020')
plt.show()
# line plot
year = ['2012','2013','2014', '2015', '2016', '2017', '2018', '2019', '2020','2021']
plt.figure(figsize=(8, 5))
plt.plot(year, data.iloc[0, 11:21], label='CAN')
plt.plot(year, data.iloc[1, 11:21], label='CHINA')
plt.plot(year, data.iloc[2, 11:21], label='IND')
plt.plot(year, data.iloc[3, 11:21], label='USSR')
plt.plot(year, data.iloc[4, 11:21], label='UK')
plt.plot(year, data.iloc[5, 11:21], label='US')
plt.xlabel('Year')
plt.ylabel('Military expenditure')
plt.title('line plot of Military Expenditure from 2014 to 2020')
plt.legend()
plt.show()