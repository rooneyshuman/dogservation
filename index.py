import os
import sys
from flask import render_template
from flask.views import MethodView
from dotenv import load_dotenv


class Index(MethodView):
    def get(self):
        load_dotenv()
        SITE_URL = os.getenv("SITE_URL")
        return render_template("index.html", site_url=SITE_URL)