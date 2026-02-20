from flask import Flask, render_template, request, send_from_directory,redirect, url_for

#this importbd
import os

basedir = os.path.abspath(os.path.dirname(__file__))
app = Flask(__name__)
MyFolderForVolodia = os.path.join(basedir, '..', 'uploads')
app.config['UPLOAD_FOLDER'] = os.path.normpath(MyFolderForVolodia)


@app.route("/")
def home():
    return render_template("")