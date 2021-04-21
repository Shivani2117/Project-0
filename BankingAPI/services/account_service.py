from daos.account_dao_temp import AccountDAOTemp


class AccountService:

    account_dao = AccountDAOTemp()

    @classmethod
    def create_account(cls, client_id):
        return cls.account_dao.create_account(client_id)

    @classmethod
    def all_accounts(cls):
        return cls.account_dao.all_accounts()

    @classmethod
    def get_account_by_id(cls, client_id):
        return cls.account_dao.get_account(client_id)

    @classmethod
    def update_account(cls, client_id):
        return cls.account_dao.update_account(client_id)

    @classmethod
    def delete_account(cls, account_id):
        return cls.account_dao.delete_account(account_id)