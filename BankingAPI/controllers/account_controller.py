from flask import jsonify, request

from exceptions.resorce_not_found import ResourceNotFound
from model.account import Account
from services.account_service import AccountService


def route(app):

    @app.route("/accounts", methods=['GET'])
    def get_all_accounts():
        return jsonify(AccountService.all_accounts())

    @app.route("/accounts/<client_id>", methods=['GET'])
    def get_account(client_id):
        try:
            account = AccountService.get_account_by_id(int(client_id))
            return jsonify(account.json()), 200
        except ValueError as er:
            return "Not a Valid Id", 400
        except ResourceNotFound as rr:
            return rr.message, 404

    @app.route("/accounts", methods=["post"])
    def post_account():
        # account = Account.json_parse(request.json())
        account = Account.json_parse(request.json)
        AccountService.create_account(account)
        return jsonify(account.json())

    @app.route("/accounts/<client_id>", methods=["PUT"])
    def put_account(client_id):
        account = Account.json_parse(request.json)
        account.account_id = int(client_id)
        AccountService.update_account(account)
        return jsonify(account.json()), 200

    @app.route("/accounts/<client_id>", methods=["DELETE"])
    def del_account(client_id):
        AccountService.delete_account(int(client_id))
        return '', 200