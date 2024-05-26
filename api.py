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
@app.route("/accounts", methods=["GET"])
def get_account():
    query = "SELECT * FROM account_details"
    data = data_fetch(query)
    return make_response(jsonify(data), 200)

#select specific network based on id
@app.route("/network_infrastructure/<int:id>", methods=["GET"])
def get_network_by_id(id):
    data = data_fetch("""select * from network_infrastructure
where network_id = {}""".format(id))
    return make_response(jsonify(data), 200)

#select specific customer based on id
@app.route("/customers/<int:id>", methods=["GET"])
def get_customer_by_id(id):
    data = data_fetch("""select * from customer
where customer_id = {}""".format(id))
    return make_response(jsonify(data), 200)

#select specific account based on id
@app.route("/accounts/<int:id>", methods=["GET"])
def get_account_by_id(id):
    data = data_fetch("""select * from account_details
where account_id = {}""".format(id))
    return make_response(jsonify(data), 200)

@app.route("/customers", methods=["POST"])
def add_customer():
    cur = mysql.connection.cursor()
    info = request.get_json()
    customer_id = info["customer_id"]
    first_name = info["first_name"]
    last_name = info["last_name"]
    contact_number = info["contact_number"]
    network_id_fk = info ["network_id_fk"]
    customer_address = info["customer_address"]
    
    cur.execute(
        """ INSERT INTO customer (contact_number, customer_address, customer_id, 
         first_name, last_name, network_id_fk ) VALUE (%s, %s, %s, %s, %s, %s)""",
        (contact_number, customer_address, customer_id, 
         first_name, last_name, network_id_fk ),
    )
    mysql.connection.commit()
    print("row(s) affected :{}".format(cur.rowcount))
    rows_affected = cur.rowcount
    cur.close()
    return make_response(
        jsonify(
            {"message": "customer added successfully", "rows_affected": rows_affected}
        ),
        201,
    )


if __name__ == "__main__":
    app.run(debug=True)