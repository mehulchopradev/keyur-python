n = int(input('Enter n: '))

# i = 0

# while loop
'''
while <<expression that evaluates to True/False as understood by python>>:
    I1
    I2
    I3
'''

''' while i <= n:
    if i % 2:
        print(i)
    i = i + 1 '''

# for loop
'''
for v in <<sequence of elements>>:
    I1
    I2
    I3

Sequence of elements | Iterations
10  | 10 times
40 | 40 times
0 | 0 times

[5, 6, 7, 8, 9]
1st iteration - v - 5
2nd iteration - v - 6 
'''

# [0-n]
# n = 8 : [0-8]
# n = 5 : [0-5]
# range()
# start: 0 stop: n + 1 - [0, n+1-1]
# step=1

''' for v in range(0, n+1):
    if v % 2:
        print(v) '''

for v in range(1, n + 1, 2):
    print(v)