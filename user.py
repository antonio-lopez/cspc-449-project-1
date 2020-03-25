from flask import Flask, request, jsonify, Response
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
<p>User API</p>'''

@app.route('/api/v1/resources/users/all', methods=['GET'])
def api_all():
    conn = sqlite3.connect('redditDB.db')
    conn.row_factory = dict_factory
    cur = conn.cursor()
    all_users = cur.execute('SELECT * FROM user_tbl;').fetchall()

    return jsonify(all_users)

@app.errorhandler(404)
def page_not_found(e):
    return "<h1>404</h1><p>The resource could not be found.</p>", 404

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
        return jsonify(message='User added successfully.'), 201 
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
        return jsonify(message='User successfully deleted.'), 200
    except:
        return jsonify(message='User does not exist.'), 404  


@app.route('/api/v1/resources/users/inc', methods=['PUT'])
def increment_karma():
    request_json = request.get_json()
    User = request_json.get('username')
    try:
        conn = sqlite3.connect('redditDB.db')
        cur = conn.cursor()
        cur.execute("UPDATE user_tbl SET Karma= Karma+1 WHERE username=?", (User,))
        conn.commit()
        return jsonify(message='User karma successfully incremented.'), 200
    except:
        return jsonify(message='User does not exist.'), 404  



@app.route('/api/v1/resources/users/dec', methods=['PUT'])
def decrement_karma():
    request_json = request.get_json()
    User = request_json.get('username')

    try:
        conn = sqlite3.connect('redditDB.db')
        cur = conn.cursor()
        cur.execute("UPDATE user_tbl SET Karma= Karma-1 WHERE username=?", (User,))
        conn.commit()
        return jsonify(message='User karma successfully decremented.'), 200
    except:
        return jsonify(message='User does not exist.'), 404 



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
        return jsonify(message='User email successfully updated.'), 200
    except:
        return jsonify(message='User does not exist.'), 404 

    

if __name__ == '__main__':
    app.run()