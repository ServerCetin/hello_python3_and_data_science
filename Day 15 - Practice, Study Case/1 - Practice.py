import numpy as np
import pandas as pd

# house list of lists
house = [["hallway", 11.25],
         ["kitchen", 18.0],
         ["living room", 20.0],
         ["bedroom", 10.75],
         ["bathroom", 9.50]]

# Build a for loop from scratch
for a, [x, y] in enumerate(house):
    print("the " + str(x) + " is " + str(y) + " sqm")

world = {"afghanistan": 30.55,
         "albania": 2.77,
         "algeria": 39.21}

for k, v in world.items():
    print(k + "--" + str(v))


np_height = np.array([1.73, 1.68, 1.71, 1.89, 1.79])
np_weight = np.array([65.4, 59.2, 63.6, 88.4, 68.7])
meas = np.array([np_height, np_weight])

for val in np.nditer(meas): # np.nditer()  => x.item()
    print(val)

print('=================================================')


belnet_excel = pd.read_excel('belnet-subs-and-marketplace.xlsx', index_col=0)

for index, row in belnet_excel.iterrows():
    print(index)
    print(row)

for year, row in belnet_excel.iterrows():
    print(f'{index} : {row.iloc[1]}')


for lab, row in belnet_excel.iterrows() :
    # - Creating Series on every iteration
    belnet_excel.loc[lab, "Number Count"] = len(str(row.iloc[1]))
print(belnet_excel)


# Code for loop that adds COUNTRY column
for lab, row in belnet_excel.iterrows() :
    belnet_excel.loc[lab, "TEXTUPPER"] = row["Text"].upper()

print(belnet_excel)

belnet_excel["text_length"] = belnet_excel["TEXTUPPER"].apply(len) # same code but one line
print(belnet_excel)
# .apply(str.upper)