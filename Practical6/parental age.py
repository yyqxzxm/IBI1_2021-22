paternal_age=[30,35,40,45,50,55,60,65,70,75]
chd=[1.03,1.07,1.11,1.17,1.23,1.32,1.42,1.55,1.72,1.94]
dir = {}#create and print a dictionary
for i in range(len(paternal_age)):
    dir[paternal_age[i]] = chd[i]
print(dir)#Make the data of different paternal age correspond to the data of CHD of their offspring one by one
age = 40#You can put in other ages
print("The risk for CHD in the offspring of a father of",age,"is",dir[int(age)])#Show the conclusion
#import module
import numpy as np
import matplotlib.pyplot as plt
N = 10
x = (30,35,40,45,50,55,60,65,70,75)#The X-axis shows paternal Age data
y = (1.03,1.07,1.11,1.17,1.23,1.32,1.42,1.55,1.72,1.94)#The Y-axis shows data about CHD risk
plt.ylabel('risk for congenital heart disease in the offspring')#Make a Y-axis label
plt.xlabel('paternal age')#Make a X-axis label
plt.title('Parental age vs offspring health')#make title
plt.scatter(x,y,marker= 'x',color='crimson')#Change the icon style and icon color
plt.show()##show the scatter plot

