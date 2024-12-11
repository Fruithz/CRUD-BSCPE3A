from flask import Flask, render_template, request,redirect, url_for, flash
from flask_mysqldb import MySQL
app  = Flask(__name__)

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'crudapplication'

mysql = MySQL(app)
app.secret_key = "flash message"


@app.route('/') # '/' is the main url of the site 
def index():
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM employees") # this is so that the database items are read
    data = cur.fetchall()
    cur.close()

    return render_template('main.html', employees = data)


@app.route('/insert', methods = ['POST'])  # /insert is the new url used for inserting new datas in the DB
def insert(): 
    if request.method == "POST":
        flash("data inserted succesfully.")
        
        #this connects the variables name to our SQL database
        name = request.form['name']
        email = request.form['email']
        phone = request.form['phone']

        cur = mysql.connection.cursor()
        
        # this is the part where INSERT is the command used to add new datas in the table, and %s is used as a placeholder values
        cur.execute("INSERT INTO Employees (name, email, phone) VALUES (%s, %s, %s)", (name,email,phone))
        mysql.connection.commit()
        
        #this redirects our page back to the main page
        return redirect(url_for('index'))



@app.route('/update', methods = ['POST', 'GET']) # /update is the url used for updating current values on the table
def update():
    if request.method == "POST":
        
        #this connects the variables name to our SQL database
        id_data = request.form['id']
        name = request.form['name']
        email = request.form['email']
        phone = request.form['phone']

        cur = mysql.connection.cursor()
        #this is a more than one line command to update current employees status, 
        # set their new names, emails , etc, and finding its current id 
        cur.execute("""

            UPDATE employees
            SET name=%s, email=%s, phone=%s
            WHERE id=%s

        """, (name,email,phone,id_data))
        
        flash("Data Updated succesfully")
        mysql.connection.commit()
        
        # Where after this redirects it back to the main page
        return redirect(url_for('index'))

@app.route('/delete/<string:id_data>', methods = ['POST', 'GET'])
def delete(id_data):

    flash("data deleted succesfully")

    cur = mysql.connection.cursor()
    
    #this is to delete anything
    cur.execute("DELETE FROM employees WHERE id = %s", (id_data))
    mysql.connection.commit()
    return redirect(url_for('index'))
