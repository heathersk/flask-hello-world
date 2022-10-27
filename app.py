import os
from flask import Flask, jsonify, abort, render_template
from flask import request
import psycopg2

conn = psycopg2.connect("dbname=flask-hello-world.db user=heatherkoehler")

cur = conn.cursor()


app = Flask(__name__)




@app.route('/greeting')
def hello_world():
    return render_template('index.html')



@app.route('/v1/templates/create', methods=['POST', 'GET'])
def create_template():
    if request.method == 'POST':
        #if (request.form['mentee']),
        mentee = request.method['nm']
        print(request.form)
        print('the name was that was received is this: %s', request.form['name'])
        return ''
    elif request.method == 'GET':
        return render_template('form.html'), 200

@app.route('/v1/templates/create', methods=['POST', 'GET'])
def create_template():
    if request.method == 'POST':
        link = request.method['url']
        print(request.form)
        print('Here is the link to a YouTube video: %s', request.form['link'])
    elif request.method == 'GET':
        return render_template('form.html'), 200

@app.route('/v1/templates/create', methods=['POST', 'GET'])
def create_template():
    if request.method == 'POST':
        description = request.method['text']
        print(request.form)
        print('This is a description of the video: %s', request.form[description])
    elif request.method == 'GET':
        return render_template('form.html'), 200

@app.route('/v1/templates/create', methods=['POST'])
def add_template():
    data = request.get_json()
    if not data:
        abort(400)

    cur = conn.cursor()
    cur.execute("INSERT INTO template (name, YouTube_link, description) values (%s, %s, %s)")
    conn.commit()
    cur.close()
    conn.close()
    return '', 200



