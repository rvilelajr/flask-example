def init_app(app):
    app.config["SQLALCHEMY_DATABASE_URI"] = 'sqlite:///delivery.db'