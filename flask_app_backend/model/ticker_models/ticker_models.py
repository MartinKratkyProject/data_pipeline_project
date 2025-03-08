from util.connection.db_connection import db

class AAPL(db.Model):
    __tablename__ = 'AAPL'

    open = db.Column(db.Float)
    high = db.Column(db.Float)
    low = db.Column(db.Float)
    close = db.Column(db.Float)
    volume = db.Column(db.Float)
    vwap = db.Column(db.Float)
    timestamp = db.Column(db.BigInteger, primary_key=True)
    transactions = db.Column(db.BigInteger)

    def __repr__(self):
        return f"<AAPL open={self.open}, high={self.high}, low={self.low}, close={self.close}, volume={self.volume}, vwap={self.vwap}, timestamp={self.timestamp}, transactions={self.transactions}>"
    

class AMZN(db.Model):
    __tablename__ = 'AMZN'

    open = db.Column(db.Float)
    high = db.Column(db.Float)
    low = db.Column(db.Float)
    close = db.Column(db.Float)
    volume = db.Column(db.Float)
    vwap = db.Column(db.Float)
    timestamp = db.Column(db.BigInteger, primary_key=True)
    transactions = db.Column(db.BigInteger)

    def __repr__(self):
        return f"<AMZN open={self.open}, high={self.high}, low={self.low}, close={self.close}, volume={self.volume}, vwap={self.vwap}, timestamp={self.timestamp}, transactions={self.transactions}>"
    

class GOOGL(db.Model):
    __tablename__ = 'GOOGL'

    open = db.Column(db.Float)
    high = db.Column(db.Float)
    low = db.Column(db.Float)        
    close = db.Column(db.Float)
    volume = db.Column(db.Float)
    vwap = db.Column(db.Float)
    timestamp = db.Column(db.BigInteger, primary_key=True)
    transactions = db.Column(db.BigInteger)

    def __repr__(self):
        return f"<GOOGL open={self.open}, high={self.high}, low={self.low}, close={self.close}, volume={self.volume}, vwap={self.vwap}, timestamp={self.timestamp}, transactions={self.transactions}>"   
    

class NVDA(db.Model):
    __tablename__ = 'NVDA'

    open = db.Column(db.Float)
    high = db.Column(db.Float)
    low = db.Column(db.Float)
    close = db.Column(db.Float)
    volume = db.Column(db.Float)
    vwap = db.Column(db.Float)
    timestamp = db.Column(db.BigInteger, primary_key=True)
    transactions = db.Column(db.BigInteger)

    def __repr__(self):
        return f"<NVDA open={self.open}, high={self.high}, low={self.low}, close={self.close}, volume={self.volume}, vwap={self.vwap}, timestamp={self.timestamp}, transactions={self.transactions}>"
    

class TSLA(db.Model):
    __tablename__ = 'TSLA'

    open = db.Column(db.Float)
    high = db.Column(db.Float)
    low = db.Column(db.Float)
    close = db.Column(db.Float)
    volume = db.Column(db.Float)
    vwap = db.Column(db.Float)
    timestamp = db.Column(db.BigInteger, primary_key=True)
    transactions = db.Column(db.BigInteger)

    def __repr__(self):
        return f"<TSLA open={self.open}, high={self.high}, low={self.low}, close={self.close}, volume={self.volume}, vwap={self.vwap}, timestamp={self.timestamp}, transactions={self.transactions}>"
