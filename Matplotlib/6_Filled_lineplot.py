# This script is used for the educational purpose to learn
# the concept of filled lineplot using matplotlib.pyplot library
from matplotlib import pyplot as plt
import pandas as pd

data = pd.read_csv('data1.csv')
ages = data['Age']   # data.Age is also acceptable
dev_salaries = data['All_Devs']
py_salaries = data['Python']
js_salaries = data['JavaScript']

# Plotting the figure
plt.figure(figsize=(8,5))
plt.plot(ages, dev_salaries, color = 'c', linestyle = '--',linewidth =1,label = 'All Developer')
plt.plot(ages,py_salaries, color= 'b',linestyle ='-',linewidth =1,label = 'Python Developer')

# median line to fill the plot above and below
median_salary = 57287
# plt.fill_between(ages, js_salaries, alpha =0.25)
plt.fill_between(ages, py_salaries, median_salary,
                 where = (py_salaries>median_salary),
                 interpolate= True, alpha = 0.25)

plt.fill_between(ages, py_salaries, median_salary,
                 where = (py_salaries<=median_salary),
                 interpolate= True, alpha = 0.25)

plt.title("Median Salary", fontdict= {'fontweight': 'bold'}, fontsize = 12)
plt.xlabel('Ages of person')
plt.ylabel('Monthly Salary')
plt.legend()
plt.tight_layout()
#plt.savefig('image.png', dpi =300)  # used to save the image
plt.show()