#Returns True if one of the elements in an iterable is true.

def one_true(iter):
    return any(iter)

print(one_true([True, True, True]))
print(one_true([False, False, False]))
print(one_true((True, False)))