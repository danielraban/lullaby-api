import click
from flask.cli import with_appcontext


@click.command("init")
@with_appcontext
def init():
    """Create a new admin user"""
    from lullaby_api.extensions import db
    from lullaby_api.models import User

    click.echo("create user")
    user = User(username="admin", email="danielraban@proton.me", password="admin", active=True)
    db.session.add(user)
    db.session.commit()
    click.echo("created user admin")
