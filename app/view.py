from flask import Blueprint, render_template

bp = Blueprint('view_bp', __name__)


@bp.route('/')
def index():
    return render_template('index.html')
