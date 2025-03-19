from model.ticker_models import ticker_models
from flask import jsonify

def get_googl_data():
    result = []
    try:
        googl_data = ticker_models.GOOGL.query.all()
        result = [
            {
                "record_date": row.record_date
                , "open": row.open
                , "close": row.close
                , "high": row.high
                , "low": row.low
                , "volume": row.volume
                , "vwap": row.vwap
                , "transactions": row.transactions
                , "ticker": "AAPL"
            } for row in googl_data
        ]

        return jsonify(result)
    except Exception as e:
        return jsonify(result)