from flask import Flask
  2 import mysql.connector
  3
  4 app = Flask(__name__)
  5
  6 def get_db_connection():
  7         connection = mysql.connector.connect(
  8          host="db",
  9          user="root",
 10          password="example",
 11          database="test_db"
 12         )
 13         return connection
 14
 15 @app.route('/')
 16 def hello_world():
 17         connection = get_db_connection()
 18         cursor = connection.cursor()
 19         cursor.execute("SELECT 'Hello, Docker!'")
 20         result = cursor.fetchone()
 21         connection.close()
 22         return str(result[0])
 23
 24 if __name__ == "__main__":
 25         app.run(host='0.0.0.0')