import os

from flask import Flask

'''

author: Dennis Hsieh
date: 11/10//2023

the starting point of this application

NOTE: WE HAVE TO PUT SECRET_KEY IN A CONFIG FILE ON OUR SERVE DURING DEPLOYMENT

'''

def create_app(test_config=None):
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='dev', # should change and not make secret key public later
        DATABASE=os.path.join(app.instance_path, 'flaskr.sqlite'),
    )

    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile('config.py', silent=True)
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    from . import db

    db.init_app(app)

    # a simple page that says hello
    @app.route('/welcome')
    def hello():
        return 'Welcome to your code runtime profiler!'

    return app