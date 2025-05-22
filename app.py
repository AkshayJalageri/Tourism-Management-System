from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# SQLite database configuration
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///bookings.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# Define the Booking model
class Booking(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    age = db.Column(db.Integer)
    gender = db.Column(db.String(10))
    destination = db.Column(db.String(100))
    flight = db.Column(db.String(100))
    hotel = db.Column(db.String(100))
    days = db.Column(db.Integer)

# Create the database (only first time)
with app.app_context():
    db.create_all()

@app.route("/", methods=["GET", "POST"])
def index():
    result = None
    if request.method == "POST":
        # Extract form data
        name = request.form["name"]
        age = int(request.form["age"])
        gender = request.form["gender"]
        destination = request.form["destination"]
        flight = request.form["flight"]
        hotel = request.form["hotel"]
        days = int(request.form["days"])

        # Create and save the booking
        booking = Booking(
            name=name, age=age, gender=gender,
            destination=destination, flight=flight,
            hotel=hotel, days=days
        )
        db.session.add(booking)
        db.session.commit()

        # Show data on result section
        result = booking

    return render_template("index.html", result=result)

if __name__ == "__main__":
    app.run(debug=True)
