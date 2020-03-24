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
    
    if not Email:
        page_not_found(404)
    elif not User:
        page_not_found(404)
    else:
        conn = sqlite3.connect('redditDB.db')
        cur = conn.cursor()
        # exist = cur.execute("Select Exists(SELECT Email FROM user WHERE Email=?", (Email))
        # if exist != 1:
        response_content = cur.execute("INSERT INTO user_tbl VALUES(?,?,?)", (User, Email, Karma))
        conn.commit()
            #return jsonify(response_content)
        return Response(response_content,status=201,mimetype='application/json')
        # else:
        #     page_not_found(404)


@app.route('/api/v1/resources/users/remove', methods=['DELETE'])
def delete_user():
    # get user name you want to delete
    request_json = request.get_json()
    User = request_json.get('username')

    # connect to the database
    conn = sqlite3.connect('redditDB.db')
    cur = conn.cursor()
    # response = cur.execute("SELECT * FROM user_tbl WHERE username=?", (User,))
    # if response != 0:

    #     response_content = "User Does Not Exist"
    #     return Response(response_content,status=404,mimetype='application/json')
    # else:
    # execute command to delete user
    response_content = cur.execute("DELETE FROM user_tbl WHERE username=?", (User,))
    conn.commit()
    return Response(response_content,status=200,mimetype='application/json')


@app.route('/api/v1/resources/users/inc', methods=['PUT'])
def increment_karma():
    # get user name you want to delete
    request_json = request.get_json()
    User = request_json.get('username')

    # connect to the database
    conn = sqlite3.connect('redditDB.db')
    cur = conn.cursor()
    #inc karma
    response_content = cur.execute("UPDATE user_tbl SET Karma= Karma+1 WHERE username=?", (User,))
    conn.commit()
    return Response(response_content,status=200,mimetype='application/json')


@app.route('/api/v1/resources/users/dec', methods=['PUT'])
def decrement_karma():
    # get user name you want to delete
    request_json = request.get_json()
    User = request_json.get('username')

    # connect to the database
    conn = sqlite3.connect('redditDB.db')
    cur = conn.cursor()
    #dec karma
    response_content = cur.execute("UPDATE user_tbl SET Karma= Karma-1 WHERE username=?", (User,))
    conn.commit()
    return Response(response_content,status=200,mimetype='application/json')


@app.route('/api/v1/resources/users/email', methods=['PUT'])
def update_email():
    request_json = request.get_json()
    User = request_json.get('username')
    Email = request_json.get('email')

    conn = sqlite3.connect('redditDB.db')
    cur = conn.cursor()
    response_content = cur.execute("UPDATE user_tbl SET Email=? WHERE username=?", (Email, User))
    conn.commit()
    return Response(response_content,status=200,mimetype='application/json')
    

if __name__ == '__main__':
    app.run()