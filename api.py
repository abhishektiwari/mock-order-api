"""
Flask Sample APIs
"""
from flask import Flask, jsonify
from flask_dotenv import DotEnv
from apis.exceptions import InvalidUsage
from flask_cors import CORS

# Flask app
app = Flask(__name__)  # pylint: disable=invalid-name
app.config.from_object("config")

# if .env file available
env = DotEnv(app)

# if .env file available
env = DotEnv(app)

# Setup CORS globally
cors = CORS(app, resources={r"/*": {"origins": "*"}})

# API blueprints, imported after OS.environ
from apis.public import public_api
from apis.private import private_api
app.register_blueprint(public_api)
app.register_blueprint(private_api)


@app.errorhandler(InvalidUsage)
def handle_invalid_usage(error):
    response = jsonify(error.to_dict())
    response.status_code = error.status_code
    return response

# Controllers API
@app.route("/", methods=["GET"])
def index():
    """
    Index for this app
    """
    return jsonify({"api": "Mock Order APIs"})
