import json

import modules.service as service

from loguru import logger
from flasgger.utils import swag_from
from flask import Blueprint, Response, abort
from libraries.custom_error import NotFound, Forbidden
from flask_cors import cross_origin

api_blueprint = Blueprint("route_1", __name__,)


def ErrorException(e):
    logger.error(f"Error to get schema - {e}")
    t = type(e)
    if t == ConnectionError: abort(400, e)
    if t == NotFound: abort(404, e)
    if t == Forbidden: abort(403, e)
    else: abort(400, e)


@api_blueprint.route("/sum/<num_1>/<num_2>", methods=(["GET"]))
@cross_origin(supports_credentials=True)
@swag_from("sum.yaml")
def sum(num_1, num_2):
    try:
        response = service.sum(int(num_1), int(num_2))
        return Response(json.dumps(response), 200, mimetype = "application/json")
    except:
        ErrorException("Error to sum numbers")
