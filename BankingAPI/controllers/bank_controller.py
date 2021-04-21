from flask import jsonify, request

from exceptions.resorce_not_found import ResourceNotFound
from model.bank import Bank

from services.bank_services import BankServices

def route(app):
    @app.route("/clients", methods=['GET'])
    def get_all_clients():
        return jsonify(BankServices.all_clients())

    @app.route("/clients/<client_id>", methods=['GET'])
    def get_client(client_id):
        try:
            bank = BankServices.get_client_by_id(int(client_id))
            return jsonify(bank.json()), 200
        except ValueError as e:
            return "Not a Valid ID", 400
        except ResourceNotFound as r:
            return r.message, 404

    @app.route("/clients", methods=["POST"])
    def post_client():
        bank = Bank.json_parse(request.json)
        bank = BankServices.create_client(bank)
        return jsonify(bank.json()), 201

    @app.route("/clients/<client_id>", methods=["PUT"])
    def put_client(client_id):
        bank = Bank.json_parse(request.json)
        bank = bank.client_id = int(client_id)
        BankServices.update_client(bank)
        return jsonify(bank.json()), 200

    @app.route("/clients/<client_id>", methods=["DELETE"])
    def del_client(client_id):
        BankServices.delete_client(int(client_id))
        return '', 204



