from flask import Flask
from flask_mysqldb import MySQL

app = Flask(__name__)

# MySQL configurations
app.config['MYSQL_HOST'] = '192.168.0.160'
app.config['MYSQL_USER'] = 'my_user'
app.config['MYSQL_PASSWORD'] = 'EmersonFitipaldi'
app.config['MYSQL_DB'] = 'mydatabase'
app.config['MYSQL_CURSORCLASS'] = 'DictCursor'

# Initialize MySQL
mysql = MySQL(app)


@app.route('/')
def test_db_connection():
    try:
        # Check the database connection
        cursor = mysql.connection.cursor()
        cursor.execute('SELECT 1')
        result = cursor.fetchone()
        cursor.close()

        return 'Successfully connected to the MySQL database'

    except Exception as e:
        return f'Failed to connect to the MySQL database: {str(e)}'


if __name__ == '__main__':
    app.run(host='0.0.0.0')
