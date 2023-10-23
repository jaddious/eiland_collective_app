from flask import Flask, jsonify, render_template, request, redirect, Blueprint
from jinja2 import Environment, FileSystemLoader
import jinja2
import json
import pandas as pd
import os
from globals import make_engine, make_socket

# Create Flask App

app = Flask(__name__)

app.secret_key = 'PvpdpBraYKhuB9ErHuUpOAIeZ98xUrou8Xg'

engine = make_engine()

socketio = make_socket(app)



def plugin_loader(app):
    plugins = [x for x in os.listdir('./plugins')
             if os.path.isdir('./plugins/' + x)]
    for plugin in plugins:
        module = __import__('plugins.' + str(plugin) + '.loader', fromlist=['register_as_plugin'])
        app = module.register_as_plugin(app)
    return app

app = plugin_loader(app)

# Load Plugins

@app.errorhandler(404)
def page_not_found(e):
    # note that we set the 404 status explicitly
    return render_template('404.html'), 404

if __name__ == "__main__":
    app.run(debug=True)
    #socketio.run(app) to make socket work

