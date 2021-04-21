import os
my_secret = os.environ['API_KEY']

from flask import Flask
from flask import render_template
from flask import jsonify


app = Flask(__name__)

@app.route('/')
def hello_world():
  return render_template("index.html")

if __name__ == '__main__':
  app.run(host='0.0.0.0',port=8080)
