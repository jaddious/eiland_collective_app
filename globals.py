from flask import Flask, jsonify, render_template, request, redirect, Blueprint, current_app
import flask
from sqlalchemy import create_engine
import io
from urllib.parse import quote_plus, urlencode
from authlib.integrations.flask_client import OAuth
from flask_socketio import SocketIO, emit
import io
import os

def get_authentications():
    oauth = OAuth(flask.current_app)
    auth0 = oauth.register(
        'auth0',
        client_id='7fNHliipf0XD8pMEcZFrwuhrWbNI7Ual',
        client_secret='KpCXUzf25_9yl3qPN9AAMPyEwJVj7T6iSd5PaLObpj00KlAfosm_mlllxDy9TGiB',
        api_base_url='https://round-art-6737.eu.auth0.com',
        access_token_url='https://round-art-6737.eu.auth0.com/oauth/token',
        authorize_url='https://round-art-6737.eu.auth0.com/authorize',
        client_kwargs={
            'scope': 'openid profile email',
        },
    )
    return auth0

def make_engine():
    engine = create_engine("postgresql://eheckvjtzjqgay:614dc6bd385edb1da94935be3f366b42316857464467de97d3bf8565d9e96a2e@ec2-54-75-184-144.eu-west-1.compute.amazonaws.com:5432/dcgvqt1nj6o0d3")
    return engine

def make_socket(app):
    socketio = SocketIO(app)
    return socketio





