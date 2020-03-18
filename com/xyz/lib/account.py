from .min_bal_error import MinBalError

class Account:
    def __init__(self, acc_name, acc_type, acc_balance):
        self.acc_name = acc_name
        self.acc_type = acc_type
        self.acc_balance = acc_balance

    def withdraw(self, amt):
        print('Transaction starts...')

        try:
            if amt <= 0:
                raise ValueError('Amt to withdraw must be a non zero positive value')
            if self.acc_balance - amt < 1000:
                # raise an error to the caller
                # raise Exception('Min balance not being maintained')
                raise MinBalError('Min balance not being maintained')

            self.acc_balance -= amt
            return self.acc_balance
        finally:
            # will execute always
            # let there be an exception being raised in the corresponding try block
            # or no exception being raised

            # eg. statements like closing connection to server, closing connection to file system
            print('Transaction ends!')