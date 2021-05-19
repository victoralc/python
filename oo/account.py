class Account:

    def __init__(self, number, owner, balance, limit):
        self.__number = number
        self.__owner = owner
        self.__balance = balance
        self.__limit = limit
        print("Creating object... {}".format(self))

    def deposit(self, amount):
        self.__balance += amount

    def withdraw(self, amount):
        if self.__can_withdraw(amount):
            self.__balance -= amount
        else:
            print("Limit reached {}. Cannot withdraw this value".format(self.__limit))

    def __can_withdraw(self, amount_wanted):
        return amount_wanted <= (self.balance + self.limit)

    def account_summary(self):
        print("Your balance {}".format(self.__balance))

    def transfer_to(self, amount, target_account):
        self.withdraw(amount)
        target_account.withdraw(amount)

    @property
    def balance(self):
        return self.__balance

    @property
    def account_owner(self):
        return self.__owner

    @property
    def limit(self):
        return self.__limit

    @limit.setter
    def limit(self, limit):
        self.__limit = limit

    def __repr__(self):
        return "Account[number:{}, titular:{}, balance:{}, limit:{}]"\
            .format(self.__number, self.__owner, self.__balance, self.__limit)

    @staticmethod
    def bank_code():
        return "001"

    @staticmethod
    def bank_codes():
        return {'BB': '001', 'Caixa': '104', 'Bradesco': '237'}
