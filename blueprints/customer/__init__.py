from flask import Blueprint

customer_bp = Blueprint('customer', __name__, url_prefix='/customers')
from . import routes