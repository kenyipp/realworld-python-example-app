from flask import request, jsonify
from server.user.service.factory import Factory
from server.user.dto import ApiInputRegistration

factory = Factory()
api_registration = factory.new_api_registration()

def registration():
    request_body = request.get_json()
    body = ApiInputRegistration(**request_body)

    username = body.get("username")
    email = body.get("email")
    password: body.get("password")
    image: body.get("image")

    response = api_registration.execute(
        username=username,
        email=email,
        password=password,
        image=image
    )
    return jsonify(response)
