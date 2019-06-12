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
cur = connection.cursor()

#functional? APIs below

@app.route('/api/version', methods=['GET'])
def version():
    return jsonify(status='success', db_version=connection.version)

@app.route('/api/hubsters', methods=['GET', 'POST'])
def readAndWriteHubsters():
    cursor = connection.cursor()
    if request.method =='GET':
        data=[]
        for row in cursor.execute("SELECT * FROM HUBHUBSTERS"):
            data.append(row)
        return jsonify(status='success', db_version=connection.version, data=data)
    
    if request.method == 'POST':
        p_FirstName = request.form['FirstName']
        p_LastName = request.form['LastName']
        p_PillarID = request.form['PillarID']
        p_ManagerID = request.form['ManagerID']
        p_Seat = request.form['Seat']
        p_Phone = request.form['Phone']
        p_Neighborhood = request.form['Neighborhood']
        p_Birthday = request.form['Birthday']
        cursor.callproc('INSERTHUBSTER', (p_FirstName, p_LastName, p_PillarID, p_ManagerID, p_Seat, p_Phone, p_Neighborhood, p_Birthday))
        for result in cursor.stored_results():
            print(result.fetchall())
    connection.commit()
    cursor.close()

@app.route('/api/pillars', methods=['GET', 'POST'])
def readAndWritePillars():
    cursor = connection.cursor()
    if request.method =='GET':
        data=[]
        cursor = connection.cursor()
        for row in cursor.execute("SELECT * FROM HUBPILLARS"):
            data.append(row)
        cursor.close()
        return jsonify(status='success', db_version=connection.version, data=data)
    
    if request.method == 'POST':
        p_MANAGERID = request.form['MANAGERID']
        p_PILLARNAME = request.form['PILLARName']
        cursor.callproc('INSERTPILLAR', (p_MANAGERID, p_PILLARNAME))
        for result in cursor.stored_results():
            print(result.fetchall())
    connection.commit()
    cursor.close()

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

if __name__ == '__main__':
    app.run(host=HOST,
            debug=True,
            port=PORT)


##CRUD stored procedures in database stored here
'''
CREATE OR REPLACE PROCEDURE insertPillar(
    p_MANAGERID in HUBPILLARS.MANAGERID%type default null 
,p_PILLARNAME in HUBPILLARS.PILLARNAME%type default null
) IS
BEGIN
    INSERT INTO HUBPILLARS ("MANAGERID","PILLARNAME")
    VALUES (p_ManagerID, p_PillarName);
    
    Commit;
    
End;

CREATE OR REPLACE PROCEDURE insertHubster(
    p_FirstName in HUBHUBSTERS.FIRSTNAME%type default null 
,p_LastName in HUBHUBSTERS.LASTNAME%type default null
,p_PillarID in HUBHUBSTERS.PILLARID%type default null 
,p_ManagerID in HUBHUBSTERS.MANAGERID%type default null 
,p_Seat in HUBHUBSTERS.SEAT%type default null 
,p_Phone in HUBHUBSTERS.PHONE%type default null 
,p_Neighborhood in HUBHUBSTERS.NEIGHBORHOOD%type default null 
,p_Birthday in HUBHUBSTERS.BIRTHDAY%type default null 
) IS
BEGIN
    INSERT INTO HUBHUBSTERS ("FIRSTNAME", "LASTNAME", "PILLARID", "MANAGERID", "SEAT", "PHONE", "NEIGHBORHOOD", "BIRTHDAY")
    VALUES (p_FirstName, p_LastName, p_PillarID, p_ManagerID, p_Seat, p_Phone, p_Neighborhood, p_Birthday);
    
    Commit;
    
End;

'''
