#accepts any number of named arguments and prints them in the pattern key : value one at a time

def name_args(**kwargs):
    for k in kwargs.keys():
        print(f"{k}:{kwargs[k]}")

name_args(name="Randon", weather="sunny", location="park", time=3)