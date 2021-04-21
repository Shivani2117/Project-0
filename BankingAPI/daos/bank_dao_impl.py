from daos.bank_dao import BankDAO
from exceptions.resorce_not_found import ResourceNotFound
from util.db_connection import connection
from model.bank import Bank

class BankDAOImpl(BankDAO):
    def create_client(self, bank):
        sql = "INSERT INTO clients VALUES string(DEFAULT,%s,%s,%s) RETURNING *"

        cursor = connection.cursor()
        cursor.execute(sql, (bank.firstname, bank.lastname, bank.address))

        connection.commit()
        record = cursor.fetchone()
        print(record)
        new_client = Bank(record[0], record[1], record[2])
        print(new_client)
        return new_client

    def get_client(self, client_id):
        sql = "select * from clients where clientid = %s"
        cursor = connection.cursor()
        cursor.execute(sql, [client_id])

        record = cursor.fetchone()
        #print(record)
        if record:
            return Bank(record[0], record[1], record[2], record[3]).json()
        else:
            raise ResourceNotFound(f"Client with id: {client_id} - Not Found")


    def all_clients(self):
        sql = "select * from clients"
        cursor = connection.cursor()
        cursor.execute(sql)
        records = cursor.fetchall()

        client_list = []
        for record in records:
            bank = Bank(record[0], record[1], record[2], record[3])

            client_list.append(bank.json())

        return client_list

    def update_client(self, change):
        sql = "UPDATE clients SET firstname=%s,lastname=%s,address=%s WHERE clientid = %s RETURNING *"

        cursor = connection.cursor()
        cursor.execute(sql, (change.firstname, change.lastname, change.address, change.client_id))
        connection.commit()

        record = cursor.fetchone()

        new_client = Bank(record[0], record[1], record[2], float(record[3]), record[4], record[5])
        return new_client

    def delete_client(self, client_id):
        sql = "DELETE FROM client WHERE clientid = %s"

        cursor = connection.cursor()
        cursor.execute(sql, [client_id])
        connection.commit()


def _test():
    b_dao = BankDAOImpl()
    clients = b_dao.all_clients()
    print(clients)

    print(b_dao.get_client(1))


if __name__ == '__main__':
    _test()