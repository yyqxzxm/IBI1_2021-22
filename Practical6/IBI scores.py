#import module
import numpy as np
import matplotlib.pyplot as plt
scores = [45,36,86,57,53,92,65,45]#List 8 grades
print (sorted(scores))#sorting lists
plt.boxplot(scores,labels=["Rob"],patch_artist = True)
#Display boxplot, mark Rob's score, display background color
plt.title("IBI scores")#make title
plt.ylabel('scores')#Make a Y-axis label
plt.show()#show the boxplot

avg = sum(scores)/len(scores)#Calculate grade averages
print(avg)
if avg>=60:
    print("Pass")
else:
    print("Fail")
#Test whether the average score is passed
