
class Bank:

    def __init__(self, client_id=0, firstname="", lastname="", address=""):
        self.client_id = client_id
        self.firstname = firstname
        self.lastname = lastname
        self.address = address

    def json(self):
        return {
            'clientId': self.client_id,
            'firstname': self.firstname,
            'lastname': self.lastname,
            'address': self.address
        }

    @staticmethod
    def json_parse(json):
        bank = Bank()
        bank.client_id = json["clientId"] if "client_id" in json else 0
        bank.firstname = json["firstname"]
        bank.lastname = json["lastname"]
        bank.address = json["address"]
        return bank

    def __repr__(self):
        return str(self.json())

