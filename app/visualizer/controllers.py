from flask import Flask, request
from flask import Blueprint

visualizer = Blueprint('viz', __name__, url_prefix='/viz')

@visualizer.route('/hello', methods=['GET'])
def hello():
  return "hello"