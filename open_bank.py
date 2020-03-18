from com.xyz.lib.account import Account
from traceback import print_exc

a1 = Account('mehul chopra', 'Savings', 9000)

try:
    ub = a1.withdraw(9000)
except ValueError:
    print('Enter right amount to withdraw')
except Exception:
    print_exc()
else:
    print(ub)