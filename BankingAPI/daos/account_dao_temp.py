from daos.account_dao import AccountDAO
from exceptions.resorce_not_found import ResourceNotFound
from model import account
from util.temp_db_account import TempDBAccount as db

class AccountDAOTemp(AccountDAO):

    def create_account(self, client_id):
        db.accounts[account.client_id] = account

    def get_account(self, account_id):
        try:
            return db.accounts[account_id]
        except KeyError:
            raise ResourceNotFound(f"Account with id: {client_id} - Not Found")

    def all_accounts(self):
        return [account.json() for account in db.accounts.values()]

    def update_account(self, change):
        db.accounts.update({change.account_id: change})

    def delete_account(self, account_id):
        del db.accounts[account_id]
