
from App import app


@app.route("/")
def index():
    return "Hello Word"
