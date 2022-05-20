'''
    What is the point of pandas
     -Data manipulation skill track
     -Data visualization skill track

    Chapter 1 DataFrames
        -sorting and subsetting
        -creating a new column

    Chapter 2 Aggregating Data
        -Summary statistics
        -Counting
        -Grouped summary statistics

    Chapter 3 Slicing and Indexing Data
        -Subsetting using slicing
        -Indexes and subsetting using indexes

    Chapter 4 Creating and Visualizating Data
        -Plotting
        -Handling Missing Data
        -Reading data into a DataFrame

    *pandas built in numpy and matplotlib

    Exploring DataFrame
        - .head() returns first few rows
        - .info() displays name of columns, data type they contain, whether they have any missing values
        - .shape row,column returns ex: (3,4)
        - .describe() computes some summary statistical values for numeric columns, like mean and median
        - .values
        - .columns
        - .index
'''

import pandas as pd

netflix_data_csv = pd.read_csv('netflix_data.csv')
netflix_df = pd.DataFrame(netflix_data_csv)

print(netflix_df.head())
print(netflix_df.info())
print(netflix_df.describe())
print(netflix_df.shape)
print(netflix_df.values)
print(netflix_df.columns)
print(netflix_df.index)

print(netflix_df[:5])
print(netflix_df.sort_values('genre')[:5])
print(netflix_df.sort_values('genre', ascending=False)[:5])
print(netflix_df.sort_values(['genre', 'show_id'], ascending=[False, True])[:5]) # first sort genre later sort show_id

is_drama = netflix_df['genre'] == "Dramas"
is_action = netflix_df['genre'] == "Action"

print(netflix_df[is_drama | is_action])

is_drama_or_action = netflix_df['genre'].isin(["Dramas", "Action"])

print(netflix_df[is_drama_or_action])

netflix_df["new_show_id"] = netflix_df["show_id"] + 'new'
print(netflix_df.head())
# Adding a new column

'''
    # Create indiv_per_10k col as homeless individuals per 10k state pop
    import numpy as np
    import pandas as pd
    homelessness["indiv_per_10k"] = 10000 * (np.array(homelessness['individuals']) / (np.array(homelessness['state_pop'])))
    
    # Subset rows for indiv_per_10k greater than 20
    high_homelessness = homelessness[homelessness["indiv_per_10k"] > 20]
    
    # Sort high_homelessness by descending indiv_per_10k
    high_homelessness_srt = high_homelessness.sort_values('indiv_per_10k', ascending=False)
    
    # From high_homelessness_srt, select the state and indiv_per_10k cols
    result = high_homelessness_srt[['state', 'indiv_per_10k']]
    
    # See the result
    print(result)
'''