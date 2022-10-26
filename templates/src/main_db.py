import sys
import config
from loguru import logger
from flasgger import Swagger
from datetime import datetime
from flask import Flask, jsonify
from flask_cors import CORS
from flask_wtf.csrf import CSRFProtect

from models.db import db
from routes.route import api_blueprint


# Logger config
logger_format = '<le>{time:YYYY-MM-DD HH:mm:ss.SSS}</le>|<b>{name}-{function}</b>|<lvl>{level.name}</lvl>:{message}'
logger_path = "src/logs/{}.logs".format(datetime.strftime(datetime.today(), "%Y/%m/%d"))
logger.remove(0)
logger.level("INFO",color="<green>")
logger.add(logger_path, format=logger_format, rotation="00:00", compression="zip", colorize=False)
logger.add(sys.stdout, format=logger_format, colorize=True)

# Initialize Flask
app = Flask(__name__)
CORS(app, support_credentials=True)
app.url_map.strict_slashes = False

csrf = CSRFProtect(app)

# Database connection config
app.config["SQLALCHEMY_DATABASE_URI"] = config.DATABASE_CONNECTION_URI
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.app_context().push()
db.init_app(app)

# Swagger config
app.config["SWAGGER"] = {"title": "Swagger-UI", "uiversion": 2}
swagger_config = {
    "headers": [],
    "specs": [
        {
            "endpoint": "apispec_1",
            "route": "/apispec_1.json",
            "rule_filter": lambda rule: True,
            "model_filter": lambda tag: True,
        }
    ],
    "static_url_path": "/flasgger_static",
    "swagger_ui": True,
    "specs_route": "/swagger/",
}
swagger = Swagger(app, config=swagger_config)

# Register blueprints
app.register_blueprint(api_blueprint, url_prefix='/api')


# Errors config
@app.errorhandler(400)
def bad_request(e):
    return jsonify(error=str(e)), 400


@app.errorhandler(412)
def precondition_failed(e):
    return jsonify(error=str(e)), 412


@app.errorhandler(409)
def conflict(e):
    return jsonify(error=str(e)), 409


@app.errorhandler(500)
def internal_server_error(e):
    return jsonify(error=str(e)), 500


@app.errorhandler(401)
def unauthorized(e):
    return jsonify(error=str(e)), 401


@app.errorhandler(403)
def forbidden(e):
    return jsonify(error=str(e)), 403


@app.errorhandler(404)
def not_found(e):
    return jsonify(error=str(e)), 404


if __name__ == '__main__':
    app.run(host="0.0.0.0", debug=True)
