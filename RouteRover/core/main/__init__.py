from flask import Blueprint


main_bp = Blueprint('main', __name__, url_prefix='/')

from core.main import routes