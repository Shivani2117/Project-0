from model.account import Account
class TempDBAccount:

    accounts = {
        1: Account(client_id=0, account_id=0, account_type="Withdraw", amount=2000),
        2: Account(client_id=1, account_id=1, account_type="Withdraw", amount=7000),
        3: Account(client_id=2, account_id=2, account_type="Withdraw", amount=29000)
    }
