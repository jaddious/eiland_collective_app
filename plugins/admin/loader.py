from flask import Flask, jsonify, render_template, request, redirect, url_for, session, Blueprint, make_response
import flask
from functools import wraps
from six.moves.urllib.parse import urlencode
from globals import get_authentications, make_engine
import json
from sqlalchemy import text

admin = Blueprint('admin', __name__)

engine = make_engine()


def register_as_plugin(app):
  app.register_blueprint(admin, url_prefix='/admin')
  return app

# Authentication Routes (Using Auth0)

def requires_auth(f):
  @wraps(f)
  def decorated(*args, **kwargs):
    if 'profile' not in session:
      # Redirect to Login page here
      return redirect('/admin/login')
    return f(*args, **kwargs)

  return decorated



@admin.route('/callback', methods=['GET', 'POST'])
def callback_handling():
    # Handles response from token endpoint
    auth0 = get_authentications()
    auth0.authorize_access_token()
    resp = auth0.get('userinfo')
    userinfo = resp.json()

    # Store the user information in flask session.
    session['jwt_payload'] = userinfo
    session['profile'] = {
        'user_id': userinfo['sub'],
        'name': userinfo['name'],
        'picture': userinfo['picture'],
        'email': userinfo['email']
    }
    return redirect(url_for('admin.welcome'))

@admin.route('/login')
def login():
    auth0 = get_authentications()
    return auth0.authorize_redirect(redirect_uri=url_for('admin.callback_handling', _external=True))


@admin.route('/logout')
def logout():
    auth0 = get_authentications()
    # Clear session stored data
    session.clear()
    # Redirect user to logout endpoint
    params = {'returnTo': url_for('admin.login', _external=True), 'client_id': '7fNHliipf0XD8pMEcZFrwuhrWbNI7Ual'}
    return redirect(auth0.api_base_url + '/v2/logout?' + urlencode(params))

# Admin Routes

@admin.route('/')
@requires_auth
def welcome():
    return "logged in!"

@admin.route('/test', methods=['POST', 'GET'])
@requires_auth
def test():
    return "succes"


