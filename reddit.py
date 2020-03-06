from flask import Flask, request, jsonify
import sqlite3

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

@app.route('/api/v1/resources/users', methods=['POST'])
def create_user():
    request_json = request.get_json()
    Email = request_json.get('Email')
    User = request_json.get('User')
    Karma = request_json.get('Karma')
    response_content = None
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

    cur.execute("INSERT INTO useraccount VALUES(?,?,?)", (Karma,User,Email))
    conn.commit()
    return jsonify(response_content)


app.run()