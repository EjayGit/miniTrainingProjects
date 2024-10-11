import sys
import cProfile

square_ge = (num**2 for num in range(1,5000))
square_lc = [num**2 for num in range(1,5000)]

print(cProfile.run("max((num**2 for num in range(1,5000)))"))
print(cProfile.run("max([num**2 for num in range(1,5000)])"))