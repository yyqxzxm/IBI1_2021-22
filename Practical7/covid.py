#import all needed packages
import os
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
#change to the directory
os.chdir("/Users/zhengximeng/IBI1_2021-22/Practical7")
#import the file
covid_data = pd.read_csv("full_data.csv")

#show the first and third columns from rows 10-20 
print(covid_data.iloc[9:20,[0,2]])

#use a Boolean to show “total cases” for all rows corresponding to Afghanistan.
Afghanistan_rows = (covid_data.loc[:,'location']=='Afghanistan')
print(covid_data.loc[Afghanistan_rows,["location","total_cases"]])

#compute the mean number of new cases and new deaths in China
China_rows = (covid_data.loc[:,'location']=='China')
print(covid_data.loc[China_rows,["location","total_cases"]])
china_new_cases = covid_data.loc[China_rows,'new_cases']
china_new_death = covid_data.loc[China_rows,'new_deaths']
mean_newcases = china_new_cases.mean()
mean_newdeath = china_new_death.mean()
china_dates = covid_data.loc[China_rows,'date']

print(mean_newcases)
print(mean_newdeath)

#create a boxplot of new cases and new deaths in China worldwide
data_all = [china_new_cases,china_new_death]
plt.boxplot(data_all,patch_artist = True,showmeans = True,labels = ('new cases','new death'))
plt.title("new cases and new deaths in China")
plt.show()

#plot both new cases and new deaths in China over time
figl = plt.figure(num='china_cases',figsize = (9,9),dpi = 75,facecolor = 'lightskyblue')
plt.plot(china_dates,china_new_cases,'b+')
plt.plot(china_dates,china_new_death,'ro')
plt.xlabel('dates')
plt.ylabel('number of people')
plt.xticks(china_dates.iloc[0:len(china_dates):4],rotation=-90)
plt.show()

#pursue a question that interests me.(the question is in File question.txt)
Germany_rows = (covid_data.loc[:,'location']=='Germany')
print(covid_data.loc[Germany_rows,["location","date"]])
#After printing the last result, find the number of rows where the latest date is located, that is, row 2816
Germany_totalcases_latest = covid_data.loc[2816,"total_cases"]
Germany_totaldeaths_latest = covid_data.loc[2816,"total_deaths"]
G = Germany_totaldeaths_latest/Germany_totalcases_latest
print(G)


UK_rows = (covid_data.loc[:,'location']=='United Kingdom')
print(covid_data.loc[UK_rows,["location","date"]])
#After printing the last result, find the number of rows where the latest date is located, that is, row 7625
UnitedKingdom_totalcases_latest = covid_data.loc[7625,"total_cases"]
UnitedKingdom_totaldeaths_latest = covid_data.loc[7625,"total_deaths"]
UK = UnitedKingdom_totaldeaths_latest/UnitedKingdom_totalcases_latest
print(UK)

