from flask import Blueprint
from model.ticker_data.aapl_ticker_data import get_aapl_data
from model.ticker_data.amzn_ticker_data import get_amzn_data

routes_bp = Blueprint('routes', __name__)

@routes_bp.route('/')
def index():
    return "Welcome to the backend"

@routes_bp.route('/aapl', methods=['GET'])
def get_aapl_route():
    return get_aapl_data()

@routes_bp.route('/amzn', methods=['GET'])
def get_amzn_route():
    return get_amzn_data()
