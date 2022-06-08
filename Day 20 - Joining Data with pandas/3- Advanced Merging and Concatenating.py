# filtering joins

'''
semi join
    -returns the intersection, similar to an inner join
    -returns only tables from left table, not right table
    -no duplicates

anti join
    -returns the left table, excluding the intersection
    -returns only columns from the left table
'''

'''
#anti join
# Merge employees and top_cust
empl_cust = employees.merge(top_cust, on='srid', 
                            how='left', indicator=True)

# Select the srid column where _merge is left_only
srid_list = empl_cust.loc[empl_cust['_merge'] == 'left_only', 'srid']

# Get employees not working with top customers
print(employees[employees['srid'].isin(srid_list)])
'''

# Concatenate DataFrames together vertically

# pd.concat([x_jan, x_fab, x_march])
# pd.concat([x_jan, x_fab, x_march], ignore_index=True)
# pd.concat([x_jan, x_fab, x_march], ignore_index=False, keys=['jan','feb', 'mar])

# Concatenate DataFrames with different column names

# pd.concat([x_jan, x_fab, x_march], sort=True)
# pd.concat([x_jan, x_fab, x_march], join='inner')

'''
    Using append method instead of concat
        -supports ignore_index and sort
        -does not support keys and join -> always join=outer
'''

# x_jan.append([x_fab, x_march], ignore_index=True, sort=True)

'''
# Concatenate the tables and add keys
inv_jul_thr_sep = pd.concat([inv_jul, inv_aug, inv_sep], 
                            keys=['7Jul','8Aug','9Sep'])

# Group the invoices by the index keys and find avg of the total column
avg_inv_by_month = inv_jul_thr_sep.groupby(level=0).agg({'total':'mean'})

# Bar plot of avg_inv_by_month
avg_inv_by_month.plot(kind='bar')
plt.show()
'''

'''
validating merges
merge(validate=None)

checks if merge is specified type
'one_to_one'
'one_to_many'
'many_to_one'
'many_to_many'

tracks.merge(speck, on='id', validate='one_to_one') # merge error 
'''

'''
.concat(verify_integrity=False)
Default val is False
checks whether the new concatenated index contains duplicates
'''

'''
# Concatenate the classic tables vertically
classic_18_19 = pd.concat([classic_18, classic_19], ignore_index=True)

# Concatenate the pop tables vertically
pop_18_19 = pd.concat([pop_18, pop_19], ignore_index=True)

# Merge classic_18_19 with pop_18_19
classic_pop = classic_18_19.merge(pop_18_19, on='tid', how='inner')

# Using .isin(), filter classic_18_19 rows where tid is in classic_pop
popular_classic = classic_18_19[classic_18_19['tid'].isin(classic_pop['tid'])]

# Print popular chart
print(popular_classic)
'''