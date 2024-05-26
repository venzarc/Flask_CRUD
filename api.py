from flask import Flask, make_response, jsonify, request
from flask_mysqldb import MySQL

app = Flask(__name__)
app.config["MYSQL_HOST"] = "127.0.0.1"
app.config["MYSQL_USER"] = "root"
app.config["MYSQL_PASSWORD"] = "1234"
app.config["MYSQL_DB"] = "mydb"
app.config["MYSQL_CURSORCLASS"] = "DictCursor"  

mysql = MySQL(app)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

#to fetch data from the mysql server
def data_fetch(query):
    cur = mysql.connection.cursor()
    cur.execute(query)
    data = cur.fetchall()
    cur.close()
    return data

#get/select functions for the tables
#select function for network infrastructure
@app.route("/network_infrastructure", methods=["GET"])
def get_net():
    query = "SELECT * FROM network_infrastructure"
    data = data_fetch(query)
    return make_response(jsonify(data), 200)

#select function for customers
@app.route("/customers", methods=["GET"])
def get_customer():
    query = "SELECT * FROM customer"
    data = data_fetch(query)
    return make_response(jsonify(data), 200)

#select function for account details
@app.route("/account_details", methods=["GET"])
def get_account():
    query = "SELECT * FROM account_details"
    data = data_fetch(query)
    return make_response(jsonify(data), 200)


if __name__ == "__main__":
    app.run(debug=True)