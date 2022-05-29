import pandas as pd
import matplotlib.pyplot as plt

netflix_csv = pd.read_csv('netflix_data.csv')
netflix = pd.DataFrame(netflix_csv)
netflix_first_30 = netflix[:50]

print(netflix.head())
print(netflix.columns)

# histogram

# netflix_first_30['year'].hist()
netflix_first_30['duration'].hist(bins=6)
plt.show()

duration_mean = netflix_first_30.groupby('genre')['duration'].mean()
print(duration_mean)

# plot bar

duration_mean.plot(kind='bar', title='Table title')
plt.show()

# line plot and rotating axis labels 45 degree
duration_mean.plot(kind='line', x='duration', y='genre', rot=45)
plt.show()

# Scatter plots - scatters only can usable for data frames
netflix_first_30.plot(kind='scatter', x='duration', y='genre', rot=45)
plt.show()

# Layering plots with legends, action transparent
netflix_first_30[netflix_first_30['genre'] == 'Action']['duration'].plot(alpha=0.7)
netflix_first_30[netflix_first_30['genre'] == 'Comedies']['duration'].plot()
plt.legend(['Action', 'Comedies'])
plt.show()

# DETECTING MISSING VALUES

print(netflix_first_30.isna())

# Detecting any missing values
print(netflix_first_30.isna().any())  # has columns any missing values

# counting missing values
print(netflix_first_30.isna().sum())

netflix_first_30.isna().sum().plot(kind='bar')
plt.show()

# Removing missing values
# print(netflix_first_30.dropna())

print(netflix_first_30.fillna('null'))

'''
# From previous step
cols_with_missing = ["small_sold", "large_sold", "xl_sold"]
avocados_2016[cols_with_missing].hist()
plt.show()

# Fill in missing values with 0
avocados_filled = avocados_2016[cols_with_missing].fillna(0)

# Create histograms of the filled columns
avocados_filled[cols_with_missing].hist()

# Show the plot
plt.show()

'''

'''
Dictionary of lists - by column

dict_of_lists = 
{   "name": ["Ginger" , "Scout"], 
    "breed": ["Dachshund" , "Dalmatian"],
    "height _ cm": [22, 59],
    "weight _ kg": [10, 25], 
    "date_of_birth": ["2019-03-14" , "2019-05-09"] }
    
new_dogs = pd.DataFrame(dict_of_lists)

Dictionary of lists - by column

list_of_dicts = [ 
{  
   "name": "Ginger" ,
   "breed": "Dachshund" ,
   "height _ cm": 22,
   "weight _ kg": 10,
   "date _ of _ birth": "2019-03-14"
},
{"name": "Scout" , "breed": "Dalmatian" , "height _ cm": 59, "weight _ kg": 25, "date _ of _ birth": "2019-05-09"} ]
'''


# DataFrame to CSV
# new_dogs.to_csv("new_dogs_with_bmi.csv")

'''
# From previous step
airline_bumping = pd.read_csv("airline_bumping.csv")
print(airline_bumping.head())

# For each airline, select nb_bumped and total_passengers and sum
airline_totals = airline_bumping.groupby('airline')[['nb_bumped','total_passengers']].sum()
'''