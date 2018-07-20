from flask import Flask, jsonify
from flask import Flask, request

app = Flask(__name__)

db = MySQLdb.connect(host="letstestdb.mysql.database.azure.com",user="myadmin@letstestdb",passwd="Welcome12@admin",db="mysampledb")

cursor = db.cursor()

 
@app.route("/dept")
def hello():
    #return "Hello World!"
    cursor.execute("SELECT distinct department FROM salaries")
    print 'after query'
    r = [dict((cursor.description[i][0], value)
              for i, value in enumerate(row)) for row in cursor.fetchall()]
    return jsonify({'myCollection' : r})
    db.close()

if __name__ == "__main__":
    app.run()
	
