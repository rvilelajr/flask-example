import click
from delivery.extensions.auth.controller import create_user
from delivery.extensions.db import db


def init_app(app):
    @app.cli.command()
    def create_db():
        """Initialize the database"""
        db.create_all()

    @app.cli.command()
    @click.option("--name", "-n")
    @click.option("--email", "-e")
    @click.option("--password", "-p")
    @click.option("--admin", "-a", is_flag=True, default=False)
    def add_user(name, email, password, admin):
        """Add a new user"""
        create_user(email, password, name)
        click.echo(f"User {email} has been created")
