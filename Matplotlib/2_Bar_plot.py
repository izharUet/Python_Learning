# Bar plot concept in the matplotlib
from matplotlib import pyplot as plt
import numpy as np

# Styles of graphs
print(plt.style.available)
plt.style.use('ggplot')

#Axis and the necessary info for bar plot.
dev_x = [25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35]
x_indexes = np.arange(len(dev_x))  # For evenly spaced x_axis
width = 0.25  # To set bar in certain distance

dev_y = [2345,2783,2893,2849,4893,5000,3782,5032,2537,3768,2430]
py_dev_y = [3450,4040,3450,3640,3900,3670,2780,3000,3430,3780,3890]

# Bar plot coding section
plt.bar(x_indexes-width, dev_y, width=width, label = 'All Developer')
plt.bar(x_indexes, py_dev_y, width=width, label = "Python Developer")
plt.title("Salary in respective years")
plt.xticks(ticks=x_indexes, labels=dev_x)
plt.xlabel('Ages of person')
plt.ylabel('Monthly Salary')
plt.legend()
plt.tight_layout()
# plt.savefig('image.png', dpi =1600)
plt.show()