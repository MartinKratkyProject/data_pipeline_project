from flask import Blueprint
from model.ticker_data.aapl_ticker_data import get_aapl_data
from model.ticker_data.amzn_ticker_data import get_amzn_data
from model.ticker_data.googl_ticker_data import get_googl_data
from model.ticker_data.nvda_ticker_data import get_nvda_data
from model.ticker_data.tsla_ticker_data import get_tsla_data
from model.home_ticker_data import get_home_data

routes_bp = Blueprint('routes', __name__)

@routes_bp.route('/')
def index():
    return "Welcome to the backend"

@routes_bp.route('/home', methods=['GET'])
def get_home_route():
    return get_home_data()

@routes_bp.route('/aapl', methods=['GET'])
def get_aapl_route():
    return get_aapl_data()

@routes_bp.route('/amzn', methods=['GET'])
def get_amzn_route():
    return get_amzn_data()

@routes_bp.route('/googl', methods=['GET'])
def get_googl_route():
    return get_googl_data()

@routes_bp.route('/nvda', methods=['GET'])
def get_nvda_route():
    return get_nvda_data()

@routes_bp.route('/tsla', methods=['GET'])
def get_tsla_route():
    return get_tsla_data()