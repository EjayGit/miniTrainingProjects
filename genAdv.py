import time

def isDivided(num):
    if num % 555 == 0:
        return True 
    return False

print(isDivided(555))

def infiniteDivision():
    num = 0
    while True:
        if isDivided(num):
            i = (yield num)
            if i is not None:
                num = i
        num += 1


gen_ob = infiniteDivision()
for i in gen_ob:
    print(i)
    time.sleep(3)
    digits = len(str(i))
    gen_ob.send(10**(digits))