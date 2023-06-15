from flask import Flask

def health_check():
    return "Ok"

def register_route(app: Flask):
    app.add_url_rule(
        "/api/health-check",
        "health-check",
        health_check,
        methods=["GET"]
    )
