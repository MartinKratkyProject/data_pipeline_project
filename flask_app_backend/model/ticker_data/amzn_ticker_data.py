from model.ticker_models import ticker_models
from flask import jsonify

def get_amzn_data():
    result = []
    try:
        amzn_data = ticker_models.AMZN.query.all()
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
            } for row in amzn_data
        ]

        return jsonify(result)
    except Exception as e:
        return jsonify(result)