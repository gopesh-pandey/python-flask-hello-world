from flask import Flask
app = Flask(__name__)

@app.route('/departments')
def listdept():
  return 'Hello, World...Will list db soon!'

if __name__ == '__main__':
  app.run()
