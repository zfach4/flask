# -*- coding: utf-8 -*-
from flask import Flask

app = Flask(__name__)

@app.route('/hello')
def hello():
	print(app)
	return "Hello Word"