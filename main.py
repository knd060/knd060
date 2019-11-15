from flask import Flask, flash, request, redirect, render_template, send_from_directory, jsonify
import pandas as pd



app = Flask(__name__, static_folder='static')
# app.secret_key = 'secretkey'
# app.config['SESSION_TYPE'] = 'filesystem'


@app.route('/')
def my_form():
    return render_template('index.html')