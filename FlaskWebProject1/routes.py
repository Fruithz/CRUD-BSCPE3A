from flask import render_template, request, redirect, url_for, flash

def init_routes(app, mysql):
    @app.route('/')
    def index():
        cur = mysql.connection.cursor()
        cur.execute("SELECT * FROM employees")
        data = cur.fetchall()
        cur.close()
        return render_template('main.html', employees=data)

    @app.route('/insert', methods=['POST'])
    def insert():
        if request.method == "POST":
            name = request.form['name']
            email = request.form['email']
            phone = request.form['phone']

            cur = mysql.connection.cursor()
            cur.execute("INSERT INTO Employees (name, email, phone) VALUES (%s, %s, %s)", (name, email, phone))
            mysql.connection.commit()
            cur.close()

            flash("Data inserted successfully.")
            return redirect(url_for('index'))

    @app.route('/update', methods=['POST', 'GET'])
    def update():
        if request.method == "POST":
            id_data = request.form['id']
            name = request.form['name']
            email = request.form['email']
            phone = request.form['phone']

            cur = mysql.connection.cursor()
            cur.execute("UPDATE employees SET name=%s, email=%s, phone=%s WHERE id=%s", (name, email, phone, id_data))
            mysql.connection.commit()
            cur.close()

            flash("Data updated successfully.")
            return redirect(url_for('index'))

    @app.route('/delete/<string:id_data>', methods=['POST', 'GET'])
    def delete(id_data):
        cur = mysql.connection.cursor()
        cur.execute("DELETE FROM employees WHERE id = %s", (id_data,))
        mysql.connection.commit()
        cur.close()

        flash("Data deleted successfully.")
        return redirect(url_for('index'))
