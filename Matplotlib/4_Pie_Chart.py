from matplotlib import pyplot as plt
plt.style.use('fivethirtyeight')

slices = [60,40,30,20]
label = ('Sixty', 'Fourty', 'Extra1', 'Extra2')
explode = [0,0,0,0.1]

colors = ['#008fd5', '#fc4f30', '#e5ae37', '#6d904f']
plt.pie(slices, labels = label, explode = explode, shadow = True,
        startangle= 270, colors = colors, autopct='%1.1f%%', wedgeprops={'edgecolor':'black'})
plt.title('Awesome Pie Chart')
plt.tight_layout()
plt.show()