try:  # try codes inline
    print(213231)
except:  # if error occurred run this codes
    print("2")
#except TypeError: # we can also expect error type
#    print('3')
else:  # if error did not occurred run this codes
    print("3")
finally:  # run this code anyway
    print("4")


#except TypeError: # we can also expect error type
#    print('3')

#short way of itt

try:
    pront()
except Exception as e:
    print(e)