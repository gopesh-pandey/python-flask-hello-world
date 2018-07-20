from flask import Flask, jsonify
from flask import Flask, request
from flask_restful import Resource, Api
#from sqlalchemy import create_engine
from json import dumps
import MySQLdb


app = Flask(__name__)

db = MySQLdb.connect(host="letstestdb.mysql.database.azure.com",user="myadmin@letstestdb",passwd="Welcome12@admin",db="mysampledb")

cursor = db.cursor()

# Execute SQL select statement


@app.route('/v')
def get():

    cursor.execute("SELECT distinct department FROM salaries")
    print 'after query'
    r = [dict((cursor.description[i][0], value)
              for i, value in enumerate(row)) for row in cursor.fetchall()]
    return jsonify({'myCollection' : r})
    db.close()
if __name__ == '__main__':
    app.run(debug=True)
