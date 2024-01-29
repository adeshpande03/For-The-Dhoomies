import datetime
import json
import os
import requests
import urllib.parse
from flask_uploads import UploadSet, IMAGES, configure_uploads
from flask import (
    Flask,
    redirect,
    render_template,
    request,
    session,
    send_file,
    make_response,
)
from flask_session import Session
from functools import wraps
from tempfile import mkdtemp
from functools import *


# import for future functionality
import shutil
import zipfile
from glob import glob
from io import BytesIO


app = Flask(__name__)
photos = UploadSet("photos", IMAGES)

app.config["UPLOADS_DEFAULT_DEST"] = "static/img"
app.config["UPLOADS_DEFAULT_URL"] = "/static/img"

configure_uploads(app, photos)

app.config["TEMPLATES_AUTO_RELOAD"] = True


@app.after_request
def after_request(response):
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response


app.config["SESSION_FILE_DIR"] = mkdtemp()
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

@app.route("/")
def index():
    return render_template("index.html")

