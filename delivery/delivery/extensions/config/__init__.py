def init_app(app):
    app.config["SECRET_KEY"] = "sarava123"
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///delivery.db"
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    app.config["FLASK_ADMIN_SWATCH"] = "cerulean"
