import flask
from flask.views import MethodView
from index import Index

app = flask.Flask(__name__)  # our Flask app

app.add_url_rule("/", view_func=Index.as_view("index"), methods=["GET"])

"""
Application access point. Specifies host and port to run on
"""
if __name__ == "__main__":
    app.run(debug=True)