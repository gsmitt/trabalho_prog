from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy 
import os 
from flask_cors import CORS

app = Flask(__name__)  
CORS(app)
path = os.path.dirname(os.path.abspath(__file__)) 
arquivobd = os.path.join(path, "cavalos.db") 

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///"+arquivobd 
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False 
db = SQLAlchemy(app)