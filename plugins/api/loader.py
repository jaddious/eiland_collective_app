from flask import Flask, jsonify, render_template, request, redirect, url_for, session, Blueprint, make_response
import flask
import json
import pandas as pd
import os
from globals import make_engine
from sqlalchemy import text


api = Blueprint('api', __name__)

engine = make_engine()


def register_as_plugin(app):
  app.register_blueprint(api, url_prefix='/api')
  return app


