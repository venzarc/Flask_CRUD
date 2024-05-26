# Flask_CRUD
<br>
<hr>
<p align="center">
This is a web application that deals with a MYSQL server allowing the user integrate it into the web
  It is very easy to use and the functions made can be used as basis for creating more functions
</p>
<hr>
<br>


## Features
- Select and view all field values in a table 
- Select and view specific field values by mentioning their unique id
- Add new field values
- Select inner join customer and networks to show the reclosers where the customers are in
- Update and edit field values
- Deletion of field values

## Installation 
-- First install python then after installing python add it to your enviroment variable
After that install flask
```bash
pip install flask-mysqldb
```
After installing flask you must now create a virtual enviroment 
```bash
python -m venv {folder_name}
```
You can copy the api.py file here then run it on the IDE

-- Then you would to install MYSQL
It can be installed here:
https://dev.mysql.com/downloads/installer/
Then install a database design tool I used MYSQL Workbench it can be installed from here:
https://dev.mysql.com/downloads/workbench/
The ERD and the backup of the database is also here and it can be downloaded to be used for the REST api

-- This also uses an application that test api's I used postman installed from here:
https://www.postman.com/downloads/?utm_source=postman-home


## TODO
- Open a database design tool to open the server
- Open a terminal and then type python api.py
- It will say that it is Running on http://127.0.0.1:5000
- Go to that link

## Here are the commands 
-- To display the tables
- http://127.0.0.1:5000/customers
- http://127.0.0.1:5000/networks
- http://127.0.0.1:5000/accounts
  
-- To display a specific field value
- http://127.0.0.1:5000/customers/<int:id>
- http://127.0.0.1:5000/networks/<int:id>
- http://127.0.0.1:5000/accounts/<int:id>

-- To display specific customers within a specific recloser
- http://127.0.0.1:5000/customers/<int:id>/networks

-- Adding new field values (open postman) 
When adding a network http://127.0.0.1:5000/networks [POST]
```bash
{
    "grid_location": "{}",
    "grid_name": "{}",
    "network_id": {} 
}
```
When adding a customer http://127.0.0.1:5000/customers [POST]
```bash
{
    "first_name": "{}",
    "last_name": "{}",
     "customer_id": {},
     "contact_number": {},
     "customer_address": "{}",
     "network_id_fk": {}
}
```
When adding an account http://127.0.0.1:5000/accounts [POST]
```bash
{
    "account_id": {},
    "customer_id_fk" : {},
    "service_type": "{}"

}
```
When editing a customer http://127.0.0.1:5000/customers/<int:id> [PUT]
```bash
{
    "first_name": "{}",
    "last_name": "{}"
}
```
When editing a network http://127.0.0.1:5000/networks/<int:id> [PUT]
```bash
{
    "grid_location": "{}",
    "grid_name": "{}"
}
```
When editing an account http://127.0.0.1:5000/accounts/<int:id> [PUT]
```bash
{
     "service_type": "{}"
}
```
Deleting a network http://127.0.0.1:5000/networks/<int:id> [DELETE]



