import os
import click
from flask import Flask
from .extension import api
from .setting import config
from .bluelog import app_rustful
from .bluelog import api_bp
from .models import *


def creat_app(config_name=None):
    if config_name is None:
        config_name = os.getenv('FLASK_CONFIG', 'development')
    # print(__name__)
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    register_extensions(app)
    register_blueprints(app)
    register_commands(app)
    return app


def register_extensions(app):
    db.init_app(app)
    # api.init_app(app)


def register_blueprints(app):
    # app.register_blueprint(app_rustful,url_prefix="/admin")
    app.register_blueprint(app_rustful)
    app.register_blueprint(api_bp, url_prefix="/api")


# def register_shell_context(app):
#     @app.shell_context_processor
#     def make_shell_context():
#         return dict(db=db,note=Note)


def register_commands(app):
    @app.cli.command()
    @click.option('--drop', is_flag=True, help='Create after drop.')
    def initdb(drop):
        """Initialize the database."""
        if drop:
            click.confirm('This operation will delete the database, do you want to continue?', abort=True)
            db.drop_all()
            click.echo('Drop tables.')
        db.create_all()
        click.echo('Initialized database.')
