from flask import Blueprint, render_template, request, jsonify, redirect, url_for

views = Blueprint(__name__, "views")


@views.route("/")
def home():
    return render_template("./index.html")


@views.route("/home/styles.css/")
def index():
    return render_template("./styles.css")
