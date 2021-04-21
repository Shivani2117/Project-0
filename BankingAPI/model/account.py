class Account:

    def __init__(self, client_id=0, account_id=0, account_type="", amount=0):
        self.client_id = client_id
        self.account_id = account_id
        self.account_type = account_type
        self.amount = amount

    def json(self):
        return {
            'clientId': self.client_id,
            'accountId': self.account_id,
            'account_type': self.account_type,
            'amount': self.amount
        }

    @staticmethod
    def json_parse(json):
        account = Account()
        account.client_id = json["clientId"]
        account.account_id = json["accountId"]
        account.account_type = json["account_type"]
        account.amount = json["amount"]
        return account