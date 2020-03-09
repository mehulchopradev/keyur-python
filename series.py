# this file houses all the library functions that help in generating mathematical series

# Module
# name -> series

def get_fibo_series(n):
    # '0 1 1 2 3 5 8 13'
    pass

def get_odd_series(n):
    # '1 3 5 7 9'
    result = ''
    for v in range(1, n + 1, 2):
        result += str(v) + ' '
    return result