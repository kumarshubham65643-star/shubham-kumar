from flask import Flask, render_template, request, redirect, url_for, flash
import mysql.connector

app = Flask(__name__)
app.secret_key = "student_management_secret"


# ==================================
# DATABASE CONNECTION
# ==================================

def get_db_connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="1309",
        database="student_management"
    )


# ==================================
# HOME PAGE AND VIEW STUDENTS
# ==================================

@app.route('/')
def home():

    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)

    cursor.execute("SELECT * FROM students ORDER BY id DESC")

    students = cursor.fetchall()

    cursor.close()
    conn.close()

    return render_template(
        'frontend.html',
        students=students,
        edit_student=None
    )


# ==================================
# ADD STUDENT
# ==================================

@app.route('/add', methods=['POST'])
def add_student():

    name = request.form['name']
    email_id = request.form['email_id']
    contact_no = request.form['contact_no']
    address = request.form['address']
    course = request.form['course']
    adhar_no = request.form['adhar_no']

    conn = get_db_connection()
    cursor = conn.cursor()

    query = """
        INSERT INTO students
        (name, email_id, contact_no, address, course, adhar_no)
        VALUES (%s, %s, %s, %s, %s, %s)
    """

    values = (
        name,
        email_id,
        contact_no,
        address,
        course,
        adhar_no
    )

    cursor.execute(query, values)

    conn.commit()

    cursor.close()
    conn.close()

    flash("Student Added Successfully!")

    return redirect(url_for('home'))


# ==================================
# UPDATE STUDENT
# ==================================

@app.route('/update/<int:id>', methods=['GET', 'POST'])
def update_student(id):

    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)

    # Update form submit
    if request.method == 'POST':

        name = request.form['name']
        email_id = request.form['email_id']
        contact_no = request.form['contact_no']
        address = request.form['address']
        course = request.form['course']
        adhar_no = request.form['adhar_no']

        query = """
            UPDATE students
            SET name=%s,
                email_id=%s,
                contact_no=%s,
                address=%s,
                course=%s,
                adhar_no=%s
            WHERE id=%s
        """

        values = (
            name,
            email_id,
            contact_no,
            address,
            course,
            adhar_no,
            id
        )

        cursor.execute(query, values)

        conn.commit()

        cursor.close()
        conn.close()

        flash("Student Updated Successfully!")

        return redirect(url_for('home'))

    # Fetch selected student
    cursor.execute(
        "SELECT * FROM students WHERE id=%s",
        (id,)
    )

    edit_student = cursor.fetchone()

    if edit_student is None:

        cursor.close()
        conn.close()

        return "Student Not Found", 404

    # Fetch all students
    cursor.execute("SELECT * FROM students ORDER BY id DESC")

    students = cursor.fetchall()

    cursor.close()
    conn.close()

    return render_template(
        'frontend.html',
        students=students,
        edit_student=edit_student
    )


# ==================================
# DELETE STUDENT
# ==================================

@app.route('/delete/<int:id>', methods=['POST'])
def delete_student(id):

    conn = get_db_connection()
    cursor = conn.cursor()

    cursor.execute(
        "DELETE FROM students WHERE id=%s",
        (id,)
    )

    conn.commit()

    cursor.close()
    conn.close()

    flash("Student Deleted Successfully!")

    return redirect(url_for('home'))


# ==================================
# RUN APPLICATION
# ==================================

if __name__ == '__main__':
    app.run(debug=True)