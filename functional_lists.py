nos = [5, 6, 4, 5, 6, 10, 4, 3, 7, 8]

# get a new list which has all the odd nos greater than or equal to 5 from the nos list
# filtering
# no looping and being functional

# l = filter (function, iterable - list)

# lower order function
def odd_more_than_equal_5(element):
    return element % 2 and element >= 5
ans = list(filter(odd_more_than_equal_5, nos))
print(ans)

# get a new list which has the marks from the nos list but deducted by 1
# mapping
# no looping

# l = map(function, iterable)

# lower order function
def deduct_by_1(element):
    return element - 1
a = list(map(deduct_by_1, nos))
print(a)

# Lambda functions (lambda expressions)
# Functions with only one expression in their body can be written as lambda functions

print(list(filter(lambda element: element % 2 and element >= 5, nos)))
print(list(map(lambda element: element - 1, nos)))