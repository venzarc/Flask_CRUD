from flask import Flask, make_response, jsonify, request
from flask_mysqldb import MySQL

app = Flask(__name__)
app.config["MYSQL_HOST"] = "127.0.0.1"
app.config["MYSQL_USER"] = "root"
app.config["MYSQL_PASSWORD"] = "1234"
app.config["MYSQL_DB"] = "mydb"
app.config["MYSQL_CURSORCLASS"] = "DictCursor"  

mysql = MySQL(app)

#home page
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
@app.route("/networks", methods=["GET"])
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
@app.route("/networks/<int:id>", methods=["GET"])
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

#adding new customer
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

#adding new network
@app.route("/networks", methods=["POST"])
def add_network():
    cur = mysql.connection.cursor()
    info = request.get_json()
    network_id = info["network_id"]
    grid_location = info["grid_location"]
    grid_name = info["grid_name"]

    cur.execute(
        """ INSERT INTO network_infrastructure (network_id, grid_location, grid_name) VALUE (%s, %s, %s)""",
        (network_id, grid_location, grid_name),
    )
    mysql.connection.commit()
    print("row(s) affected :{}".format(cur.rowcount))
    rows_affected = cur.rowcount
    cur.close()
    return make_response(
        jsonify(
            {"message": "network added successfully", "rows_affected": rows_affected}
        ),
        201,
    )

#adding new account
@app.route("/accounts", methods=["POST"])
def add_account():
    cur = mysql.connection.cursor()
    info = request.get_json()
    account_id = info["account_id"]
    service_type = info["service_type"]
    customer_id_fk = info["customer_id_fk"]

    
    cur.execute(
        """ INSERT INTO account_details (account_id,customer_id_fk, service_type) VALUE (%s, %s, %s)""",
        (account_id, customer_id_fk,service_type),
    )
    mysql.connection.commit()
    print("row(s) affected :{}".format(cur.rowcount))
    rows_affected = cur.rowcount
    cur.close()
    return make_response(
        jsonify(
            {"message": "account added successfully", "rows_affected": rows_affected}
        ),
        201,
    )

#update customer
@app.route("/customers/<int:id>", methods=["PUT"])
def update_customer(id):
    cur = mysql.connection.cursor()
    info = request.get_json()
    first_name = info["first_name"]
    last_name = info["last_name"]
    cur.execute(
        """ UPDATE customer SET first_name = %s, last_name = %s WHERE customer_id = %s """,
        (first_name, last_name, id),
    )
    mysql.connection.commit()
    rows_affected = cur.rowcount
    cur.close()
    return make_response(
        jsonify(
            {"message": "customer updated successfully", "rows_affected": rows_affected}
        ),
        200,
    )

#update networks
@app.route("/networks/<int:id>", methods=["PUT"])
def update_network(id):
    cur = mysql.connection.cursor()
    info = request.get_json()
    grid_location = info["grid_location"]
    grid_name = info["grid_name"]
    cur.execute(
        """ UPDATE network_infrastructure SET grid_location = %s, grid_name = %s WHERE network_id = %s """,
        (grid_location, grid_name, id),
    )
    mysql.connection.commit()
    rows_affected = cur.rowcount
    cur.close()
    return make_response(
        jsonify(
            {"message": "network updated successfully", "rows_affected": rows_affected}
        ),
        200,
    )

#update accounts
@app.route("/accounts/<int:id>", methods=["PUT"])
def update_account(id):
    cur = mysql.connection.cursor()
    info = request.get_json()
    service_type = info["service_type"]
    cur.execute(
        """ UPDATE account_details SET service_type = %s WHERE account_id = %s """,
        (service_type, id),
    )
    mysql.connection.commit()
    rows_affected = cur.rowcount
    cur.close()
    return make_response(
        jsonify(
            {"message": "account updated successfully", "rows_affected": rows_affected}
        ),
        200,
    )

#delete network
@app.route("/networks/<int:id>", methods=["DELETE"])
def delete_network(id):
    cur = mysql.connection.cursor()
    cur.execute(""" DELETE FROM network_infrastructure where network_id = %s """, (id,))
    mysql.connection.commit()
    rows_affected = cur.rowcount
    cur.close()
    return make_response(
        jsonify(
            {"message": "network deleted successfully", "rows_affected": rows_affected}
        ),
        200,
    )

#uri parameter for networks
@app.route("/networks/format", methods=["GET"])
def get_params_net():
    fmt = request.args.get('id')
    foo = request.args.get('aaaa')
    return make_response(jsonify({"format":fmt, "foo":foo}),200)

#uri parameter for customers
@app.route("/customers/format", methods=["GET"])
def get_params_customers():
    fmt = request.args.get('id')
    foo = request.args.get('aaaa')
    return make_response(jsonify({"format":fmt, "foo":foo}),200)

#uri parameter for accounts
@app.route("/accounts/format", methods=["GET"])
def get_params_account():
    fmt = request.args.get('id')
    foo = request.args.get('aaaa')
    return make_response(jsonify({"format":fmt, "foo":foo}),200)


if __name__ == "__main__":
    app.run(debug=True)