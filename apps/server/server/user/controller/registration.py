from flask import jsonify, request
from server.user.dto import ApiInputRegistration
from server.user.service.factory import Factory

factory = Factory()
api_registration = factory.new_api_registration()


def registration():
    request_body = request.get_json()
    body = ApiInputRegistration(**request_body.get("user"))

    response = api_registration.execute(
        username=body.username,
        email=body.email,
        password=body.password,
        image=body.image
    )

    return jsonify(response)
