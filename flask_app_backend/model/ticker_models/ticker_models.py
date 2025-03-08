from util.connection.db_connection import db

class AAPL(db.Model):
    __tablename__ = 'AAPL'

    timestamp = db.Column(db.BigInteger, primary_key=True)
    open = db.Column(db.Float)
    close = db.Column(db.Float)

    def __repr__(self):
        return f"<AAPL timestamp={self.timestamp}, open={self.open}, close={self.close}>"
    
class AMZN(db.Model):
    __tablename__ = 'AMZN'

    timestamp = db.Column(db.BigInteger, primary_key=True)
    open = db.Column(db.Float)
    close = db.Column(db.Float)

    def __repr__(self):
        return f"<AMZN timestamp={self.timestamp}, open={self.open}, close={self.close}>"
