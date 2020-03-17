class Account:
    def __init__(self, acc_name, acc_type, acc_balance):
        self.acc_name = acc_name
        self.acc_type = acc_type
        self.acc_balance = acc_balance

    def withdraw(self, amt):
        if self.acc_balance - amt < 1000:
            # raise an error to the caller
            raise Exception('Min balance not being maintained')

        self.acc_balance -= amt
        return self.acc_balance