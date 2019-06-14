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

@app.route('/api/hubsters/<HubbbID>', methods=['DELETE', 'GET'])
def getHubster(HubbbID):
    cursor = connection.cursor()
    if request.method =='GET':
        data = []
        query_string = "SELECT * FROM HUBHUBSTERS WHERE HUBSTERID=:HubbID"
        result = cursor.execute(query_string,HubbID=HubbbID)
        for row in result:
            data.append(row)
            #data.append({'HubsterID': row[0], 'Firstname':row[1], 'lastname':row[2], 'pillarid':row[3],'managerid':row[3],'seat':row[4],'phone':row[5],'email':row[6],'neighborhood':row[7]:'birthday':row[8]})
        return jsonify(status='success', data=data)
      #  return 'ok',200

   # if request.method =='DELETE':

@app.route('/api/hubsters/teams/<pillarrrID>',methods=['GET'])
def getPillarTeam(pillarrrID):
    cursor = connection.cursor()
    if request.method =='GET':
        data = []
        query_string = "SELECT * FROM HUBHUBSTERS WHERE PILLARID=:PillarrID"
        result = cursor.execute(query_string,PillarrID=pillarrrID)
        for row in result:
            data.append(row)
        return jsonify(status='success', data=data)


@app.route('/api/hubsters/Manager/<managerrrID>',methods=['GET'])
def getPillarTeamByManager(managerrrID):
    cursor = connection.cursor()
    if request.method =='GET':
        data = []
        query_string = "SELECT * FROM HUBHUBSTERS WHERE MANAGERID=:managerrID"
        result = cursor.execute(query_string,managerrID=managerrrID)
        for row in result:
            data.append(row)
        return jsonify(status='success', data=data)


#move Put from /api/hubsters endpoint to here?

'''
@app.errorhandler(404)
def not_found(error=None):
    message = {
        'status': 404,
        'message': 'Not Found: ' + request.url,
    }
    resp = jsonify(message)
    resp.status_code = 404

    return resp
'''

@app.route('/api/hubsters', methods=['GET', 'POST', 'PUT'])
def readAndWriteHubsters():
    cursor = connection.cursor()
    if request.method =='GET':
        data=[]
        for row in cursor.execute("SELECT * FROM HUBHUBSTERS"):
            data.append(row)
        return jsonify(status='success', db_version=connection.version, data=data)
    
    if request.method == 'POST':
        json_data = request.get_json(force=True)
        p_FirstName = json_data['FirstName']
        p_LastName = json_data['LastName']
        p_PillarID = json_data['PillarID']
        p_ManagerID = json_data['ManagerID']
        p_Seat = json_data['Seat']
        p_Phone = json_data['Phone']
        p_Neighborhood = json_data['Neighborhood']
        p_Birthday = json_data['Birthday']
        cursor.callproc('INSERTHUBSTER', (p_FirstName, p_LastName, p_PillarID, p_ManagerID, p_Seat, p_Phone, p_Neighborhood, p_Birthday))
        for result in cursor.stored_results():
            print(result.fetchall())
        #NEED TO RETURN p_HubsterID in stored proc and here for update ease
        connection.commit()
        cursor.close()

    if request.method == 'PUT':
        json_data = request.get_json(force=True)
        p_HubsterID = json_data['HubsterID']
        p_FirstName = json_data['FirstName']
        p_LastName = json_data['LastName']
        p_PillarID = json_data['PillarID']
        p_ManagerID = json_data['ManagerID']
        p_Seat = json_data['Seat']
        p_Phone = json_data['Phone']
        p_Neighborhood = json_data['Neighborhood']
        p_Birthday = json_data['Birthday']
        cursor.callproc('UPDATEHUBSTER', (p_HubsterID, p_FirstName, p_LastName, p_PillarID, p_ManagerID, p_Seat, p_Phone, p_Neighborhood, p_Birthday))
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
        json_data = request.get_json(force=True)
        p_MANAGERID = json_data['MANAGERID']
        p_PILLARNAME = json_data['PILLARName']
        cursor.callproc('INSERTPILLAR', (p_MANAGERID, p_PILLARNAME))
        for result in cursor.stored_results():
            print(result.fetchall())
    connection.commit()
    cursor.close()

@app.route('/api/managers', methods=['GET'])
def viewManagers():
    data=[]
    cursor = connection.cursor()
    for row in cursor.execute("SELECT * FROM HUBMANAGERS"):
        data.append(row)
    cursor.close()
    return jsonify(status='success', db_version=connection.version, data=data)

@app.route('/api/rooms', methods=['GET'])
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

The stored procedure below is effectively doing a patch on hubsters, 
https://stackoverflow.com/questions/43612860/update-stored-procedure-only-update-certain-fields-and-leave-others-as-is
this link has SQL SErver syntax on how to make it a PUT, which is what we want. 

create or replace PROCEDURE updateHubster(
p_HubsterID in HUBHUBSTERS.HUBSTERID%type
,p_FirstName in HUBHUBSTERS.FIRSTNAME%type default null 
,p_LastName in HUBHUBSTERS.LASTNAME%type default null
,p_PillarID in HUBHUBSTERS.PILLARID%type default null 
,p_ManagerID in HUBHUBSTERS.MANAGERID%type default null 
,p_Seat in HUBHUBSTERS.SEAT%type default null 
,p_Phone in HUBHUBSTERS.PHONE%type default null 
,p_Neighborhood in HUBHUBSTERS.NEIGHBORHOOD%type default null 
,p_Birthday in HUBHUBSTERS.BIRTHDAY%type default null 
) IS
BEGIN
    UPDATE HUBHUBSTERS set
    FIRSTNAME = p_FirstName,
    LASTNAME = p_LastName,
    PillarID = p_PillarID,
    ManagerID = p_ManagerID,
    Seat = p_Seat,
    Phone = p_Phone,
    Neighborhood = p_Neighborhood,
    Birthday = p_Birthday
    where HUBSTERID = p_HubsterID;
    Commit;
End;

How to call the patch stored procedure (SYNTAX IMPORTANT FOR CALLING STORED PROCS IN SQL DEVELOPER, UPDATEHUBSTER IS THE NAME OF THE STORED PROC):
DECLARE
  P_HUBSTERID NUMBER;
  P_FIRSTNAME VARCHAR2(26);
  P_LASTNAME VARCHAR2(26);
  P_PILLARID NUMBER;
  P_MANAGERID NUMBER;
  P_SEAT NUMBER;
  P_PHONE NUMBER;
  P_NEIGHBORHOOD VARCHAR2(26);
  P_BIRTHDAY VARCHAR2(255);
BEGIN
  P_HUBSTERID := 62;
  P_FIRSTNAME := NULL;
  P_LASTNAME := 'success';
  P_PILLARID := NULL;
  P_MANAGERID := NULL;
  P_SEAT := NULL;
  P_PHONE := NULL;
  P_NEIGHBORHOOD := NULL;
  P_BIRTHDAY := NULL;


  UPDATEHUBSTER(
    P_HUBSTERID => P_HUBSTERID,
    P_FIRSTNAME => P_FIRSTNAME,
    P_LASTNAME => P_LASTNAME,
    P_PILLARID => P_PILLARID,
    P_MANAGERID => P_MANAGERID,
    P_SEAT => P_SEAT,
    P_PHONE => P_PHONE,
    P_NEIGHBORHOOD => P_NEIGHBORHOOD,
    P_BIRTHDAY => P_BIRTHDAY
  );
--rollback; 
END;

PUT stored procedure below for firstname:

create or replace PROCEDURE updateHubster(
p_HubsterID in HUBHUBSTERS.HUBSTERID%type
,p_FirstName in HUBHUBSTERS.FIRSTNAME%type default null 
,p_LastName in HUBHUBSTERS.LASTNAME%type default null
,p_PillarID in HUBHUBSTERS.PILLARID%type default null 
,p_ManagerID in HUBHUBSTERS.MANAGERID%type default null 
,p_Seat in HUBHUBSTERS.SEAT%type default null 
,p_Phone in HUBHUBSTERS.PHONE%type default null 
,p_Neighborhood in HUBHUBSTERS.NEIGHBORHOOD%type default null 
,p_Birthday in HUBHUBSTERS.BIRTHDAY%type default null 
) IS
BEGIN
    UPDATE HUBHUBSTERS set
    FIRSTNAME = CASE WHEN p_FirstName is null then Firstname else p_FirstName END,
    LASTNAME = CASE WHEN p_LastName is null then LastName else p_LastName END,
    PillarID = CASE WHEN p_PillarID is null then PillarID else p_PillarID END,
    ManagerID = CASE WHEN p_ManagerID is null then ManagerID else p_ManagerID END,
    Seat = CASE WHEN p_Seat is null then Seat else p_Seat END,
    Phone = CASE WHEN p_Phone is null then Phone else p_Phone END,
    Neighborhood = CASE WHEN p_Neighborhood is null then Neighborhood else p_Neighborhood END,
    Birthday = CASE WHEN p_Birthday is null then Birthday else p_Birthday END
    where HUBSTERID = p_HubsterID;
    Commit;
End;

'''
