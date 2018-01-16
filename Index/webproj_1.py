from flask import Flask
from flask import request
from flask_bootstrap import Bootstrap
from flask import render_template

app = Flask(__name__)
Bootstrap(app)
@app.route('/test', methods = ['get'])
def home_1():
    return render_template('base.html')
if __name__ == '__main__':
	app.run(host = '127.0.0.1', port = 5000)