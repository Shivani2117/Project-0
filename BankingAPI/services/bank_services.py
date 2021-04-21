from daos.bank_dao_impl import BankDAOImpl
from daos.bank_dao_temp import BankDaoTemp


class BankServices:

    #bank_dao = BankDaoTemp()
    bank_dao = BankDAOImpl()

    @classmethod
    def create_client(cls, bank):
        return cls.bank_dao.create_client(bank)

    @classmethod
    def all_clients(cls):
        return cls.bank_dao.all_clients()

    @classmethod
    def get_client_by_id(cls, client_id):
        return cls.bank_dao.get_client(client_id)

    @classmethod
    def update_client(cls, bank):
        return cls.bank_dao.update_client(bank)

    @classmethod
    def delete_client(cls, client_id):
        return cls.bank_dao.delete_client(client_id)