#Histogram concept in matplotlib
from matplotlib import pyplot as plt
import pandas as pd

# print(plt.style.available)
plt.style.use('ggplot')

plt.figure(figsize = (8,5))

# Reading the data
data = pd.read_csv('data2.csv')
ages =data.Age
ids = data.Responder_id
# ages = [18,19,21,25,26,27,29,30,31,32,32, 33,35,45]

#Bins setting for the histogram ploting
bins = [10,20,30,40,50,60,70,80,80,90,100]
plt.hist(ages, 'auto',(0,100), color='green', edgecolor = 'black',
         rwidth=0.8,log=True, bottom=0)

# Median in histogram
median_age = 29
color = '#fc4f30'
plt.axvline(median_age,color = color, label = 'Age Median', linewidth = 2)

plt.legend()
plt.title('Ages of Respondent')
plt.xlabel('Ages')
plt.ylabel('Total Respondent')
plt.tight_layout()
plt.show()
