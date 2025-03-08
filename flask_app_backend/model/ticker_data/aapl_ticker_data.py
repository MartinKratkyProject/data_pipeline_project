from model.ticker_models import ticker_models
from flask import jsonify

def get_aapl_data():
    result = []
    try:
        aapl_data = ticker_models.AAPL.query.all()
        result = [{"timestamp": row.timestamp, "open": row.open, "close": row.close} for row in aapl_data]
        print(result)

        return jsonify(result)
    except Exception as e:
        return jsonify(result)
