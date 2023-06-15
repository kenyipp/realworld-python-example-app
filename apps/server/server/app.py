from flask import Flask
from server.config import register_route as register_config_route
from server.user import register_route as register_user_route
from server.utils.handle_exception import handle_exception

app = Flask(__name__)

register_config_route(app=app)
register_user_route(app=app)

# Global Error handler for all exceptions
@app.errorhandler(Exception)
def global_exception_handler(error):
    response, code = handle_exception(error)
    return response, code

if __name__ == "__main__":
    app.run()
