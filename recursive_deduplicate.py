#Recursively removes all adjacent duplicate letters from a string.
#EG input: AABBCCDD output: ABCD

def recursive_deduplicate(my_str, i=0):
    if len(my_str) <= 1 or i == len(my_str)-1:
        return my_str
    else:
        if my_str[i] == my_str[i+1]:
            return recursive_deduplicate(my_str[0:i]+my_str[i+1:],i)
        else:
            return recursive_deduplicate(my_str, i+1)

print(recursive_deduplicate("aaaa"))
print(recursive_deduplicate("aaba"))
print(recursive_deduplicate("apple"))
print(recursive_deduplicate(""))