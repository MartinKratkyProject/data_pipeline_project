from model.ticker_models import ticker_models
from flask import jsonify
from sqlalchemy import desc

def get_home_data():
    try:
        aapl_data = ticker_models.AAPL.query.order_by(desc(ticker_models.AAPL.record_date)).first()
        amzn_data = ticker_models.AMZN.query.order_by(desc(ticker_models.AMZN.record_date)).first()
        googl_data = ticker_models.GOOGL.query.order_by(desc(ticker_models.GOOGL.record_date)).first()
        nvda_data = ticker_models.NVDA.query.order_by(desc(ticker_models.NVDA.record_date)).first()
        tsla_data = ticker_models.TSLA.query.order_by(desc(ticker_models.TSLA.record_date)).first()

        def format_stock_data(stock_obj, ticker):
            if stock_obj:
                return {
                    "record_date": stock_obj.record_date,
                    "open": stock_obj.open,
                    "close": stock_obj.close,
                    "ticker": ticker
                }
            return None

        result = [
            stock for stock in [
                format_stock_data(aapl_data, "AAPL"),
                format_stock_data(amzn_data, "AMZN"),
                format_stock_data(googl_data, "GOOGL"),
                format_stock_data(nvda_data, "NVDA"),
                format_stock_data(tsla_data, "TSLA")
            ] if stock is not None
        ]

        return jsonify(result)
    except Exception as e:
        return jsonify(result)
