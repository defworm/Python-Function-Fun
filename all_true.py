#Returns True if all the elements in an iterable are true. 

def all_true(iter):
    return all(iter)

print(all_true([True, True, True]))
print(all_true((True, False)))