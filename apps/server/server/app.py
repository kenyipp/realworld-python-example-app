from flask import Flask

app = Flask(__name__)

@app.route("/api/health-check", methods=["GET"])
def health_check():
    return "Ok"

if __name__ == "__main__":
    app.run()
