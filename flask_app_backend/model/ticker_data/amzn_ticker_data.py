from model.ticker_models import ticker_models
from flask import jsonify

def get_amzn_data():
    result = []
    try:
        amzn_data = ticker_models.AMZN.query.all()
        result = [{"timestamp": row.timestamp, "open": row.open, "close": row.close} for row in amzn_data]

        return jsonify(result)
    except Exception as e:
        return jsonify(result)