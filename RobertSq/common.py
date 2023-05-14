from datetime import date

class TransactionData:
    def __init__(self, transaction_date, reason, amount):
        self.transaction_date = transaction_date
        self.reason = reason
        self.amount = amount

    def __str__(self):
        return f'{self.transaction_date}\t {self.amount}\t {self.reason}'


class MaintenanceData:
    def __init__(self):
        self.data = [TransactionData(reason='ROBSQMAINTENANCE , '
                                               'ROBERTSQUAREFLAT10, VIA ONLINE - PYMT , FP 24/06/21 10 , 07102023552324000N',
                                        amount=150, transaction_date=date(2021, 6, 24)),
                     TransactionData(reason='ROBSQMAINTENANCE , '
                                          'ROBERTSQUAREFLAT10, VIA ONLINE - PYMT , FP 25/06/21 10 , 54084755180580000N',
                                   amount=369.14, transaction_date=date(2021, 6, 25)),
                     TransactionData(reason='ROBSQMAINTENANCE , '
                                          'ROBERTSQUAREFLAT10, VIA ONLINE - PYMT , FP 19/01/22 10 , 06140634182600000N',
                                   amount=492.61, transaction_date=date(2022, 1, 19)),
                     TransactionData(reason='ROBSQMAINTENANCE , '
                                          'ROBERTSQUAREFLAT10, VIA ONLINE - PYMT , FP 19/01/22 10 , 43140408329965000N',
                                   amount=166.06, transaction_date=date(2022, 1, 19)),
                     TransactionData(reason='ROBSQMAINTENANCE , '
                                          'ROBERTSQUAREFLAT10, VIA ONLINE - PYMT , FP 07/07/22 10 ,05082747548973000N',
                                   amount=150, transaction_date=date(2022, 7, 7)),
                     TransactionData(reason='REGENTROBSQMAINT , '
                                          '051-01-010A , VIA ONLINE - PYMT , FP 19/07/22 10 , 49103540908729000N',
                                   amount=487.08, transaction_date=date(2022, 7, 19))
                   ]

    def sum(self):
        sum_amount = sum(data.amount for data in self.data)
        return round(sum_amount, 2)

    def __str__(self):
        return '\n'.join(str(data) for data in self.data)
