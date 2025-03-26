from model.ticker_models import ticker_models
from flask import jsonify
from sqlalchemy import desc, asc, and_
from datetime import datetime, timedelta

def get_first_trading_day_query(model, start_date):
    """Fetch the first trading day's record after the given start_date"""
    return model.query.filter(model.record_date >= start_date).order_by(asc(model.record_date)).first()

def get_home_data():
    try:
        latest_data = {
            "AAPL": ticker_models.AAPL.query.order_by(desc(ticker_models.AAPL.record_date)).first(),
            "AMZN": ticker_models.AMZN.query.order_by(desc(ticker_models.AMZN.record_date)).first(),
            "GOOGL": ticker_models.GOOGL.query.order_by(desc(ticker_models.GOOGL.record_date)).first(),
            "NVDA": ticker_models.NVDA.query.order_by(desc(ticker_models.NVDA.record_date)).first(),
            "TSLA": ticker_models.TSLA.query.order_by(desc(ticker_models.TSLA.record_date)).first(),
        }

        today = datetime.today().date()
        week_start = today - timedelta(days=today.weekday())
        month_start = today.replace(day=1)

        result = []

        for ticker, stock_obj in latest_data.items():
            if stock_obj:
                week_open_record = get_first_trading_day_query(getattr(ticker_models, ticker), week_start)
                month_open_record = get_first_trading_day_query(getattr(ticker_models, ticker), month_start)

                result.append({
                    "ticker": ticker,
                    "record_date": stock_obj.record_date,
                    "open": stock_obj.open,
                    "close": stock_obj.close,
                    "week_open": week_open_record.open if week_open_record else stock_obj.open,
                    "month_open": month_open_record.open if month_open_record else stock_obj.open,
                })

        return jsonify(result)

    except Exception as e:
        print(f"Error fetching stock data: {e}")
        return jsonify([])
