# Tourism-Management-System
A simple web-based Tourism Management System built with **Flask**, **HTML**, **CSS**, and **SQLite**. This project allows users to book tours by entering personal and travel details, which are then stored in a SQLite database.

## 🌐 Live Preview

*Not hosted yet* – clone and run locally to preview.

## 📁 Project Structure

```

├── app.py                # Main Flask application
├── bookings.db           # SQLite database storing booking records
├── bookings.json         # Sample booking data in JSON format
├── templates/
│   └── index.html        # HTML template for the main page
├── static/
│   ├── style.css         # CSS styling for the UI (optional)

````

## 🚀 Features

- Collects user details such as:
  - Name
  - Age
  - Gender
  - Destination
  - Flight
  - Hotel
  - Duration of stay
- Stores bookings in a SQLite database
- Displays submitted booking details upon form submission

## 🛠️ Technologies Used

- Python (Flask Framework)
- SQLite
- HTML5 & CSS3
- Jinja2 (Flask templating engine)

## 🧪 How to Run the Project

1. **Clone the Repository**

   ```bash
   git clone https://github.com/yourusername/tourism-management-system.git
   cd tourism-management-system
````

2. **Create Virtual Environment (Optional but Recommended)**

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install Dependencies**

   ```bash
   pip install flask flask_sqlalchemy
   ```

4. **Run the Application**

   ```bash
   python app.py
   ```

5. **Open in Browser**

   Navigate to `http://127.0.0.1:5000/` to view the app.

## 📦 Sample Data

You can refer to `bookings.json` for example booking entries.

## 📌 Future Improvements

* Add user authentication
* Enable viewing/editing/deleting of bookings
* Add cost calculations
* Include admin dashboard

```
