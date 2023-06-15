from flask import Flask
from server.user.controller.registration import registration

def register_route(app: Flask):
    app.add_url_rule(
        "/api/users",
        "registration",
        registration,
        methods=["POST"]
    )
