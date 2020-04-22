from flask import Flask, request, jsonify, Response
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
<p>User API</p>'''

@app.route('/api/v1/resources/users/all', methods=['GET'])
def api_all():
    conn = sqlite3.connect('redditDB.db')
    conn.row_factory = dict_factory
    cur = conn.cursor()
    all_users = cur.execute('SELECT * FROM user_tbl;').fetchall()

    return jsonify(all_users)
    

@app.route('/api/v1/resources/users/create', methods=['POST'])
def create_user():
    request_json = request.get_json()
    Email = request_json.get('email')
    User = request_json.get('username')
    Karma = request_json.get('karma')
    
    try:
        conn = sqlite3.connect('redditDB.db')
        cur = conn.cursor()
        cur.execute("INSERT INTO user_tbl VALUES(?,?,?)", (User, Email, Karma))
        conn.commit()
        cur.close()
        conn.close()
        return jsonify(message=User + ' was added successfully.'), 201 
    except:
        return jsonify(message='Username or mail already exists.'), 409



@app.route('/api/v1/resources/users/remove', methods=['DELETE'])
def delete_user():
    request_json = request.get_json()
    User = request_json.get('username')

    try:
        conn = sqlite3.connect('redditDB.db')
        cur = conn.cursor()
        cur.execute("DELETE FROM user_tbl WHERE username=?", (User,))
        conn.commit()
        cur.close()
        conn.close()
        return jsonify(message=User + ' was sucessfully deleted.'), 200
    except:
        return jsonify(message='Username does not exists'), 404


@app.route('/api/v1/resources/users/inc', methods=['PUT'])
def increment_karma():
    # get user name you want to delete
    request_json = request.get_json()
    User = request_json.get('username')

    try:
        # connect to the database
        conn = sqlite3.connect('redditDB.db')
        cur = conn.cursor()
        #inc karma
        cur.execute("UPDATE user_tbl SET Karma= Karma+1 WHERE username=?", (User,))
        conn.commit()
        cur.close()
        conn.close()
        return jsonify(message='Karma incremented'), 200
    except:
        return jsonify(message='Username does not exists'), 404


@app.route('/api/v1/resources/users/dec', methods=['PUT'])
def decrement_karma():
    # get user name you want to delete
    request_json = request.get_json()
    User = request_json.get('username')

    try:
        # connect to the database
        conn = sqlite3.connect('redditDB.db')
        cur = conn.cursor()
        #dec karma
        cur.execute("UPDATE user_tbl SET Karma= Karma-1 WHERE username=?", (User,))
        conn.commit()
        cur.close()
        conn.close()
        return jsonify(message='Karma decremented'), 200
    except:
        return jsonify(message='Username does not exists'), 404


@app.route('/api/v1/resources/users/email', methods=['PUT'])
def update_email():
    request_json = request.get_json()
    User = request_json.get('username')
    Email = request_json.get('email')

    try:
        conn = sqlite3.connect('redditDB.db')
        cur = conn.cursor()
        cur.execute("UPDATE user_tbl SET Email=? WHERE username=?", (Email, User))
        conn.commit()
        cur.close()
        conn.close()
        return jsonify(message='Email updated.'), 200
    except:
        return jsonify(message='Username does not exists'), 404
    

if __name__ == '__main__':
    app.run()
