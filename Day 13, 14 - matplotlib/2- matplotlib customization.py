'''
    we can change colors, shapes, axes, labels and so on.

    the choice depends on
        -data
        -story we want to tell
'''

import matplotlib.pyplot as plt

year = [1999, 2002, 2004, 2008, 2014, 2023]
population = [14.132, 27.532, 34.862, 76.231, 102.532, 202.132]

# year = year + [2044, 2099]
# population = population + [41.244, 0]
# plt.scatter(gdp_cap, life_exp, s = np_pop) #

plt.plot(year, population)
plt.scatter(year, population, s=[12, 23, 44, 15, 124,12]) # c= color, alpha=0.8

plt.title('Population of Python Republic')
plt.xlabel('Year')
plt.ylabel('Population')

# plt.yticks([0, 25, 50, 100, 150, 175, 200])
plt.yticks([0, 25, 50, 100, 150, 200],
           ['Zero', 'Little', 'Hmmm', 'Good', 'Vow', 'OMG'])

# Additional customizations
plt.text(1999, 25.132, 'Hey yo!')
plt.text(2008, 102.532, 'I am here')

plt.grid(True)

plt.show()
