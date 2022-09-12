from flask import Flask, jsonify, request, Response, make_response, jsonify
import json
import mysql.connector

app = Flask(__name__)

class FoodTruck:
    def __init__(self, name, points):
        self.name = name
        self.points = points

        def printTruck(self):
            print("The name is %s", self.name)

playerinsertTable = ("INSERT INTO mysqltutorial.player "
"(`_id`, points)"
"VALUES (%s, %s)")

#database connect
username = "veloAdmin@velosql-server"
hst = "velosql-server.mysql.database.azure.com"
port = "3306"
db = "mysqltutorial"
pwd = "password12!"



@app.route("/updateusertable", methods=['POST', 'GET'])
def updateUserTable():
    print("function call")    

    # x = request.get_data()
    # data = json.loads(x)
    # print(data)
    # id = data["id"]
    # name = data["name"]
    # points = data["points"]


    try:
        print(username)
        cnx = mysql.connector.connect(user=username, password=pwd, host=hst, database=db)
        cursor = cnx.cursor()
        
        query = ("INSERT INTO mysqltutorial.player(`_id`,name,points) VALUES (%s, %s, %s)")
        # insertStuff = (id, name, points)
        insertStuff = ('6', 'Chris', '8591')
        cursor.execute(query, insertStuff)
        cnx.commit()
        print("Successfully added to db")
        return 'OK', 200

    except (Exception, mysql.connector.Error) as error:
        if(cnx):
            print("Failed to insert record into mobile table", error)
            return 'Not OK', 400

    finally:
        #closing database connection.
        if(cnx):
            cursor.close()
            cnx.close()
            print("MySQL connection is closed")
            return 'OK', 200

    #logging.debug("Status message: %s", cursor.statusmessage)
    return 'OK', 200 


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)