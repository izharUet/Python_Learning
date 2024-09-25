# Area plot or stack plot
# import the necessary library
from matplotlib import pyplot as plt

#figure sytle
plt.style.use('fivethirtyeight')

minutes = [1,2,3,4,5,6,7,8,9]
player_1 = [1,2,3,3,3,4,4,4,5]
player_2 = [1,1,1,1,1,2,2,2,4]
player_3 = [1,1,1,1,1,2,2,2,2]

#Plotting in stack
labels = ['player_1','player_2','player_3']
plt.stackplot(minutes,player_1, player_2, player_3, labels=labels)
plt.legend(loc='upper left')
plt.title('Stack Plot')
plt.tight_layout()
plt.show()

