def route(app):
    @app.route("/", methods=['GET', 'POST'])
    def hello():
        return "Hello Bank!"

    @app.route("/contact")
    def contact():
        return "Contact Us via Email: Bank@email.com  or Phone no: 777-888-9999 "

