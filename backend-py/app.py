# A very simple Flask Hello World app for you to get started with...
from flask import Flask, request
from api_controller import ApiController

app = Flask(__name__)

api = ApiController()

@app.route('/')
def hello_world():
    return api.hello_world()

@app.route('/myip')
def my_ip():
    ip = request.headers.getlist("X-Forwarded-For")[0]
    return ip