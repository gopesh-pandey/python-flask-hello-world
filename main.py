from flask import Flask
import MySQLdb

app = Flask(__name__)

@app.route('/departments')
def listdept():
 # Open database connection
 db = MySQLdb.connect("letstestdb.mysql.database.azure.com","myadmin@letstestdb","Welcome12@admin","mysampledb" )
 # prepare a cursor object using cursor() method
 #cursor = db.cursor()
# cursor.execute( "select * from salaries where Department='%s'"%department_name.upper())
# result = {'data': [dict(zip(tuple (query.keys()) ,i)) for i in query.cursor]}
# return result
 return 'Hello, World...Will list db soon!'

if __name__ == '__main__':
  app.run()
