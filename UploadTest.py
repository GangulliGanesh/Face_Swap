import os
from face_swap import swap_warp

from uuid import uuid4

from flask import Flask, render_template, request, redirect, url_for, send_from_directory
from werkzeug import secure_filename

app = Flask(__name__)

image_2=""
image_1=""
ko=""

APP_ROOT = os.path.dirname(os.path.abspath(__file__))

@app.route("/")
def index():
    return render_template("upload.html")

@app.route("/upload", methods=["POST","GET"])
def upload():

    print(request.method)
    if request.method == "GET":
        return render_template("upload.html")
    elif request.method== "POST":
        target = os.path.join(APP_ROOT, 'static/')

        if not os.path.exists(target):
                os.mkdir(target)
        else:
            print("Target created 0")


        for upload in request.files.getlist("file1"):
            global image_1
            image_1=""
            filename1= upload.filename
            destination = "/".join([target, filename1])
            destination = os.path.join(target,filename1)
            image_1=os.path.join("static",filename1)
            upload.save(destination)
            print(image_1)


        return render_template("upload.html",image_1=image_1,image_2=image_2)


@app.route("/upload1", methods=["POST","GET"])
def upload1():

    print(request.method)
    if request.method == "GET":
        return render_template("upload.html")
    elif request.method== "POST":
        target = os.path.join(APP_ROOT, 'static/')

        if not os.path.exists(target):
                os.mkdir(target)
        else:
            print("Static folder created 1")


        for upload in request.files.getlist("file2"):
            global image_2
            image_2=""
            filename2= upload.filename
            destination = "/".join([target, filename2])
            destination = os.path.join(target,filename2)
            image_2=os.path.join("static",filename2)
            print(image_2)
            print(image_1)
            upload.save(destination)

        return render_template("upload.html",image_2=image_2,image_1=image_1)

@app.route("/res", methods=["POST","GET"])
def res():
    global ko
    ko=""
    ko=swap_warp(image_1,image_2)
    return render_template("upload.html",image_2=image_2,image_1=image_1,ko=ko)


@app.route('/upload/<filename>')
def send_image(filename):
    return send_from_directory("images", filename)



if __name__ == "__main__":
    app.run(port=8080, debug=True)
