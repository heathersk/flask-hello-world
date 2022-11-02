import os
from flask import Flask, jsonify, abort, render_template
from flask import request, url_for
import psycopg2
from jinja2 import environment, FileSystemLoader

DATABASE_URL = os.environ['DATABASE_URL']


app = Flask(__name__)


def get_db_conn():
    return psycopg2.connect(DATABASE_URL, sslmode='require')

@app.route('/greeting')
def hello_world():
    return render_template('index.html')



@app.route('/v1/templates/create', methods=['POST', 'GET'])
def create_template():
    if request.method == 'POST':
        #if (request.form['mentee']),
        title = request.form['title']
        print(request.form)
        print('the name was that was received is this: %s', request.form['title'])

        link = request.form['youtube_link']
        print(request.form)
        print('Here is the link to a YouTube video: %s', request.form['youtube_link'])

        description = request.form['description']
        print(request.form)
        add_template(title, link, description)
        return ''
    elif request.method == 'GET':
        return render_template('form.html'), 200


def add_template(title, youtube_link, description):
    conn = get_db_conn()
    cur = conn.cursor()
    query = (
        "insert into template (title, youtube_link, description) values (%s, %s, %s)")
    cur.execute(query, (title, youtube_link, description))
    conn.commit()
    cur.close()

@app.route('/v1/templates/<template_id>')
def view_template(template_id):
    conn = get_db_conn()
    cur = conn.cursor()
    query = (
        "select id, title, youtube_link, description "

        "from template "

        "where id = %s "
    )
    cur.execute(query, (template_id,))
    data = cur.fetchone()
    '''
    entries = []
    for id, title, youtube_link, description in data:
        entries.append({
            'id': id,
            'title': title,
            'youtube_link': youtube_link,
            'description': description

        })
    '''
    return render_template('view.html')
    return '', 200
    

'''
    select title, youtube_link, description
    from template
    where id = 'edd0cf94-5a20-11ed-8e45-0adf2b4a8b95';

    retrieve the above data, fetchone (I think)
    create a new HTML page/template, pass the above data to the template
'''


@app.route('/v1/templates/view')
def show_templates():
    conn = get_db_conn()
    cur = conn.cursor()
    cur.execute ('select id, title, description from template order by id desc')
    data = cur.fetchall()
    entries = []
    for id, title, description in data:
        entries.append({
            'id': id,
            'title': title,
            'description': description
        })
    return render_template('show_templates.html', entries=entries)



'''
    environment= 
   environment(loader=FileSystemLoader("templates/"))
   template= environment.get_template("")

   for mentee in mentees:
    filename = 
    f"message_{mentee['name'].lower()}.txt"
    content = template.render(
        mentee,
    )
    with open(filename, mode="w", encoding="utf-8") as message
'''







