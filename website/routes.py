from flask import Blueprint, render_template, request

routes = Blueprint('routes', __name__)

@routes.route('/')
def home():
    return render_template("home.html")