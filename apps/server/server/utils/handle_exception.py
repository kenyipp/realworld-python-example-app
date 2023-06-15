from uuid import uuid4
from flask import jsonify
from pydantic import ValidationError
from server.error.api_error import APIError
from server.error.api_error_unprocessable_entity import APIErrorUnprocessableEntity
from server.error.api_error_internal_server import APIErrorInternalServerError
from werkzeug.exceptions import HTTPException

def handle_exception(error):
    if isinstance(error, HTTPException):
        return error.get_body(), error.code
    elif isinstance(error, ValidationError):
        error = APIErrorUnprocessableEntity()

    if not isinstance(error, APIError):
        error = APIErrorInternalServerError()

    return jsonify({
        "error": {
            "id": str(uuid4()),
            "code": error.code,
            "message": error.message,
            "error_code": error.error_code,
            "error_type": error.error_type,
            "payload": error.payload
        }
    }), error.code

