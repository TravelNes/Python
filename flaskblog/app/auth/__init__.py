from flask import Blueprint, render_template, request

auth = Blueprint('auth', __name__, template_folder='templates')
from . import route
