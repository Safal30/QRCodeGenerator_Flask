from flask import Flask, app, render_template, request
import os, qrcode, time, base64, requests, json, io
from PIL import Image

#to create a requirements.txt = pip3 freeze > requirements.txt

app = Flask(__name__)

UPLOAD_FOLDER = "/"
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER


@app.route("/")
def form():

    return render_template("base.html")


@app.route("/", methods=["POST"])
def data():

    text = request.form["title"]
    #pro_text = text.upper()

    url = text

    #an instance of qrcode
    qr = qrcode.QRCode(version=1, error_correction=qrcode.constants.ERROR_CORRECT_L, box_size=10, border=4,)

    qr.add_data(url)
    qr.make(fit=True)

    img = qr.make_image(fill_color="black", back_color="white")
    #img.save("static\qrcode.png")

    data = io.BytesIO()
    img.save(data, "JPEG")
    encoded_img_data = base64.b64encode(data.getvalue())

    return render_template("qrcode.html", img = encoded_img_data.decode("utf-8"))


if __name__ == '__main__':
    app.run(debug=True)


