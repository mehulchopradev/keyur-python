''' print('Program starts...')

n = input('Enter n : ')

ni = int(n)

print('Odd') if ni % 2 else print('Even')

print('Program ends!') '''

# Python env -> play_input -> int('mehul') -> ValueError and raise it to its caller -> play_input ->
# since no handling, ValueError will be raised to the caller of play_input -> Python env ->
# It prints the traceback (info about the error)


# Python env -> play_input -> int('mehul') -> ValueError and raise it to its caller -> play_input ->
# Handle the error

from traceback import print_exc

print('Program starts...')

n = input('Enter n : ')

try:
    ni = int(n) # ni (module)
except ValueError:
    print('Please enter integer values')
    print_exc() # prints the exception stack trace
else:
    # will execute if the corresponding try block is successful i.e. does not raise
    # any exception
    print('Odd') if ni % 2 else print('Even')

print('Program ends!')