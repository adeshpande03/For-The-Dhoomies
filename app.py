import atexit
import os
from flask import (
    Flask,
    redirect,
    render_template,
    request,
    flash,
    url_for,
    send_from_directory,
)
from werkzeug.utils import secure_filename
import random
import shutil

UPLOAD_FOLDER = "uploads"
ALLOWED_EXTENSIONS = {"png", "jpg", "jpeg", "gif"}

app = Flask(__name__)
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER
app.secret_key = "super_secret_key"
app.picidx = -1
app.playerNames = []


def clear_uploads_folder():
    folder = app.config["UPLOAD_FOLDER"]
    for filename in os.listdir(folder):
        file_path = os.path.join(folder, filename)
        try:
            if os.path.isfile(file_path) or os.path.islink(file_path):
                os.unlink(file_path)
            elif os.path.isdir(file_path):
                shutil.rmtree(file_path)
        except Exception as e:
            print(f"Failed to delete {file_path}. Reason: {e}")


os.makedirs(UPLOAD_FOLDER, exist_ok=True)
clear_uploads_folder()


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
    player_names = request.form.getlist("playerName[]")
    app.playerNames = player_names
    print(player_names)
    return redirect(url_for("show_random_image"))


@app.route("/random-image")
def show_random_image():
    player_names = app.playerNames
    return render_template("play.html", player_names=player_names)


@app.route("/get-random-image")
def get_random_image():
    files = [
        f
        for f in os.listdir(app.config["UPLOAD_FOLDER"])
        if os.path.isfile(os.path.join(app.config["UPLOAD_FOLDER"], f))
    ]
    if not files:
        return "No images uploaded", 404
    if app.picidx == -1:
        random.shuffle(files)
    app.picidx += 1
    if app.picidx == len(files):
        random.shuffle(files)
        app.picidx = 0
    return send_from_directory(app.config["UPLOAD_FOLDER"], files[app.picidx])


@atexit.register
def goodbye():
    clear_uploads_folder()


if __name__ == "__main__":
    app.run()
