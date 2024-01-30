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


@app.route("/")
def index():
    return render_template("index.html")


if __name__ == "__main__":
    app.run()
