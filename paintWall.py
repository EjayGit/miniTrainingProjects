# TODO
import math

height = int(input("Enter height of wall: "))
width = int(input("Enter width of wall: "))

def number_of_cans(height, width, coverage):
    area = height * width
    num_cans = math.ceil(area / coverage)
    print(num_cans)

number_of_cans(height, width, 4)