import pandas as pd

belnet_excel = pd.read_excel('belnet-subs-and-marketplace.xlsx')
belnet_df = pd.DataFrame(belnet_excel)

# Setting a column as the index

print(belnet_df)

belnet = belnet_excel.set_index('Yıl')
print(belnet)

# Removing an index
# belnet.reset_index()

# Dropping an index
# dogs_ind.reset_index(drop=True)

# Indexes make subsetting simpler
# dogs[dogs["name"].isin(["Bella","Stella"])]
# dogs_ind.loc[["Bella","Stella"]]
# Index values don't need to be unique
print(belnet.loc[2009])

# Multi-level indexes a.k.a. hierarchical indexes
belnet2 = belnet_excel.set_index(['Yıl', 'Text'])
print(belnet2)

# Subset the outer level with a list
print(belnet2.loc[[2007, 2008]])

# Subset inner levels with a list of tuples
print(belnet2.loc[[(2007, 'ttales'), (2008, 'kadam')]])

# Sorting by index values
belnet2.sort_index()

# Controlling sort_ index
belnet2.sort_index(level=['Yıl','Text'], ascending=[True,False])

'''
Now you have two problems
- Index values are just data
- Indexes violate "tidy data" principles
- You need to learn two syntaxes
'''

'''
# Make a list of cities to subset on
cities = ["Moscow", "Saint Petersburg"]

# Subset temperatures using square brackets
print(temperatures[temperatures['city'].isin(cities)])

# Subset temperatures_ind using .loc[]
print(temperatures_ind.loc[cities])
'''

'''
# Index temperatures by country & city
temperatures_ind = temperatures.set_index(['country', 'city'])

# List of tuples: Brazil, Rio De Janeiro & Pakistan, Lahore
rows_to_keep = [
    ('Brazil', 'Rio De Janeiro'), 
    ('Pakistan','Lahore')
    ]

# Subset for rows to keep
print(rows_to_keep)
print(temperatures_ind.loc[rows_to_keep])
'''

'''
# Sort temperatures_ind by index values
print(temperatures_ind.sort_index())

# Sort temperatures_ind by index values at the city level
print(temperatures_ind.sort_index(level='city'))

# Sort temperatures_ind by country then descending city
print(temperatures_ind.sort_index(level=['country','city'], ascending=[True,False]))
'''

# Slicing the outer index level
print(belnet2)
print(belnet2.loc['2007':'2010'])
print(belnet2.loc[('2007','ttales'):('2010','melka')])

print(belnet2.iloc[:,0:2])

# Slicing by partial dates
# # Get dogs with date _ of _ birth between 2014-08-25 and 2016-09-16
# dogs.loc["2014-08-25":"2016-09-16"]
# dogs.loc["2014":"2016"]

'''
# Subset rows from India, Hyderabad to Iraq, Baghdad
print(temperatures_srt.loc[('India', 'Hyderabad'): ('Iraq','Baghdad')])

# Subset columns from date to avg_temp_c
print(temperatures_srt.loc[:,'date':'avg_temp_c'])

# Subset in both directions at once
print(temperatures_srt.loc[('India', 'Hyderabad'): ('Iraq','Baghdad'),'date':'avg_temp_c'])
'''

'''
# Use Boolean conditions to subset temperatures for rows in 2010 and 2011
temperatures_bool = temperatures[(temperatures['date'] >= '2010') & (temperatures['date'] <= '2011-12-31')]
print(temperatures_bool)

# Set date as the index and sort the index
temperatures_ind = temperatures.set_index('date').sort_index()

# Use .loc[] to subset temperatures_ind for rows in 2010 and 2011
print(temperatures_ind.loc['2010-01-01':'2011-12-31'])

# Use .loc[] to subset temperatures_ind for rows from Aug 2010 to Feb 2011
print(temperatures_ind.loc['08-2010':'02-2011'])
'''

# working with pivot
belnet_piv = belnet_df.pivot_table(values='Şube Sayısı', index='Yıl', columns='Text')
print(belnet_piv)
print(belnet_piv.mean(axis='index'))
print(belnet_piv.mean(axis='columns'))

'''
# Add a year column to temperatures
temperatures["year"] = temperatures["date"].dt.year

# Pivot avg_temp_c by country and city vs year
temp_by_country_city_vs_year = temperatures.pivot_table("avg_temp_c", index = ["country", "city"], columns = "year")

# See the result
print(temp_by_country_city_vs_year)
'''

'''
# Get the worldwide mean temp by year
mean_temp_by_year = temp_by_country_city_vs_year.mean()

# Filter for the year that had the highest mean temp
print(mean_temp_by_year[mean_temp_by_year == mean_temp_by_year.max()])

# Get the mean temp by city
mean_temp_by_city = temp_by_country_city_vs_year.mean(axis="columns")

# Filter for the city that had the lowest mean temp
print(mean_temp_by_city[mean_temp_by_city == mean_temp_by_city.min()])
'''