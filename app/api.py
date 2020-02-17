from flask import Blueprint

bp = Blueprint('api_bp', __name__, url_prefix='/api')


@bp.route('/')
def main():
    return 'API/main'
