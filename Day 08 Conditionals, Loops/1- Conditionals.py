# Too bad I could not study Python for 4 days. We have been preparing for a study case competition
# We came 3rd in the competition, that was good experience

nmbr = 3

if nmbr % 2 == 0:
    print("%d is even" % nmbr)
elif nmbr == 0:
    print("%d is zero" % nmbr)
else:
    print("%d is odd" % nmbr)

free = "free";

print("I am free") if free == "free" else print("I am not free")

# Nested Conditions

nmbr = 4

if nmbr % 2 == 0:
    if nmbr % 4 == 0:
        print("I can pass all the condititions!")

if nmbr > 0 and nmbr % 1 == 0:
    print("Vow I can pass here too!")

