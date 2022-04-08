# Set is a collection of items. Let me take you back to your elementary or high school Mathematics lesson.
# The Mathematics definition of a set can be applied also in Python. Set is a collection of unordered
# and un-indexed distinct elements. In Python set is used to store unique items, and it is possible
# to find the union, intersection, difference, symmetric difference, subset, super set and disjoint set among sets.

# syntax
st = {}
# or
st = set()

# same methods like list

# Adding Items to a Set
st = {'item1', 'item2', 'item3', 'item4'}
st.add('item5')

# Add multiple items using update() The update() allows to add multiple items to a set.
# The update() takes a list argument.

st = {'item1', 'item2', 'item3', 'item4'}
st.update(['item5', 'item6', 'item7'])

st = {'item1', 'item2', 'item3', 'item4'}
st.remove('item2')

# Converting List to Set
lst = ['item1', 'item2', 'item3', 'item4', 'item1']
st = set(lst)  # {'item2', 'item4', 'item1', 'item3'} - the order is random, because sets in general are unordered

# Joining Sets
st1 = {'item1', 'item2', 'item3', 'item4'}
st2 = {'item5', 'item6', 'item7', 'item8'}
st3 = st1.union(st2)

st1 = {'item1', 'item2', 'item3', 'item4'}
st2 = {'item5', 'item6', 'item7', 'item8'}
st1.update(st2)  # st2 contents are added to st1

st1 = {'item1', 'item2', 'item3', 'item4'}
st2 = {'item3', 'item2'}
st1.intersection(st2)  # {'item3', 'item2'}

st1 = {'item1', 'item2', 'item3', 'item4'}
st2 = {'item2', 'item3'}
st2.issubset(st1)  # True
st1.issuperset(st2)  # True

st1 = {'item1', 'item2', 'item3', 'item4'}
st2 = {'item2', 'item3'}
st2.difference(st1)  # set()
st1.difference(st2)  # {'item1', 'item4'} => st1\st2

# Finding Symmetric Difference Between Two Sets
# It returns the the symmetric difference between two sets. It means that it returns a set that contains all items
# from both sets, except items that are present in both sets, mathematically: (A\B) ∪ (B\A)
st1 = {'item1', 'item2', 'item3', 'item4'}
st2 = {'item2', 'item3'}
# it means (A\B)∪(B\A)
st2.symmetric_difference(st1) # {'item1', 'item4'}

#If two sets do not have a common item or items we call them disjoint sets. We can check if two sets are joint or
# disjoint using isdisjoint() methodjoi.

st1 = {'item1', 'item2', 'item3', 'item4'}
st2 = {'item2', 'item3'}
st2.isdisjoint(st1) # False