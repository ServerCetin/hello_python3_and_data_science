'''
    pandas is high level data manipulation tool
    built in numpy
    dataframe
'''

import pandas as pd

dict = {
    "country": ["Brazil", "Russia", "India", "China", "South Africa"],
    "capital": ["Brasilia", "Moscow", "New Delhi", "Beijing", "Pretoria"],
    "area": [8.516, 17.10, 3.286, 9.597, 1.221],
    "population": [200.4, 143.5, 1252, 1357, 52.98]
}

brics = pd.DataFrame(dict)

print(brics)  # table

# print(brics.index)  # RangeIndex(start=0, stop=5, step=1)

# brics = pd.read_csv("path/to/brics.csv") #dataframe from csv
# brics = pd.read_csv("path/to/brics.csv", index_col=0)

names = ['United States', 'Australia', 'Japan', 'India', 'Russia', 'Morocco', 'Egypt']
dr = [True, False, False, False, True, True, True]
cpc = [809, 731, 588, 18, 200, 70, 45]

my_dict = {'country': names, 'drives_right': dr, 'cars_per_cap': cpc}
row_labels = ['US', 'AUS', 'JPN', 'IN', 'RU', 'MOR', 'EG']

cars = pd.DataFrame(my_dict)
cars.index = row_labels
print(cars)

'''
    Index and select data
        Square brackets
        Advanced methods
            loc label based
            iloc integer position based
'''

print(cars['country'])  # only ids and country and name,dtype
type(cars['country'])  # pandas.core.series.Series

print(cars[['country']])  # only ids and country
type(cars[['country']])  # pandas.core.frame.DataFrame

print(cars[['country', 'drives_right']])
print(cars[1:3])  # aus and jpn data

print(cars.loc['RU'])  # returns list infos for RU
print(cars.loc[['RU']])  # returns table format infos for RU

print(cars.loc[['RU', 'JPN', 'IN']])  # returns table format infos for RU

print(cars.loc[['RU', 'JPN', 'IN'], ['country', 'drives_right']])
print(cars.loc[:, ['country', 'drives_right']])

print(cars.iloc[[0]]) # US infos as table
#iloc is same format with loc but only indexes
