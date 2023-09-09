### Human Skin Detection Web App ###
### This Project Authored By Mehran Moein ###
### Linkedin: https://www.linkedin.com/in/mehran6511 ###
### Github: https://github.com/mehran6511 ###
### Refrence:Human Skin Detection Using RGB, HSV and YCbCr Color Models ###

# Libraries
import os
from flask import Flask, flash, jsonify, redirect, render_template, request, session, url_for
from werkzeug.utils import secure_filename
import numpy as np
import cv2
# permition of upload image
UPLOAD_FOLDER = './static'
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg'}
# Configure application
app = Flask(__name__)
app.secret_key = "super secret key"
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
# Ensure templates are auto-reloaded
app.config["TEMPLATES_AUTO_RELOAD"] = True

@app.after_request
def after_request(response):
    """Ensure responses aren't cached"""
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response
# allowed image function
def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        # upload and save image file
        if 'file' not in request.files:
            flash('No file part')
            return render_template("index.html")
        file = request.files['file']
        if file.filename == '':
            flash('No selected file')
            return render_template("index.html")
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        else:
            flash('plese use jpg file')
            return render_template("index.html")
        # save address image
        session['original_img'] = os.path.join("", filename)
        #read image
        img_original = cv2.imread(f"./static/{file.filename}")
        # convert to diffrent color
        img_RGB = cv2.cvtColor(img_original, cv2.COLOR_BGR2RGB)
        img_HSV = cv2.cvtColor(img_original, cv2.COLOR_BGR2HSV)
        img_YCrCb = cv2.cvtColor(img_original, cv2.COLOR_BGR2YCrCb)
        # split to channels
        R_channel,G_channel,B_channel = cv2.split(img_RGB)
        H_channel,S_channel,V_channel = cv2.split(img_HSV)
        Y_channel,Cr_channel,Cb_channel = cv2.split(img_YCrCb)
        # normalize
        S_channel = S_channel/255
        V_channel = V_channel/255
        # create image empty
        img_skin = np.zeros_like(R_channel,'uint8')
        # create channels empty
        R_channel_new = np.zeros_like(R_channel,'uint8')
        G_channel_new = np.zeros_like(R_channel,'uint8')
        B_channel_new = np.zeros_like(R_channel,'uint8')
        # calculate for detect skin
        for i in range(R_channel.shape[0]):
            for j in range(R_channel.shape[1]):
                if R_channel[i][j]>95 \
                    and G_channel[i][j]>40 \
                    and B_channel[i][j]>20 \
                    and R_channel[i][j]>G_channel[i][j] \
                    and R_channel[i][j]>B_channel[i][j] \
                    and abs(R_channel[i][j]-G_channel[i][j])>15 \
                    and Cr_channel[i][j]>135 \
                    and Cb_channel[i][j]>85 \
                    and Y_channel[i][j]>80 \
                    and Cr_channel[i][j]<=((1.5862*Cb_channel[i][j])+20) \
                    and Cr_channel[i][j]>=((0.3448*Cb_channel[i][j])+76.2069) \
                    and Cr_channel[i][j]>=(((-4.5652)*Cb_channel[i][j])+234.5652) \
                    and Cr_channel[i][j]<=(((-1.15)*Cb_channel[i][j])+301.75) \
                    and Cr_channel[i][j]<=(((-2.2857)*Cb_channel[i][j])+432.85):
                        img_skin[i][j] = 255
                        R_channel_new[i][j] = R_channel[i][j]
                        G_channel_new[i][j] = G_channel[i][j]
                        B_channel_new[i][j] = B_channel[i][j]
        # save skin detection image
        img_skin_real = cv2.merge([R_channel_new,G_channel_new,B_channel_new])
        cv2.imwrite("./static/new.jpg", cv2.cvtColor(img_skin_real, cv2.COLOR_RGB2BGR))
        # save that address
        session['new_img'] = os.path.join("", "new.jpg")
        # return to show html page
        return render_template("show.html", image1=session.get('original_img', None), image2=session.get('new_img', None))
    else:
        # return to index html page
        return render_template("index.html")