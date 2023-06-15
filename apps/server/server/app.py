from flask import Flask
from server.config import register_route as register_config_route
from server.user import register_route as register_user_route
from server.utils.handle_exception import handle_exception


def create_app():
    app = Flask(__name__)

    register_config_route(app=app)
    register_user_route(app=app)

    app.register_error_handler(Exception, lambda error: handle_exception(error))

    return app


if __name__ == "__main__":
    app = create_app()
    app.run()
