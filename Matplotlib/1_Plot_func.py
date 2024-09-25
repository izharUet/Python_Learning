# Line plot and the necessary requirements of plotting
from matplotlib import pyplot as plt

# Checking the plot styles
print(plt.style.available)
plt.style.use('ggplot')

# X_axis and Y_axis data
dev_x = [25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35]
dev_y = [2345,2783,2893,2849,4893,5000,3782,5032,2537,3768,2430]

#plotting
plt.plot(dev_x, dev_y, color ='c', linestyle = '--',linewidth =1,label = 'All Developer')
py_dev_y = [3450,4040,3450,3640,3900,3670,2780,3000,3430,3780,3890]
plt.plot(dev_x, py_dev_y, color='b',linestyle ='-',linewidth =1,label = 'Python Developer')

plt.title("Salary in respective years")
plt.xlabel('Ages of person')
plt.ylabel('Monthly Salary')
plt.legend()
plt.tight_layout()
#plt.savefig('image.png', dpi =1600)  # used to save the image
plt.show()