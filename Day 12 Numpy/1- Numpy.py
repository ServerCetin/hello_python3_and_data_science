'''
        # Numpy

- Numeric Python
- Alternative array to Pthon array: Numpy Array
- Calculations overy entire array

pip3 install numpy
'''

import numpy as np

weight = [52, 51, 66, 71, 67, 123]
height = [1.56, 1.47, 1.66, 1.81, 1.75, 2]

np_weight = np.array(weight)
np_height = np.array(height)
print(np_weight)
print(np_height)

## weight / height ** 2 syntax error
bmi = np_weight / np_height ** 2
print(bmi)

# np arrays can contain one data type
# x = np.array('x',12,23.4,True) # TypeError


python_list = [1, 2, 3]
numpy_array = np.array([1, 2, 3])

python_list + python_list  # [1, 2, 3, 1, 2, 3]
numpy_array + numpy_array  # array([2, 4, 6])

print(bmi)  # [21.36752137 23.60127725 23.95122659 21.67211013 21.87755102 30.75      ]
print(bmi > 22)  # [False  True  True False False  True]
print(bmi[bmi > 21.7])  # [23.60127725 23.95122659 21.87755102 30.75      ]

# 2D NUMPY ARRAYS

print(type(np_height))  # np_height_in[100:111] => n-dimensional array

np_2d = np.array([[1.73, 1.68, 1.71, 1.89, 1.79],
                  [65.4, 59.2, 63.6, 88.4, 68.7]])

print(np_2d.shape)  # (2, 5) 2 row 5 column
np_2d[0, 3]  # np_2d[0][3]

print(np_2d[:, 1:4])
# [[ 1.68  1.71  1.89]
# [59.2  63.6  88.4 ]]

print(np_2d[1, :])  # [65.4 59.2 63.6 88.4 68.7]

np_mat = np.array([[1, 2],
                   [3, 4],
                   [5, 6]])

np_mat * 2  # array([[ 2,  4],[ 6,  8],[10, 12]])

# Numpy Statistics
np_city = np.array([[1.64, 71.78],
                    [1.37, 63.35],
                    [1.6, 55.09],
                    [2.04, 74.85],
                    [2.04, 68.72],
                    [2.01, 73.57]])

mean_val = np.mean(np_city[:, 0])  # all member sums / count
print(np_city[:, 0])  # [1.64 1.37 1.6  2.04 2.04 2.01]
print(mean_val)  # 1.7833333333333332

median_val = np.median(np_city[:, 0])
print(median_val)  # middle val, if 2 mid child sums/2

print(np.corrcoef(np_city[:, 0], np_city[:, 1]))  # Function that returns a matrix of
# correlations of x with x, x with y, y with x and y with y. # TODO: I will check this out later

print(np.std(np_city[:, 0]))  # standart deviation 0.2608107018935807

# .sum() .sort() in numpy calculations faster because array has 1 type of data

'''
# heights and positions are available as lists

# Import numpy
import numpy as np

# Convert positions and heights to numpy arrays: np_positions, np_heights
np_positions = np.array(positions)
np_heights = np.array(heights)


# Heights of the goalkeepers: gk_heights
goalkeepers_indexes = np.array(np_positions == 'GK')
#print(goalkeepers_indexes)
#print(np_heights[goalkeepers_indexes])
gk_heights = np_heights[goalkeepers_indexes]

# Heights of the other players: other_heights
other_indexes = np_positions != 'GK'
other_heights = np_heights[other_indexes]

# Print out the median height of goalkeepers. Replace 'None'
print("Median height of goalkeepers: " + str(np.median(gk_heights)))

# Print out the median height of other players. Replace 'None'
print("Median height of other players: " + str(np.median(other_heights)))
'''
