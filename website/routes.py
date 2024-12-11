from flask import Blueprint, render_template, request

routes = Blueprint('routes', __name__)

@routes.route('/')
def home():
    return render_template("home.html")

@routes.route('/pairwise-alignment')
def pairwise_alignment():
    return render_template('pairwise_alignment.html')

@routes.route('/multiple-alignment')
def multiple_alignment():
    return render_template('multiple_alignment.html')

@routes.route('/phylogenetic-tree')
def phylogenetic_tree():
    return render_template('phylogenetic_tree.html')