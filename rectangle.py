# User defined functions
def perimeter_rectangle(length, breadth):
    return 2 * (length + breadth)

def area_rectangle(length, breadth):
    return length * breadth

# l, b = 6, 4 # multiple variable initialization
l = int(input('Enter length: '))
b = int(input('Enter breadth: '))

p = perimeter_rectangle(length=l, breadth=b)
a = area_rectangle(length=l, breadth=b)

# Built in functions (BIFs)
print(p)
print(a)