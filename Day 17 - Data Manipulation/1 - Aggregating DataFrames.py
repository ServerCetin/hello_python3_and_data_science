import pandas as pd

belnet_excel = pd.read_excel('belnet-subs-and-marketplace.xlsx', index_col=0)
belnet = pd.DataFrame(belnet_excel)

print(belnet)

'''
    Summarizing numerical data
    .median() .mode() .min() .max() .var() .std() .sum() .quantile()
'''

print(belnet.iloc[:, 0].mode())
print(belnet.iloc[:, 0].std())

print(belnet.iloc[:, 0].min())
print(belnet.iloc[:, 0].max())
print(belnet.iloc[:, 0].quantile(0.3))  # computes thirtieth percentile tile of DataFrame


def pct30(column):
    return column.quantile(0.3)


def pct50(column):
    return column.quantile(0.5)

#The .agg() method allows you to apply your own custom functions to a DataFrame, as well as apply functions to more than
#one column of a DataFrame at once, making your aggregations super-efficient.
print(belnet.iloc[:, 0].agg(pct30))

print(belnet.iloc[:, 0:2].agg(pct30))
print(belnet.iloc[:, 0:2].agg([pct30, pct50]))

print(belnet.iloc[:, 0].sum())
print(belnet.iloc[:, 0].count())

print(
    belnet.iloc[:, 0].cumsum())  # cumulative sum: returns not just a number, but a number for each row of the DataFrame
# 2007 first 2008 first + second index and so on

''' cumulative statistics
    .cummax()
    .cummin()
    .cumprod() : cumulative product    
'''

# vet_visits.drop_duplicates(subset="name")
# unique_dogs = vet_visits.drop_duplicates(subset=["name" , "breed"])
# unique_dogs["breed"].value_counts()
# unique_dogs["breed"].value_counts(sort=True)
# unique_dogs["breed"].value_counts(normalize=True) # proportion

'''
# Count the number of stores of each type
store_counts = store_types["type"].value_counts(sort=True)
print(store_counts)

# Get the proportion of stores of each type
store_props = store_types["type"].value_counts(normalize=True)
print(store_props)

# Count the number of each department number and sort
dept_counts_sorted = store_depts['department'].value_counts(sort=True)
print(dept_counts_sorted)

# Get the proportion of departments of each number and sort
dept_props_sorted = store_depts['department'].value_counts(sort=True, normalize=True)
print(dept_props_sorted)
'''

'''
dogs[dogs["color"] == "White"]["weight_kg"].mean()
dogs[dogs["color"] == "Red"]["weight_kg"].mean()
...
...
... => dogs.groupby("color")["weight_kg"].mean()

dogs.groupby("color")["weight_kg"].agg([min, max, sum])
dogs.groupby(["color","breed"])["weight_kg"].mean()
dogs.groupby(["color","breed"])[["weight_kg","height_cm"]].mean()
'''

'''
# Calc total weekly sales
sales_all = sales["weekly_sales"].groupby()

# Subset for type A stores, calc total weekly sales
sales_A = sales[sales["type"] == "A"]["weekly_sales"].groupby()

# Subset for type B stores, calc total weekly sales
sales_B = sales[sales["type"] == "B"]["weekly_sales"].groupby()

# Subset for type C stores, calc total weekly sales
sales_C = sales[sales["type"] == "C"]["weekly_sales"].groupby()

# Get proportion for each type
sales_propn_by_type = [sales_A, sales_B, sales_C] / sales_all
print(sales_propn_by_type)
'''

'''
# Calc total weekly sales
sales_all = sales["weekly_sales"].sum()

# Subset for type A stores, calc total weekly sales
sales_A = sales[sales["type"] == "A"]["weekly_sales"].sum()

# Subset for type B stores, calc total weekly sales
sales_B = sales[sales["type"] == "B"]["weekly_sales"].sum()

# Subset for type C stores, calc total weekly sales
sales_C = sales[sales["type"] == "C"]["weekly_sales"].sum()

# Get proportion for each type
sales_propn_by_type = [sales_A, sales_B, sales_C] / sales_all
print(sales_propn_by_type)


# Import numpy with the alias np
import numpy as np

# For each store type, aggregate weekly_sales: get min, max, mean, and median
sales_stats = sales.groupby('type')['weekly_sales'].agg([np.min,np.max, np.mean, np.median])

# Print sales_stats
print(sales_stats)

# For each store type, aggregate unemployment and fuel_price_usd_per_l: get min, max, mean, and median
unemp_fuel_stats = sales.groupby('type')[['unemployment','fuel_price_usd_per_l']].agg([np.min,np.max, np.mean, np.median])

# Print unemp_fuel_stats
print(unemp_fuel_stats)
'''

#grouping by pivot table = by default pivot table takes the mean value for each group

# dogs.groupby("color")["weight_kg"].mean()
# dogs.pivot_table(values="weight_kg", index="color")
# dogs.pivot_table(values="weight_kg" , index="color" , aggfunc=np.median)
# dogs.pivot_table(values="weight_kg" , index="color" , aggfunc=[np.mean, np.median])

# dogs.groupby(["color","breed"])["weight_kg"].mean()
# Pivot on two variables
# dogs.pivot_table(values="weight_kg" , index="color" , columns="breed")

# Filling missing values in pivot tables
# dogs.pivot_table(values="weight_kg" , index="color" , columns="breed" , fill_value=0)

# Summing with pivot tables
# dogs.pivot_table(values="weight_kg" , index="color" , columns="breed" , fill_value=0, margins=True)