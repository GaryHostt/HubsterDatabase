import logging
logging.basicConfig(filename='error.log',level=logging.DEBUG)
logging.debug('This message should go to the log file')
from flask import Flask, jsonify
import cx_Oracle
from passwords import DB, DB_USER, DB_PASSWORD
from flask import render_template
from flask import request
from datetime import datetime
import json


# declare constants for flask app
HOST = '0.0.0.0'
PORT = 5000

# initialize flask application
app = Flask(__name__)

print("Welcome to the Hubster Database API, Bienvenue a la database des hubsters")
print("This API is now connected with a Jenkins CI/CD Pipeline")
print("WELCOME TO FLASHY FRIDAY")

# update below with your db credentials
# put your wallet files in a /wallet/network/admin in the project directory

#DB = '***'
#DB_USER = '***'
#DB_PASSWORD = '***'

connection = cx_Oracle.connect(DB_USER, DB_PASSWORD, DB)
cur = connection.cursor()

@app.route('/api/version', methods=['GET'])
def version():
    return jsonify(status='success', db_version=connection.version)

@app.route('/api/hubsters/<HubbbID>', methods=['DELETE', 'GET'])
def getHubster(HubbbID):
    cursor = connection.cursor()
    if request.method =='GET':
            data = []
            query_string = ("SELECT * FROM HUBHUBSTERS WHERE HUBSTERID=:HubbID")
            result = cursor.execute(query_string,HubbID=HubbbID)
            keys = ('HUBSTERID', 'FIRSTNAME', 'LASTNAME', 'PILLARID', 'MANAGERID', 'SEAT', 'PHONE', 'EMAIL', 'NEIGHBORHOOD', 'BIRTHDAY', "OracleEventOpt", "OutsideEventOpt", "hometown", "picture")
            for row in result:
                data.append(dict(zip(keys,row)))
            jsonObj = json.dumps(data)
            return jsonify(data)


    if request.method =='DELETE':
        data = []
        query_string = "DELETE FROM HUBHUBSTERS WHERE HUBSTERID=:HubbID"
        result = cursor.execute(query_string,HubbID=HubbbID)
        return jsonify(status='success', data=data)     
'''
    if request.method =='GET':
        data = []
        query_string = "SELECT * FROM HUBHUBSTERS WHERE HUBSTERID=:HubbID"
        result = cursor.execute(query_string,HubbID=HubbbID)
        for row in result:
            data.append(row)
            #data.append({'HubsterID': row[0], 'Firstname':row[1], 'lastname':row[2], 'pillarid':row[3],'managerid':row[3],'seat':row[4],'phone':row[5],'email':row[6],'neighborhood':row[7]:'birthday':row[8]})
        return jsonify(status='success', data=data)
      #  return 'ok',200
'''

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

@app.route('/api/hubsters/FirstName/<FirstNameee>',methods=['GET'])
def getHubsterByFirstname(FirstNameee):
    cursor = connection.cursor()
    '''
    if request.method =='GET':
        data = []
        query_string = "SELECT * FROM HUBHUBSTERS WHERE FirstName=:FirstNamee"
        result = cursor.execute(query_string,FirstNamee=FirstNameee)
        for row in result:
            data.append(row)
        return jsonify(status='success', data=data)  
    '''
    if request.method =='GET':
            query_string = ("SELECT * FROM HUBHUBSTERS WHERE FirstName=:FirstNamee")
            result = cursor.execute(query_string,FirstNamee=FirstNameee)
            rows = cursor.fetchall()
            result = []
            keys = ('HUBSTERID', 'FIRSTNAME', 'LASTNAME', 'PILLARID', 'MANAGERID', 'SEAT', 'PHONE', 'EMAIL', 'NEIGHBORHOOD', 'BIRTHDAY')
            for row in rows:
                result.append(dict(zip(keys,row)))
            jsonObj = json.dumps(result)
            return (jsonObj)

@app.route('/api/hubsters/LastName/<LastNameee>',methods=['GET'])
def getHubsterByLastname(LastNameee):
    cursor = connection.cursor()
    if request.method =='GET':
        query_string = ("SELECT * FROM HUBHUBSTERS WHERE LastName=:Lastnamee")
        result = cursor.execute(query_string,LastNamee=LastNameee)
        rows = cursor.fetchall()
        result = []
        keys = ('HUBSTERID', 'FIRSTNAME', 'LASTNAME', 'PILLARID', 'MANAGERID', 'SEAT', 'PHONE', 'EMAIL', 'NEIGHBORHOOD', 'BIRTHDAY')
        for row in rows:
            result.append(dict(zip(keys,row)))
        jsonObj = json.dumps(result)
        return jsonify(jsonObj)
'''
    if request.method =='GET':
        data = []
        query_string = "SELECT * FROM HUBHUBSTERS WHERE LastName=:Lastnamee"
        result = cursor.execute(query_string,LastNamee=LastNameee)
        for row in result:
            data.append(row)
        return jsonify(status='success', data=data)  
'''


@app.route('/api/hubsters/Email/<Emailll>',methods=['GET'])
def getHUBSTERByEmail(Emailll):
    cursor = connection.cursor()
    if request.method =='GET':
        data = []
        query_string = "SELECT * FROM HUBHUBSTERS WHERE Email=:Emaill"
        result = cursor.execute(query_string,Emaill=Emailll)
        keys = ('HUBSTERID', 'FIRSTNAME', 'LASTNAME', 'PILLARID', 'MANAGERID', 'SEAT', 'PHONE', 'EMAIL', 'NEIGHBORHOOD', 'BIRTHDAY','OracleEventOpt', 'OutsideEventOpt', 'hometown', 'picture')
        for row in result:
            data.append(dict(zip(keys,row)))
        jsonObj = json.dumps(data)
        return jsonify(data)

@app.route('/api/hubsters', methods=['GET', 'POST', 'PUT'])
def readAndWriteHubsters():
    cursor = connection.cursor()
    '''
    if request.method =='GET':
        data=[]
        for row in cursor.execute("SELECT * FROM HUBHUBSTERS"):
            data.append(row)
        return jsonify(data=data)
    '''
    if request.method =='GET':
            cursor.execute("SELECT * FROM HUBHUBSTERS Order By FirstName")
            rows = cursor.fetchall()
            result = []
            keys = ('HUBSTERID', 'FIRSTNAME', 'LASTNAME', 'PILLARID', 'MANAGERID', 'SEAT', 'PHONE', 'EMAIL', 'NEIGHBORHOOD', 'BIRTHDAY','OracleEventOpt', 'OutsideEventOpt', 'HOMETOWN', 'picture')
            for row in rows:
                result.append(dict(zip(keys,row)))
            jsonObj = json.dumps(result)
            print (type(jsonObj))
            return jsonify(result)
            
    
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
        p_Email = json_data['Email']
        p_OracleEventOpt = json_data['OracleEventOpt']
        p_OutsideEventOpt = json_data['OutsideEventOpt']
        p_hometown = json_data['hometown']
        p_picture = json_data['picture']
        cursor.callproc('INSERTHUBSTER', (p_FirstName, p_LastName, p_PillarID, p_ManagerID, p_Seat, p_Phone, p_Neighborhood, p_Birthday, p_Email,p_OracleEventOpt, p_OutsideEventOpt, p_hometown, p_picture))
        return jsonify(status='hubster created')
        #for result in cursor.stored_results():
            #print(result.fetchall())
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
        p_Email = json_data['Email']
        p_OracleEventOpt = json_data['OracleEventOpt']
        p_OutsideEventOpt = json_data['OutsideEventOpt']
        p_hometown = json_data['hometown']
        p_picture = json_data['picture']
        cursor.callproc('UPDATEHUBSTER', (p_HubsterID, p_FirstName, p_LastName, p_PillarID, p_ManagerID, p_Seat, p_Phone, p_Neighborhood, p_Birthday, p_Email, p_OracleEventOpt, p_OutsideEventOpt, p_hometown, p_picture))
        return jsonify(status='Hubster updated')
        #lololol
        #for result in cursor.stored_results():
            #print(result.fetchall())
    connection.commit()
    cursor.close()

@app.route('/api/managers/FirstName/<FirstNameee>',methods=['GET'])
def getManagerByFirstname(FirstNameee):
    cursor = connection.cursor()
    if request.method =='GET':
        data = []
        query_string = "SELECT * FROM HUBManagers WHERE FirstName=:FirstNamee"
        result = cursor.execute(query_string,FirstNamee=FirstNameee)
        for row in result:
            data.append(row)
        return jsonify(status='success', data=data)  

@app.route('/api/managers/LastName/<LastNameee>',methods=['GET'])
def getManagerByLastname(LastNameee):
    cursor = connection.cursor()
    if request.method =='GET':
        data = []
        query_string = "SELECT * FROM HUBMANAGERS WHERE LastName=:Lastnamee"
        result = cursor.execute(query_string,LastNamee=LastNameee)
        for row in result:
            data.append(row)
        return jsonify(status='success', data=data) 

@app.route('/api/managers/Email/<Emailll>',methods=['GET'])
def getManagerByEmail(Emailll):
    cursor = connection.cursor()
    if request.method =='GET':
        data = []
        query_string = "SELECT * FROM HUBMANAGERS WHERE Email=:Emaill"
        result = cursor.execute(query_string,Emaill=Emailll)
        for row in result:
            data.append(row)
        return jsonify(status='success', data=data) 

@app.route('/api/managers/<ManagerrrID>', methods=['DELETE', 'GET'])
def getManager(ManagerrrID):
    cursor = connection.cursor()
    if request.method =='GET':
        data = []
        query_string = "SELECT * FROM HUBMANAGERS WHERE MANAGERID=:ManagerrID"
        result = cursor.execute(query_string,MANAGERRID=ManagerrrID)
        for row in result:
            data.append(row)
            #data.append({'HubsterID': row[0], 'Firstname':row[1], 'lastname':row[2], 'pillarid':row[3],'managerid':row[3],'seat':row[4],'phone':row[5],'email':row[6],'neighborhood':row[7]:'birthday':row[8]})
        return jsonify(status='success', data=data)
      #  return 'ok',200

    if request.method =='DELETE':
        data = []
        query_string = "DELETE FROM HUBManagers WHERE MANAGERID=:MANAGERRID"
        result = cursor.execute(query_string,MANAGERRID=MANAGERRRID)
        return jsonify(status='success', data=data)  

@app.route('/api/managers', methods=['GET','PUT'])
def viewAndUpdateManagers():
    cursor = connection.cursor()
    if request.method =='GET':
        data=[]
        cursor = connection.cursor()
        for row in cursor.execute("SELECT * FROM HUBMANAGERS"):
            data.append(row)
        cursor.close()
        return jsonify(status='success', db_version=connection.version, data=data)

    if request.method == 'PUT':
        json_data = request.get_json(force=True)
        p_FirstName = json_data['FirstName']
        p_LastName = json_data['LastName']
        p_ManagerID = json_data['ManagerID']
        p_Office = json_data['Office']
        p_Phone = json_data['Phone']
        p_Email = json_data['Email']
        cursor.callproc('UPDATEMANAGER', (p_FirstName, p_LastName, p_ManagerID, p_Office, p_Phone, p_Email))
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

@app.route('/api/rooms', methods=['GET'])
def viewRooms():
    data=[]
    cursor = connection.cursor()
    for row in cursor.execute("SELECT * FROM HUBROOMS"):
        data.append(row)
    cursor.close()
    return jsonify(status='success', db_version=connection.version, data=data)

@app.route('/api/events', methods=['GET', 'POST'])
def viewAndCreateEvents():
    cursor = connection.cursor()
    if request.method =='GET':
        data=[]
        cursor = connection.cursor()
        keys = ('EVENTID', 'Title', 'DateOfEvent', 'INSIDEOROUTSIDE')
        for row in cursor.execute("SELECT * FROM HUBEVENTS"):
            data.append(dict(zip(keys,row)))
        cursor.close()
        return jsonify(data)

    if request.method =='GET':
            cursor.execute("SELECT * FROM HUBHUBSTERS")
            rows = cursor.fetchall()
            result = []
            keys = ('HUBSTERID', 'FIRSTNAME', 'LASTNAME', 'PILLARID', 'MANAGERID', 'SEAT', 'PHONE', 'EMAIL', 'NEIGHBORHOOD', 'BIRTHDAY','OracleEventOpt', 'OutsideEventOpt', 'HOMETOWN', 'picture')
            for row in rows:
                result.append(dict(zip(keys,row)))
            jsonObj = json.dumps(result)
            print (type(jsonObj))
            return jsonify(result)

    if request.method =='POST':
        json_data = request.get_json(force=True)
        p_EventID = json_data['EventID']
        p_Title = json_data['Title']
        p_Date = json_data['Date']
        p_InsideOrOutside = json_data['InsideOrOutside']
        cursor.callproc('CreateEvent', (p_EventID, p_Title, p_Date, p_InsideOrOutside))
        #need to figure out return, it works, but seems like it doesn't
        for result in cursor.stored_results():
            print(result.fetchall())
        connection.commit()
        cursor.close()

@app.route('/api/events/checkin', methods=['POST'])
def checkinEvent():
    cursor = connection.cursor()
    if request.method == 'POST':
        json_data = request.get_json(force=True)
        p_EventID = json_data['EventID']
        p_Email = json_data['Email']
        cursor.callproc('EventCheckIn', (p_EventID, p_Email))
        #need to figure out return, it works, but seems like it doesn't
        #for result in cursor.stored_results():
            #print(result.fetchall())
        return jsonify(status='Hubster logged')
    connection.commit()
    cursor.close()

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

create or replace PROCEDURE CreateEvent(
    p_EventID in HUBEvents.EventID%type default null 
,p_Title in HUBEvents.Title%type default null
,p_DateOfEvent in HUBEvents.DateOfEvent%type default null

) IS
BEGIN
    INSERT INTO HUBEVENTS ("EVENTID", "TITLE", "DATEOFEVENT")
    VALUES (p_EventID, p_Title, p_DateOfEvent);

    Commit;

End;

create or replace PROCEDURE EventCheckIn(
    p_EventID in HUBEvents.EventID%type default null 
,p_HubsterID in HUBEvents.Title%type default null

) IS
BEGIN
    INSERT INTO HUBEventCheckIn ("EVENTID", "HUBSTERID")
    VALUES (p_EventID, p_HubsterID);

    Commit;

End;


'''
'''
ALL STORED PROCS AS OF JUNE 19

create or replace PROCEDURE insertHubster(
    p_FirstName in HUBHUBSTERS.FIRSTNAME%type default null 
,p_LastName in HUBHUBSTERS.LASTNAME%type default null
,p_PillarID in HUBHUBSTERS.PILLARID%type default null 
,p_ManagerID in HUBHUBSTERS.MANAGERID%type default null 
,p_Seat in HUBHUBSTERS.SEAT%type default null 
,p_Phone in HUBHUBSTERS.PHONE%type default null 
,p_Neighborhood in HUBHUBSTERS.NEIGHBORHOOD%type default null 
,p_Birthday in HUBHUBSTERS.BIRTHDAY%type default null 
,p_Email in HUBHUBSTERS.EMAIL%type default null
,p_OracleEventOpt in HUBHUBSTERS.ORACLEEVENTOPT%type default null
,p_OutsideEventOpt in HUBHUBSTERS.OUTSIDEEVENTOPT%type default null
,p_hometown in HUBHUBSTERS.HOMETOWN%type default null
,p_picture in HUBHUBSTERS.PICTURE%type default null
) IS
BEGIN
    INSERT INTO HUBHUBSTERS ("FIRSTNAME", "LASTNAME", "PILLARID", "MANAGERID", "SEAT", "PHONE", "NEIGHBORHOOD", "BIRTHDAY", "EMAIL", "ORACLEEVENTOPT","OUTSIDEEVENTOPT", "HOMETOWN", "PICTURE")
    VALUES (p_FirstName, p_LastName, p_PillarID, p_ManagerID, p_Seat, p_Phone, p_Neighborhood, p_Birthday, p_Email,p_OracleEventOpt, p_OutsideEventOpt, p_hometown, p_picture);

    Commit;

End;

create or replace PROCEDURE insertPillar(
    p_MANAGERID in HUBPILLARS.MANAGERID%type default null 
,p_PILLARNAME in HUBPILLARS.PILLARNAME%type default null
) IS
BEGIN
    INSERT INTO HUBPILLARS ("MANAGERID","PILLARNAME")
    VALUES (p_ManagerID, p_PillarName);

    Commit;

End;

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
,p_Email in HUBHUBSTERS.EMAIL%type default null 
,p_OracleEventOpt in HUBHUBSTERS.ORACLEEVENTOPT%type default null
,p_OutsideEventOpt in HUBHUBSTERS.OUTSIDEEVENTOPT%type default null
,p_hometown in HUBHUBSTERS.HOMETOWN%type default null
,p_picture in HUBHUBSTERS.PICTURE%type default null
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
    Email = CASE WHEN p_Email is null then Email else p_Email END,
    Birthday = CASE WHEN p_Birthday is null then Birthday else p_Birthday END,
    OracleEventOpt = CASE WHEN p_OracleEventOpt is null then OracleEventOpt else p_OracleEventOpt END,
    OutsideEventOpt = CASE WHEN p_OutsideEventOpt is null then OutsideEventOpt else p_OutsideEventOpt END,
    hometown = CASE WHEN p_hometown is null then HOMETOWN else p_hometown END,
    picture = CASE WHEN p_picture is null then picture else p_picture END
    where HUBSTERID = p_HubsterID;
    Commit;
End;

create or replace PROCEDURE updateManager(
p_FirstName in HUBMANAGERS.FIRSTNAME%type default null 
,p_LastName in HUBMANAGERS.LASTNAME%type default null
,p_ManagerID in HUBMANAGERS.MANAGERID%type default null 
,p_Office in HUBMANAGERS.OFFICE%type default null 
,p_Phone in HUBMANAGERS.PHONE%type default null 
,p_Email in HUBMANAGERS.EMAIL%type default null 
) IS
BEGIN
    UPDATE HUBMANAGERS set
    FIRSTNAME = CASE WHEN p_FirstName is null then Firstname else p_FirstName END,
    LASTNAME = CASE WHEN p_LastName is null then LastName else p_LastName END,
    ManagerID = CASE WHEN p_ManagerID is null then ManagerID else p_ManagerID END,
    Office = CASE WHEN p_Office is null then Office else p_Office END,
    Phone = CASE WHEN p_Phone is null then Phone else p_Phone END,
    Email = CASE WHEN p_Email is null then Email else p_Email END
    where MANAGERID = p_ManagerID;
    Commit;
End;

create or replace PROCEDURE CreateEvent(
    p_EventID in HUBEvents.EventID%type default null 
,p_Title in HUBEvents.Title%type default null
,p_DateOfEvent in HUBEvents.DateOfEvent%type default null
,p_InsideOrOutside in HUBEvents.InsideOrOutside%type default null

) IS
BEGIN
    INSERT INTO HUBEVENTS ("EVENTID", "TITLE", "DATEOFEVENT", "INSIDEOROUTSIDE")
    VALUES (p_EventID, p_Title, p_DateOfEvent, p_InsideOrOutside);

    Commit;

End;

create or replace PROCEDURE EventCheckIn(
    p_EventID in HUBEvents.EventID%type default null 
,p_HubsterID in HUBEvents.Title%type default null

) IS
BEGIN
    INSERT INTO HUBEventCheckIn ("EVENTID", "HUBSTERID")
    VALUES (p_EventID, p_HubsterID);

    Commit;

End;
'''
'''
SEPERATE PROJECT STORED PROCS ON SAME DB:
create or replace PROCEDURE GET_MARKET
(
    p_zipcode IN VARCHAR2,
    p_clientName OUT VARCHAR2,
    p_marketName OUT VARCHAR2,
    p_salesRepName OUT VARCHAR2,
    p_salesRepEmail OUT VARCHAR2,
    p_salesRepPhoneNum OUT VARCHAR2
)
AS
BEGIN
    SELECT name, client, salesRepName, salesRepEmail, salesRepPhoneNum INTO p_marketName, p_clientName, p_salesRepName, p_salesRepEmail, p_salesRepPhoneNum FROM Market WHERE Market.zipcode = p_zipcode;
END;
'''
