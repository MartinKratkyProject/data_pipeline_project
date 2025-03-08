from model.ticker_models import ticker_models
from flask import jsonify

def get_nvda_data():
    result = []
    try:
        nvda_data = ticker_models.NVDA.query.all()
        result = [
            {
                "timestamp": row.timestamp
                , "open": row.open
                , "close": row.close
                , "high": row.high
                , "low": row.low
                , "volume": row.volume
                , "vwap": row.vwap
                , "transactions": row.transactions
                , "ticker": "AAPL"
            } for row in nvda_data
        ]

        return jsonify(result)
    except Exception as e:
        return jsonify(result)