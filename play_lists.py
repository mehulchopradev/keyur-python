nos = [4, 5, 5, 10, 1, 6, 8, 8, 10, 1, 3]

# build a new list which contains the odd pointers from the nos list
# filtering
''' odds = []
for n in nos:
    if n % 2:
        odds.append(n) '''

# for comprehensions
# Pre requisite : should need a new list
odds = [n for n in nos if n % 2]
print(odds)

# build a new list that contains even elements greater than 5 from the nos list
# filtering
evens = [n for n in nos if (not n % 2) and n > 5]
print(evens)

# build a new list which contains all elements from nos list, but with marks deducted by 1
# mapping
deducted_marks = [n - 1 for n in nos]
print(deducted_marks)