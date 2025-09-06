import mysql.connector
from flask import Flask,Request,jsonify

app = Flask(__name__)

db=mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="empolyee"
)
cursor=db.cursor()
@app.route('/users')
def get_users():
    cursor.execute("select * from users")
    return jsonify (cursor.fetchall())


if __name__=='__main__':
    app.run(debug=True)

@app.route('/createuser', method=['post','get'])
def add_user():
    if(Request.method!='post'):
        return'''<form method="post">
    username:<input type="text" name="name" required><br>
    password:<input type="text" email="email" required<br>
    <input type="submit" value"register">
    </form>
    '''
    else:
        name=Request.form["name"]
        email=Request.form["email"]
        cursor.execute("INSERT INTO student")