#from flask import Flask
from flask import Flask, request
from flask_restful import Resource, Api
from sqlalchemy import create_engine
from json import dumps
import MySQLdb

app = Flask(__name__)

@app.route('/departments')
def departments():
  db = MySQLdb.connect(host="letstestdb.mysql.database.azure.com",user="myadmin@letstestdb",passwd="Welcome12@admin",db="mysampledb")
  conn = db.cursor()
  query = conn.execute("select distinct DEPARTMENT from salaries")
	return {'departments': [i[0] for i in query.cursor.fetchall()]}
  #return 'Hello, World!'

if __name__ == '__main__':
  app.run()
