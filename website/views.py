from flask import Blueprint, render_template, request
from .models import Encounter
from . import db

views = Blueprint("views", __name__)

@views.route("/")
def home():
    return render_template("home.html")

@views.route("/playerView")
def playerView():
    return render_template("playerView.html")

@views.route("/controlPanel", methods=['GET', 'POST'])
def ControlPanel():
    if request.method =="Post":
        pass

    return render_template("controlPanel.html")

@views.route("/editEnc")
def editEnc():
    return render_template("editEnc.html")

@views.route("/giveIni")
def giveIni():
    return render_template("giveIni.html")

@views.route("/runEnc")
def runEnc():
    return render_template("runEnc.html")