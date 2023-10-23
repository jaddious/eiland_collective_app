from flask import Flask, jsonify, render_template, request, redirect, url_for, session, Blueprint, make_response
import flask
import json
import pandas as pd
import os
from globals import make_engine, make_socket
from sqlalchemy import text
from datetime import datetime
from flask_socketio import SocketIO, emit
import requests
import xmltodict




eilands = Blueprint('eilands', __name__)

engine = make_engine()


def register_as_plugin(app):
  app.register_blueprint(eilands, url_prefix='/eilands')
  global socketio
  socketio = make_socket(app)
  return app

@eilands.route('/', methods=["GET"])
def eilandsmap():
    ip=str(request.remote_addr)
    return render_template("./eilands/index.html")

@eilands.route('/<id>')
def api_eilands(id):
    with engine.connect() as connection:
        eiland = connection.execute(text("select * from eilands where id='"+id+"'"))
    return render_template('eilands/eiland.html', eiland=eiland.first())

@eilands.route('/all')
def api_eiland():
    with engine.connect() as connection:
        eilands = pd.DataFrame(connection.execute(text("select id,name,moat_situation,x,y,created_by,confirmation from eilands")))
        eilands.columns =['id', 'name', 'moat_situation', 'x', 'y','created_by','confirmation']
        response = eilands.to_json(orient='records')
    return make_response(response, 200)

@eilands.route('/regionlimits')
def api_regionlimits():
    regionlimits = json.load(open('static/eilands/data/regionlimits3.geojson'))
    global socketio
    socketio = make_socket(app)
    return make_response(regionlimits, 200)

@eilands.route('/neweiland', methods=["post"])
def api_neweiland():
    x = str(request.form["x"])
    y = str(request.form["y"])
    name = str(request.form["name"])
    moat_situation = str(request.form["moat_situation"])
    address = str(xmltodict.parse(requests.get('https://nominatim.openstreetmap.org/reverse?format=xml&lat='+y+'&lon='+x+'&zoom=18&addressdetails=1').content).get('reversegeocode').get('result').get('#text'))
    with engine.connect() as connection:
        connection.execute(text("Insert Into eilands(x,y,name,moat_situation, confirmation, created_by, date_created, created_by_ip, adress) Values('"+x+"','"+y+"','"+name+"','"+moat_situation+"','unconfirmed','Public','"+str(datetime.now())+"','"+str(request.remote_addr)+"','"+address+"');"))
    socketio.emit('new_eiland', {'x':request.form['x'],'y':request.form['y']}, broadcast=True)
    return make_response("success", 200)

@eilands.route('/count', methods=["get"])
def eilandscount():
    with engine.connect() as connection:
        count = pd.DataFrame(connection.execute(text("SELECT COUNT(*) FROM eilands")))
        count.columns =['count']
    return make_response(str(count['count'][0]), 200)

@eilands.route('/temp', methods=["get"])
def temp():
    with engine.connect() as connection:
        eilands = pd.DataFrame(connection.execute(text("select id,x,y,adress from eilands where adress is Null")))
        eilands.columns = ['id', 'x', 'y','adress']
        for index, row in eilands.iterrows():
            print(row['adress'])
            address = str(xmltodict.parse(requests.get('https://nominatim.openstreetmap.org/reverse?format=xml&lat='+str(row['y'])+'&lon='+str(row['x'])+'&zoom=18&addressdetails=1').content).get('reversegeocode').get('result').get('#text'))
            connection.execute(text("update eilands set adress='"+address+"'where id='"+str(row['id'])+"'"))
    return "done!"

@eilands.route('/address/<x>/<y>', methods=["get"])
def eilandsadress(x,y):
    return make_response(str(address), 200)

@eilands.route('/docs', methods=["get"])
def eilandsdocs():
    return render_template('eilands/docs.html')
