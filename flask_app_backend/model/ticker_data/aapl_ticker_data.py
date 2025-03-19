from model.ticker_models import ticker_models
from flask import jsonify

def get_aapl_data():
    result = []
    try:
        aapl_data = ticker_models.AAPL.query.all()
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
            } for row in aapl_data
        ]

        return jsonify(result)
    except Exception as e:
        return jsonify(result) 
