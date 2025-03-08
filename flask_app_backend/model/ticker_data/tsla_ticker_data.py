from model.ticker_models import ticker_models
from flask import jsonify

def get_tsla_data():
    result = []
    try:
        tsla_data = ticker_models.TSLA.query.all()
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
            } for row in tsla_data
        ]

        return jsonify(result)
    except Exception as e:
        return jsonify(result)