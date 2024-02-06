import os
from flask_uploads import UploadSet, IMAGES, configure_uploads
from flask import (
    Flask,
    redirect,
    render_template,
    request,
    session,
    send_file,
    make_response,
    flash,
    url_for,
    send_from_directory,
)
from werkzeug.utils import secure_filename
import random


UPLOAD_FOLDER = "uploads"
ALLOWED_EXTENSIONS = {"png", "jpg", "jpeg", "gif"}


app = Flask(__name__)
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER
app.secret_key = 'super_secret_key'

def allowed_file(filename):
    return "." in filename and filename.rsplit(".", 1)[1].lower() in ALLOWED_EXTENSIONS


@app.route("/")
def upload_form():
    return render_template("upload.html")


@app.route("/upload", methods=["POST"])
def upload_files():
    if "file[]" not in request.files:
        flash("No file part")
        return redirect(request.url)
    files = request.files.getlist("file[]")
    for file in files:
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config["UPLOAD_FOLDER"], filename))
    flash("Files successfully uploaded")
    return redirect(url_for("show_random_image"))


@app.route("/random-image")
def show_random_image():
    return render_template("play.html")


@app.route("/get-random-image")
def get_random_image():
    files = [
        f
        for f in os.listdir(app.config["UPLOAD_FOLDER"])
        if os.path.isfile(os.path.join(app.config["UPLOAD_FOLDER"], f))
    ]
    if not files:
        return "No images uploaded", 404
    random_file = random.choice(files)
    return send_from_directory(app.config["UPLOAD_FOLDER"], random_file)


if __name__ == "__main__":
    app.run()
