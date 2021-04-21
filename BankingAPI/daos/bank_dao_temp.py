from daos.bank_dao import BankDAO
from exceptions.resorce_not_found import ResourceNotFound
from util.temp_db_bank import TempDBBank as db

class BankDaoTemp(BankDAO):

    def create_client(self, client):
        db.bank[client.client_id] = client

    def get_client(self, client_id):
        try:
            return db.bank[client_id]
        except KeyError:
            raise ResourceNotFound(f"Client with id: {client_id} - Not Found")

    def all_clients(self):
        return [bank.json() for bank in db.bank.values()]

    def update_client(self, change):
        db.bank.update({change.client_id: change})

    def delete_client(self, client_id):
        del db.bank[client_id]