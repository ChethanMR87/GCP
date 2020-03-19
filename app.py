from flask import Flask,jsonify
import config
import json

app= Flask(__name__)

@app.route('/')
def index():
	return '<h1>Hello!</h1>'
@app.route('/Info')
def info():
			
	jsonString = {
	  "app_name": "flask_app",
	  "version": "1.0",
	  "git_commit_sha":config.git_commit_sha(),
	  "environment": [
		{"service_port":config.port()},
		{"log_level":config.log_level()}
	  ]
	}
	
	return jsonify(jsonString),200