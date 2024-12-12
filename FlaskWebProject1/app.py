from flask import Flask
from config import Config
from database import MYSQLinstance
from routes import init_routes

app = Flask(__name__)
app.config.from_object(Config)

# Initialize the MySQL database connection
mysql = MYSQLinstance.get_instance(app)

# Set up routes
init_routes(app, mysql)

if __name__ == '__main__':
    app.run(debug=True)
