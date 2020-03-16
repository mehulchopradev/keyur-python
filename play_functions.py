# it can accept variable number of arguments : 0 to n
def myadd(*args):
    # print(args) # stores all the parameters passed to the function (0 to n)
    # print(type(args)) # tuple object
    sum = 0
    for arg in args:
        sum += arg
    return sum

# positional arguments packing
print(myadd()) # 0
print(myadd(5, 4, 2)) # 11
print(myadd(5, 6, 3, 4, 7, 8, 9, 4, 5)) # 51


def area(length, breadth):
    return length * breadth

stats = (6, 3) # cud be a list too

print(area(stats[0], stats[-1]))

# factor to leverage here is that the order of the elements in the tuple (list), match
# the positional arguments order in the area function
print(area(*stats)) # positional arguments unpacking


def perimeter(**rect_stats):
    '''
    This function supports only keyword arguments, namely
    `length` and `breadth`
    '''
    # return 2 * (length + breadth)
    # print(rect_stats) # dictionary containing the keyword argument passed during function call
    # print(type(rect_stats)) # dict
    return 2 * (rect_stats['length'] + rect_stats['breadth'])

# print(perimeter(5.1, 4.9)) # this wil not work
print(perimeter(length=5.1, breadth=4.9)) # keyword arguments packing
# print(perimeter(l=5.1, b=4.9)) # this will not work as documentation of the function clearly
# states that it accepts length and breadth keyword arguments


stats_map = {'breadth': 5.4, 'length': 6.3}


print(area(stats_map['length'], stats_map['breadth']))

# factor to leverage here is that the key names of the elements in the dict, match
# the positional arguments name in the area function
print(area(**stats_map)) # keyword arguments unpacking