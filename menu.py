'''
1. Fibonacci series\n
2. Odd series\n
3. Even or Odd\n
4. Factorial\n
5. Exit
Please enter ur choice: 1
Enter n: 8
0 1 1 2 3 5 8 13
1. Fibonacci series
2. Odd series
3. Even or Odd
4. Factorial\n
5. Exit
Please enter ur choice: 2
Enter n: 10
1 3 5 7 9
1. Fibonacci series
2. Odd series
3. Even or Odd
4. Factorial\n
5. Exit
Please enter ur choice: 3
Enter n: 7
Odd
1. Fibonacci series
2. Odd series
3. Even or Odd
4. Factorial\n
5. Exit
Please enter ur choice: 4
Enter n: 4
24
1. Fibonacci series
2. Odd series
3. Even or Odd
4. Factorial\n
5. Exit
Please enter ur choice: 5
'''

# Module
# name -> menu

# Importing a module
# import series as se
# import math
# import com.xyz.lib.math
# above in no ways we have imported the functions from the modules

# Importing the functions directly from the module
from series import get_fibo_series as fibo, get_odd_series
# from math import even_odd
from com.xyz.lib.math import even_odd
from math import factorial

# Module namespace collision
# Packages
# 1 Organize project structure
# 2.Avoids module namespace collision
# Google -> google.com -> com.google.<<app specific folder structure>>

# Environment variables
# PYTHONPATH - list of all the paths to check for built in modules as well as user defined modules
    # 1. Current directory
    # 2. Built in modules list of python

while True:
    # print('1. Fibonacci series\n2. Odd series\n3. Even or Odd\n4. Factorial\n5. Exit')
    print('1. Fibonacci series', '2. Odd series', '3. Even or Odd', '4. Factorial', '5. Exit', sep='\n')
    choice = int(input('Please enter ur choice: '))

    if choice == 5:
        break # forcefully break out of the enclosing loop

    if choice == 1 or choice == 2 or choice == 3 or choice == 4:
        n = int(input('Enter n: '))

    if choice == 1:
        # fibo series using n
        # series.get_fibo_series(n)
        # get_fibo_series(n)
        print(fibo(n))
        # pass # allows to have empty blocks in python
    elif choice == 2:
        # odd series using n
        # series.get_odd_series(n)
        print(get_odd_series(n))
        # pass
    elif choice == 3:
        # even or odd using n
        # com.xyz.lib.math.even_odd(n)
        print(even_odd(n))
        # pass
    else:
        print(factorial(n))

# In python the scope of a variable is
    # The entire module
    # Function

# Other languages usually have a block scope.
# if, else, loops, classes, all blocks create a scope.
# the same is not true in python