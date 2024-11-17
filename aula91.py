# Toda função que tem o yield é uma Generator function

def generator(n=0, maximum = 10):
    while True:
        yield n
        n += 1
        if n > maximum:
            return
        

gen = generator()
for n in gen:
    print(n)