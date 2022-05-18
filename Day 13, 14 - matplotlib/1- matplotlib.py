'''
    Data visualization is very important in data science
        -explore data
        -report insights

    There are many packages for data visualization but matplotlib is mather of them all
    we need subpackage of it, pyplot

'''

import matplotlib.pyplot as plt

year = [1950, 1970, 1990, 2010]
population = [2.519, 3.692, 5.263, 6.972]

plt.plot(year, population)  # (x,y) creates a graph with connected lines
plt.show()  # shows the graph in plots

plt.scatter(year, population)  # (x,y) creates a graph with only dots
plt.show()  # shows the graph in plots

plt.xscale('log')  # to display x horizon logarithmically

'''
    Histogram 
        is type of visualization that's very useful to explore data

    help(plt.hist)
    
    # Build histogram with 5 bins
    plt.hist(array, bins=5)
    
    # Show and clean up plot
    plt.show()
    plt.clf()
'''

values = [0, 0.6, 1.4, 1.6, 2.2, 2.5, 2.6, 3.2, 3.5, 3.9, 4.2, 6]
plt.xscale('linear') # we returned default value (set log before)
plt.hist(values, bins=3)
plt.show()

