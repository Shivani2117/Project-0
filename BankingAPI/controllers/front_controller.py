from controllers import bank_controller, home_controller, account_controller


def route(app,):
    bank_controller.route(app)
    home_controller.route(app)
    account_controller.route(app)