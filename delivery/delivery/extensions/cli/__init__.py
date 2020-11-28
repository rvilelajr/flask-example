import click
from delivery.extensions.site import models 
from delivery.extensions.db import db


def init_app(app):
    @app.cli.command()
    def create_db():
        """Initialize the database"""
        db.create_all()


    @app.cli.command()
    @click.option("--email", "-e")
    @click.option("--password", "-p")
    @click.option("--admin", "-a", is_flag=True, default=False)
    def add_user(email, password, admin):
        """Add a new user"""
        user = models.User(
            email = email,
            password = password,
            admin = admin
        )
        db.session.add(user)
        db.session.commit()
        click.echo(f"User {email} has been created")