from flask import Flask, request, jsonify, Response, abort
import sqlite3, flask, time, datetime, random

app = Flask(__name__)
app.config["DEBUG"] = True


def dict_factory(cursor, row):
    d = {}
    for idx, col in enumerate(cursor.description):
        d[col[0]] = row[idx]
    return d


@app.route('/', methods=['GET'])
def home():
    return '''<h1>Reddit</h1>
<p>WeLcOmE tO rEdDiT</p>'''


@app.route('/api/v1/resources/users/all', methods=['GET'])
def api_all():
    conn = sqlite3.connect('useraccount.db')
    conn.row_factory = dict_factory
    cur = conn.cursor()
    all_users = cur.execute('SELECT * FROM useraccount;').fetchall()

    return jsonify(all_users)


@app.errorhandler(404)
def page_not_found(e):
    return "<h1>404</h1><p>The resource could not be found.</p>", 404


@app.route('/api/v1/resources/users/all', methods=['POST'])
def create_user():
    request_json = request.get_json()
    Email = request_json.get('Email')
    User = request_json.get('User')
    Karma = request_json.get('Karma')

    # query_parameters = request.args
    # Email = query_parameters.get('Email')
    # User = query_parameters.get('User')
    # Karma = query_parameters.get('Karma')
    # query = ''' INSERT INTO useraccount VALUES(?,?,?) '''
    # to_filter = []
    # if Email:
    #     # query += ' Email=? AND'
    #     to_filter.append(Email)
    # if User:
    #     # query += ' published=? AND'
    #     to_filter.append(User)
    # if Karma:
    #     # query += ' author=? AND'
    #     to_filter.append(Karma)

    conn = sqlite3.connect('useraccount.db')
    cur = conn.cursor()

    response_content = cur.execute("INSERT INTO useraccount VALUES(?,?,?)", (Karma, User, Email))
    conn.commit()
    # return jsonify(response_content)
    return Response(response_content, status=201, mimetype='application/json')


@app.route('/api/v1/resources/users/email', methods=['PUT'])
def update_email():
    request_json = request.get_json()
    User = request_json.get('User')
    Email = request_json.get('Email')

    conn = sqlite3.connect('useraccount.db')
    cur = conn.cursor()
    response_content = cur.execute("UPDATE useraccount SET Email=? WHERE User=?", (Email, User))
    conn.commit()
    return Response(response_content, status=200, mimetype='application/json')


@app.route('/api/v1/resources/post/all_post', methods=['GET'])
def all_post():
    conn = sqlite3.connect('post.db')
    conn.row_factory = dict_factory
    cur = conn.cursor()
    all_post = cur.execute('SELECT * FROM userpost;').fetchall()
    return jsonify(all_post)


@app.route('/api/v1/resources/post/create_post', methods=['POST'])
def creat_post():
    unix = time.time()
    date = str(datetime.datetime.fromtimestamp(unix).strftime('%Y-%m-%d %H:%M:%S'))

    data = request.get_json()
    database = "post.db"
    conn = sqlite3.connect(database)
    cur = conn.cursor()

    title = data['title']
    text = data['text']
    community = data['community']
    username = data['username']
    url = data['url']
    cur.execute('''INSERT INTO userpost (title,text,community,url,username,date)
                    VALUES(?,?,?,?,?,?)''', (title, text, community, url, username, date))
    conn.commit()
    cur.close()
    conn.close()
    return jsonify({'message': 'create ' + title + ' post success!'})


@app.route('/api/v1/resources/post/delete_post', methods=['POST'])
def delete_post():
    data = request.get_json()
    database = "post.db"
    try:
        conn = sqlite3.connect(database)
        cur = conn.cursor()
        postId = data['postId']
        cur.execute('''DELETE FROM userpost 
                        WHERE postId=?;''', (postId,))
        conn.commit()
        cur.close()
        conn.close()
        return jsonify({'message': 'delete successfully'})
    except Exception as e:
        return jsonify(str(e))


@app.route('/api/v1/resources/post/retrieve_post', methods=['POST'])
def retrieve_post():
    data = request.get_json()
    database = "post.db"
    try:
        conn = sqlite3.connect(database)
        cur = conn.cursor()
        postId = data['postId']
        post = cur.execute('''SELECT * FROM userpost 
                        WHERE postId=?;''', (postId,)).fetchall()
        conn.commit()
        cur.close()
        conn.close()
        return jsonify(post)
    except Exception as e:
        return jsonify(str(e))


app.run()
