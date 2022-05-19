import pandas as pd
import numpy as np

# logical_and()
# logical_or()
# logical_not()


numbers = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 12, 321])

print(np.logical_and(numbers < 10,
                     numbers > 7))  # [False False False False False False False False  True  True False False False]
print(np.logical_or(numbers < 4,
                    numbers >= 2))  # [ True  True  True  True  True  True  True  True  True  True  True  True True]
print(np.logical_not(numbers > 4))  # [ True  True  True  True  True False False False False False False False False]
print(numbers[np.logical_not(numbers > 4)])  # [0 1 2 3 4]

x = 8
y = 9
print(not (True and not (y > 14 or y > 10)))
print(not (x < 3))

# Filtering DataFrames on Pandas

# pip install openpyxl
belnet_excel = pd.read_excel('belnet-subs-and-marketplace.xlsx', index_col=0)
belnet = pd.DataFrame(belnet_excel)

print(belnet)
# print(pop.columns)

#print(pop.iloc[:, [1, 3]])

print(belnet.iloc[:, [0]])
print(belnet.iloc[:, [0]] > 60)

big_parks = belnet.iloc[:, [0]] > 60
small_parks = belnet.iloc[:, [0]] <= 60
print(belnet[big_parks])

print(np.logical_not(small_parks))

'''
    # Import cars data
    import pandas as pd
    cars = pd.read_csv('cars.csv', index_col = 0)
    
    # Create car_maniac: observations that have a cars_per_cap over 500
    cpc = cars["cars_per_cap"]
    many_cars = cpc > 500
    car_maniac = cars[many_cars]
    
    # Print car_maniac
    print(car_maniac)
'''

'''
    # Import cars data
    import pandas as pd
    cars = pd.read_csv('cars.csv', index_col = 0)
    
    # Import numpy, you'll need this
    import numpy as np
    
    # Create medium: observations with cars_per_cap between 100 and 500
    cpc = cars['cars_per_cap']
    between = np.logical_and(cpc > 100, cpc < 500)
    medium = cars[between]
    
    # Print medium
    print(medium)
'''