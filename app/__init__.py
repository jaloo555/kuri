from flask import Flask
from flask.templating import render_template
from flask_cors import CORS

app = Flask(__name__)
app.config.from_object('config')
CORS(app)

@app.route('/')
def index():
  return 'index'

@app.errorhandler(404)
def not_found(error):
  return render_template('404.html'), 404

from app.visualizer.controllers import visualizer as vis_module

app.register_blueprint(vis_module)