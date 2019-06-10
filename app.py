from flask import Flask, jsonify
import cx_Oracle
from passwords import DB, DB_USER, DB_PASSWORD
from flask import render_template
from flask import request

# declare constants for flask app
HOST = '0.0.0.0'
PORT = 5000

# initialize flask application
app = Flask(__name__)

print("Welcome to the Hubster Database API, Bienvenue a la database des hubsters")
print("This API is now connected with a Jenkins CI/CD Pipeline")

# update below with your db credentials
# put your wallet files in a /wallet/network/admin in the project directory

#DB = '***'
#DB_USER = '***'
#DB_PASSWORD = '***'

connection = cx_Oracle.connect(DB_USER, DB_PASSWORD, DB)

# api endpoint returning version of database from automonous data warehouse
@app.route('/api/version', methods=['GET'])
def version():
    return jsonify(status='success', db_version=connection.version)
    
# sample api endpoint returning data from ATP
# update sql based on your database tables

@app.route('/api/test', methods=['GET'])
def test():
    data=[]
    cursor = connection.cursor()
    for row in cursor.execute("SELECT * FROM HUBPILLARS"):
        data.append(row)
    cursor.close()
    return jsonify(status='success', db_version=connection.version, data=data)

#api endpoints from original above this line
#VIEW/GET APIs below

@app.route('/api/view/hubsters', methods=['GET'])
def viewHubsters():
    data=[]
    cursor = connection.cursor()
    for row in cursor.execute("SELECT * FROM HUBHUBSTERS"):
        data.append(row)
    cursor.close()
    return jsonify(status='success', db_version=connection.version, data=data)

@app.route('/api/view/pillars', methods=['GET'])
def viewPillars():
    data=[]
    cursor = connection.cursor()
    for row in cursor.execute("SELECT * FROM HUBPILLARS"):
        data.append(row)
    cursor.close()
    return jsonify(status='success', db_version=connection.version, data=data)

@app.route('/api/view/managers', methods=['GET'])
def viewManagers():
    data=[]
    cursor = connection.cursor()
    for row in cursor.execute("SELECT * FROM HUBMANAGERS"):
        data.append(row)
    cursor.close()
    return jsonify(status='success', db_version=connection.version, data=data)

@app.route('/api/view/rooms', methods=['GET'])
def viewRooms():
    data=[]
    cursor = connection.cursor()
    for row in cursor.execute("SELECT * FROM HUBROOMS"):
        data.append(row)
    cursor.close()
    return jsonify(status='success', db_version=connection.version, data=data)

#CREATE/POST APIs below IN DEVELOPMENT

@app.route('/api/create/hubster', methods=['POST'])
def createHubster():
    data=[]
    cursor = connection.cursor()
    for row in cursor.execute("SELECT * FROM HUBHUBSTERS"):
        data.append(row)
    cursor.close()
    return jsonify(status='success', db_version=connection.version, data=data)


@app.route('/api/create/pillar', methods=['POST'])
def home():
    if request.form:
        print(request.form)
    return render_template("home.html")

#UPDATE/PUT APIs below


if __name__ == '__main__':
    app.run(host=HOST,
            debug=True,
            port=PORT)
