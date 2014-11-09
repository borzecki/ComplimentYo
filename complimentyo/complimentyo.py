# -*- coding: utf-8 -*-
from flask import Flask, request, render_template
import requests

app = Flask(__name__)
app.config.from_envvar('COMPLIMENTYO_SETTINGS')

api_token = app.config['YO_TOKEN']
YO_API = "https://api.justyo.co/yo/"


def send_yo(username, link):
    requests.post( YO_API,
        data={'api_token': api_token, 'username': username, 'link': link
    })


@app.route('/')
def main():
    return render_template('index.html')


@app.errorhandler(404)
def handle_error(e):
    return render_template('404.html')


@app.route('/response')
def response():
    taxi_number = request.args.get('msg')
    stand_name = request.args.get('name')
    return render_template('response.html',
                           phone_number=taxi_number,
                           stand_name=stand_name)


@app.route('/yo')
def yo():
    """Handle callback request"""
    username = request.args.get('username')
    if username:
        link = 'http://emergencycompliment.com/'
        send_yo(username, link)
        return 'OK'
    return 'NOTOK'
