"""
Private API
"""
from flask import Blueprint
from flask import jsonify
from flask import request
from datetime import datetime, timedelta
import random
from .auth import authenticate
from .exceptions import InvalidUsage

private_api = Blueprint("private_api", __name__)  # pylint: disable=invalid-name

N_DAYS = 2
STATUSES = ['shipped', 'delivered', 'processing']

@private_api.route("/order", methods=["GET"])
@authenticate
def api_private():
    """
    Private API - authentication required
    """
    customer_no = request.args.get("customerNo", None)
    if customer_no:
        return jsonify(
            {
                "customerNo": customer_no,
                "orderNumber": "OR-{}".format(customer_no),
                "orderDate": datetime.now() - timedelta(days=N_DAYS),
                "orderStatus": random.choice(STATUSES),
            }
        )
    else:
        raise InvalidUsage("Missing customerNo", status_code=400)

