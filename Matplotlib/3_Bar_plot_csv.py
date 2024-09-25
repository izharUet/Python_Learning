#Grabing Data from CSV file, loading and reading the data using pandas library
import csv
import numpy as np
import pandas as pd
from collections import Counter
from matplotlib import pyplot as plt

#print(plt.style.available)
plt.style.use('ggplot')

#Working with csvfile direclty.

# with open('data.csv') as csv_file:
#     csv_reader = csv.DictReader(csv_file)    #using dictionary as csv reader
#
#     # instantiating variable for counting.
#     languages_counter = Counter()
#     # # reading the first row
#     # row = next(csv_reader)
#     # print(row) # printing entire key values at first row
#     # #print(type(row))
#     # # As the data is working with most working languages.
#     # # printing the specific row element instead of entire row
#     # print(row['LanguagesWorkedWith'])  # accessing the specific key:values
#     # #print(row.get('LanguagesWorkedWith')) # also get the specific key:values
#     #
#     # # As there are semicolon in value of dict
#     # # converting to lists.
#     # print(row['LanguagesWorkedWith'].split(';'))
#
#     # Counting the most worked language using the built-in counter.
#     for row in csv_reader:
#         languages_counter.update(row['LanguagesWorkedWith'].split(';')) # update  every rows

#print(languages_counter)

# print the 15 most common languages out of 28.
#print(languages_counter.most_common(15))

# using the pandas method to import data and ploting.
languages_counter = Counter()
data = pd.read_csv('data.csv')
ids = data['Responder_id']
lang_responses = data['LanguagesWorkedWith']
for response in lang_responses:
    languages_counter.update(response.split(';'))

# ploting using the Bar chart.
languages =[]
popularity =[]
for item in languages_counter.most_common(15):
    languages.append(item[0])
    popularity.append(item[1])

# for descending popularity.
languages.reverse()
popularity.reverse()

plt.barh(languages, popularity)   # used for horizontal bar
plt.title('Most Popular Languages')
plt.ylabel('Programming Language')
plt.xlabel('No of People Using')
plt.tight_layout()
plt.show()
