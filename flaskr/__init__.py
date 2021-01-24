import os

from flask import Flask
from flask import render_template
from data import Data

def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='dev',
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

    # a simple page that says hello
    @app.route('/hello')
    def hello():
        outdata = Data.temp() # retrieves data from server (See data.py)

        ##DATA ACCESS
        longitude = outdata.lons        # 1 dim Array
        latitude = outdata.lats         # 1 dim Array
        temperature = outdata.ssts      # 3 dim Array [<Always 0>, <latitude index>, <longitude index>]

        return outdata

    @app.route('/index.html')
    def index():
        return render_template('index.html')

    return app
