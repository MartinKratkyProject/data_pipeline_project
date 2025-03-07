from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# Set up the PostgreSQL URI (Replace with your own DB credentials if needed)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql+psycopg2://airflow:airflow@postgres:5432/postgres'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False  # Disable track modifications to save resources

# Initialize SQLAlchemy
db = SQLAlchemy(app)

# Define the AAPL table model
class AAPL(db.Model):
    __tablename__ = 'AAPL'  # Ensure this matches your table name in the database

    timestamp = db.Column(db.BigInteger, primary_key=True)
    open = db.Column(db.Float)

    def __repr__(self):
        return f"<AAPL timestamp={self.timestamp}, open={self.open}>"

# Basic route for the backend message
@app.route('/')
def index():
    return "This is the backend"

# Route to fetch all rows from the AAPL table
@app.route('/aapl', methods=['GET'])
def get_aapl_data():
    # Fetch all data from the AAPL table
    aapl_data = AAPL.query.all()
    
    # Prepare the response in JSON format
    data = [{"timestamp": row.timestamp, "open": row.open} for row in aapl_data]
    
    return jsonify(data)