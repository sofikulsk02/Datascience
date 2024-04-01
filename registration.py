from registration import Flask, render_template, request, redirect
import mysql.connector

app = Flask(__name__)

# MySQL Configuration
mysql_connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password=" ",
    database="registration_db"
)
cursor = mysql_connection.cursor()


@app.route('/')
def registration_form():
    return render_template('register.html')


@app.route('/register', methods=['POST'])
def register():
    student_name = request.form['student_name']
    father_name = request.form['father_name']
    mother_name = request.form['mother_name']
    phone_number = request.form['phone_number']
    email = request.form['email']
    date_of_birth = request.form['date_of_birth']
    address = request.form['address']
    blood_group = request.form['blood_group']
    department = request.form['department']
    course = request.form['course']
    password = request.form['password']

    query = "INSERT INTO users (student_name, father_name, mother_name, phone_number, email, date_of_birth, address, blood_group, department, course, password) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
    values = (student_name, father_name, mother_name, phone_number, email, date_of_birth, address, blood_group, department, course, password)
    cursor.execute(query, values)
    mysql_connection.commit()

    return redirect('/')


if __name__ == '__main__':
    app.run(debug=True)
