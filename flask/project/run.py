import os,sys
import logging.config
from flask import Flask, g
import flask_login

CURRENT_DIR = os.path.dirname(os.path.realpath(__file__))
config_path = os.path.join(CURRENT_DIR, 'config')

logging.config.fileConfig(os.path.join(config_path, 'logging.conf'))

app = Flask(__name__)
login_manager = flask_login.LoginManager()
login_manager.init_app(app)

app.logger.logger_name = __name__

from social.routes import users, visit, location
app.register_blueprint(users)
app.register_blueprint(visit)
app.register_blueprint(location)


if __name__ == '__main__':
    app.run(debug=True)