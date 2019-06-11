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

'''

# api endpoint returning version of database from automonous data warehouse

# update sql based on your database tables

@app.route('/api/test', methods=['GET'])
def test():
    data=[]
    cursor = connection.cursor()
    for row in cursor.execute("SELECT * FROM HUBPILLARS"):
        data.append(row)
    cursor.close()
    return jsonify(status='success', db_version=connection.version, data=data)


likely need SQLAlchemy with this
class Hubster(Model):
    HubsterID = Column(db.Integer, primary_key=True)
    FirstName = Column(db.String(220),unique=False)
    LastName = Column(db.String(220),unique=False)
    PillarID = Column(db.Integer, foreign_key=True)
    ManagerID = Column(db.Integer, foreign_key=True)
    Seat = db.Column(db.Integer,unique=False)
    Phone = db.Column(db.String(220),unique=True)
    Email = db.Column(db.String(220),unique=True)
    Neighborhood = db.Column(db.String(220),unique=False)
    Birthday = db.Column(db.String(220),unique=False)

    def __init__(self, FirstName,LastName, Pillar, Seat, Phone, Email, Neighborhood, Birthday):
        self.FirstName = FirstName
        self.LastName = LastName
        self.Pillar = PillarID
        self.Seat = Seat
        self.Phone = Phone
        self.Email = Email
        self.Neighborhood = Neighborhood
        self.Birthday = Birthday

class Managers(Model):
    ManagerID = db.Column(db.Integer, primary_key=True)
    FirstName = db.Column(db.String(220),unique=False)
    LastName = db.Column(db.String(220),unique=False)
    Office = db.Column(db.String(220),unique=False)
    Phone = db.Column(db.String(220),unique=True)
    Email = db.Column(db.String(220),unique=True)

class Pillars(Model):
    PillarID = db.Column(db.Integer, primary_key=True)
    PillarName = db.Column(db.String(220),unique=False)
    ManagerID = db.Column(db.Integer, foreign_key=True)

class Rooms(Model):
    HubRoomNumber = db.Column(db.Integer, primary_key=True)
    Capacity = db.Column(db.Integer, unique=False)

    if you go the SQLalchemy route:
          
        #hubster = Hubster(newFirstName, newLastName, newEmail)

@app.route('/api/version', methods=['GET'])
def version():
        cur.execute ("SELECT * FROM v$version")
        row = cur.fetchone()
        print ("server version:")

    '''
#SQLAlchemy stuff above
#functional? APIs below

@app.route('/api/version', methods=['GET'])
def version():
    return jsonify(status='success', db_version=connection.version)

@app.route('/api/hubsters4', methods=['POST'])
def readAndWriteHubsters4():
    cursor = connection.cursor()
    if request.method == 'POST':
        p_MANAGERID = request.form['MANAGERID']
        p_PILLARNAME = request.form['PILLARName']
        cursor.callproc('INSERTPILLAR', (p_MANAGERID, p_PILLARNAME))
        for result in cursor.stored_results():
            print(result.fetchall())
    connection.commit()
    cursor.close()

@app.route('/api/hubsters3', methods=['POST'])
def readAndWriteHubsters3():
    cursor = connection.cursor()
    if request.method == 'POST':
        data = request.get_json()
        p_MANAGERID = data['ManagerID']
        p_PILLARNAME = data['PillarName']
        results=cursor.callproc('HUBPILLARS_TAPI.ins', (p_MANAGERID, p_PILLARNAME))
        return (results)
    connection.commit()
    cursor.close()

@app.route('/api/hubsters2', methods=['POST'])
def readandWriteHubsters2():
    cursor = connection.cursor()
    if request.method == 'POST':
        FirstName = request.form['FirstName']
        LastName = request.form['LastName']
        Email = request.form['Email']
        Seat = request.form['Seat']
        Phone = request.form['Phone']
        Neighborhood = request.form['Neighborhood']
        Birthday = request.form['Birthday']
        try:
            cursor.execute("INSERT INTO HUBHUBSTERS (FirstName, LastName, Seat, Phone, Email, Neighborhood, Birthday) VALUES (%a, %b, %c, %d, %e, %f, %g)", {"a":FirstName, "b":LastName, "c":Seat, "d":Phone, "e":Email, "f":Neighborhood, "g":Birthday})
        except cx_Oracle.DatabaseError as e:
            error, = e.args
            if error.code == 955:
                print('Table already exists')
            if error.code == 1031:
                print("Insufficient privileges - are you sure you're using the owner account?")
            if error.code == 1036:
                return "You couldn't live with your failure, and where did that bring you? Back to me"
            print(error.code)
            print(error.message)
            print(error.context)
    connection.commit()
    cursor.close()
    return "blue dogs run"

@app.route('/api/hubsters', methods=['GET', 'POST'])
def readAndWriteHubsters():
    cursor = connection.cursor()
    if request.method =='GET':
        data=[]
        
        for row in cursor.execute("SELECT * FROM HUBHUBSTERS"):
            data.append(row)
        return jsonify(status='success', db_version=connection.version, data=data)

    if request.method =='POST':
        FirstName = request.form['FirstName']
        LastName = request.form['LastName']
        Email = request.form['Email']
        Seat = request.form['Seat']
        Phone = request.form['Phone']
        Neighborhood = request.form['Neighborhood']
        Birthday = request.form['Birthday']
        cursor.execute("INSERT INTO HUBHUBSTERS (FirstName, LastName, Seat, Phone, Email, Neighborhood, Birthday) VALUES ('Santa', 'Claus', 9999999, 1234, 'email@email.com', 'Sawtelle', '12345')")
    connection.commit()
    cursor.close()
    return "yellow dogs run"
##old working apis
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
