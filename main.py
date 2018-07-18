from flask import Flask, jsonify
from flaskext.mysql import MySQL

app = Flask(__name__)
mysql = MySQL()

# MySQL configurations
app.config['MYSQL_DATABASE_USER'] = 'myadmin@letstestdb'
app.config['MYSQL_DATABASE_PASSWORD'] = 'Welcome12@admin'
app.config['MYSQL_DATABASE_DB'] = 'mysampledb'
app.config['MYSQL_DATABASE_HOST'] = 'letstestdb.mysql.database.azure.com'

mysql.init_app(app)

@app.route('/v')
def get():
    cur = mysql.connect().cursor()
    cur.execute('''select * from mysampledb.salaries''')
    r = [dict((cur.description[i][0], value)
              for i, value in enumerate(row)) for row in cur.fetchall()]
    return jsonify({'myCollection' : r})

if __name__ == '__main__':
    app.run()
