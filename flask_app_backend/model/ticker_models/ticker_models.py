from util.connection.db_connection import db

class AAPL(db.Model):
    __tablename__ = 'vw_aapl'

    open = db.Column(db.Float)
    high = db.Column(db.Float)
    low = db.Column(db.Float)
    close = db.Column(db.Float)
    volume = db.Column(db.Float)
    vwap = db.Column(db.Float)
    # timestamp = db.Column(db.BigInteger, primary_key=True)
    transactions = db.Column(db.BigInteger)
    record_date = db.Column(db.Date, primary_key=True)

    def __repr__(self):
        return f"<AAPL open={self.open}, high={self.high}, low={self.low}, close={self.close}, volume={self.volume}, vwap={self.vwap}, transactions={self.transactions}, record_date={self.record_date}>"
    

class AMZN(db.Model):
    __tablename__ = 'vw_amzn'

    open = db.Column(db.Float)
    high = db.Column(db.Float)
    low = db.Column(db.Float)
    close = db.Column(db.Float)
    volume = db.Column(db.Float)
    vwap = db.Column(db.Float)
    # timestamp = db.Column(db.BigInteger, primary_key=True)
    transactions = db.Column(db.BigInteger)
    record_date = db.Column(db.Date, primary_key=True)

    def __repr__(self):
        return f"<AMZN open={self.open}, high={self.high}, low={self.low}, close={self.close}, volume={self.volume}, vwap={self.vwap}, transactions={self.transactions}, record_date={self.record_date}>"
    

class GOOGL(db.Model):
    __tablename__ = 'vw_googl'

    open = db.Column(db.Float)
    high = db.Column(db.Float)
    low = db.Column(db.Float)        
    close = db.Column(db.Float)
    volume = db.Column(db.Float)
    vwap = db.Column(db.Float)
    # timestamp = db.Column(db.BigInteger, primary_key=True)
    transactions = db.Column(db.BigInteger)
    record_date = db.Column(db.Date, primary_key=True)

    def __repr__(self):
        return f"<GOOGL open={self.open}, high={self.high}, low={self.low}, close={self.close}, volume={self.volume}, vwap={self.vwap}, transactions={self.transactions}, record_date={self.record_date}>"   
    

class NVDA(db.Model):
    __tablename__ = 'vw_nvda'

    open = db.Column(db.Float)
    high = db.Column(db.Float)
    low = db.Column(db.Float)
    close = db.Column(db.Float)
    volume = db.Column(db.Float)
    vwap = db.Column(db.Float)
    # timestamp = db.Column(db.BigInteger, primary_key=True)
    transactions = db.Column(db.BigInteger)
    record_date = db.Column(db.Date, primary_key=True)

    def __repr__(self):
        return f"<NVDA open={self.open}, high={self.high}, low={self.low}, close={self.close}, volume={self.volume}, vwap={self.vwap}, transactions={self.transactions}, record_date={self.record_date}>"
    

class TSLA(db.Model):
    __tablename__ = 'vw_tsla'

    open = db.Column(db.Float)
    high = db.Column(db.Float)
    low = db.Column(db.Float)
    close = db.Column(db.Float)
    volume = db.Column(db.Float)
    vwap = db.Column(db.Float)
    # timestamp = db.Column(db.BigInteger, primary_key=True)
    transactions = db.Column(db.BigInteger)
    record_date = db.Column(db.Date, primary_key=True)

    def __repr__(self):
        return f"<TSLA open={self.open}, high={self.high}, low={self.low}, close={self.close}, volume={self.volume}, vwap={self.vwap}, transactions={self.transactions}, record_date={self.record_date}>"
