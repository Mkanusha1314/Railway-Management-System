from flask import Flask, render_template, request, redirect, url_for, flash
import mysql.connector

app = Flask(__name__)
app.secret_key = "Mithun@123"  # Replace with a secure key

# MySQL connection
def connect_to_db():
    return mysql.connector.connect(
        host="localhost",
        user="root",  # Replace with your MySQL username
        password="password",  # Replace with your MySQL password
        database="RailwayDB"
    )

# Home route
@app.route('/')
def index():
    return render_template('index.html')

# User Management
@app.route('/add_user', methods=['GET', 'POST'])
def add_user():
    if request.method == 'POST':
        conn = connect_to_db()
        cursor = conn.cursor()
        sql = "INSERT INTO User (First_name, Last_name, Age, Gender, Phone_no, City, State, Email, Password) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)"
        val = (
            request.form['first_name'], request.form['last_name'], request.form['age'],
            request.form['gender'], request.form['phone_no'], request.form['city'],
            request.form['state'], request.form['email'], request.form['password']
        )
        cursor.execute(sql, val)
        conn.commit()
        conn.close()
        flash("User added successfully!", "success")
        return redirect(url_for('index'))
    return render_template('add_user.html')

# Ticket Booking
@app.route('/book_ticket', methods=['GET', 'POST'])
def book_ticket():
    if request.method == 'POST':
        conn = connect_to_db()
        cursor = conn.cursor()
        sql = "INSERT INTO Ticket_Booking (User_ID, Train_no, Source_stationid, Destination_stationid, Booking_date, Journey_date, Seat_no, Class, Fare, Payment_status, Booking_status) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
        val = (
            request.form['user_id'], request.form['train_no'], request.form['source_station'],
            request.form['destination_station'], request.form['booking_date'], request.form['journey_date'],
            request.form['seat_no'], request.form['class'], request.form['fare'],
            "Pending", "Booked"
        )
        cursor.execute(sql, val)
        conn.commit()
        conn.close()
        flash("Ticket booked successfully!", "success")
        return redirect(url_for('index'))
    return render_template('book_ticket.html')

if __name__ == '__main__':
    app.run(debug=True)
