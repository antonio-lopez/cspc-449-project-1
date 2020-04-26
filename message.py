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
<p>Message API</p>'''

@app.route('/api/v1/resources/message', methods=['POST'])
def send_message():
        unix = time.time()
        Date = str(datetime.datetime.fromtimestamp(unix).strftime('%Y-%m-%d %H:%M:%S'))
        request_json = request.get_json()
        UserTo = request_json.get('userto')
        UserFrom = request_json.get('userfrom')
        MessageContents = request_json.get('messagecontents')
        MessageFlag = request_json.get('messageflag')

        try:
            conn = sqlite3.connect('redditDB.db')
            cur = conn.cursor()
            cur.execute("INSERT INTO message_tbl (userto,userfrom,messagecontents,messageflag,date) VALUES(?,?,?,?,?)", (UserTo, UserFrom, MessageContents, MessageFlag, Date))
            conn.commit()
            cur.close()
            conn.close()
            return jsonify(message='Message Sent.'), 201
        except:
            return jsonify(message='Message already exists.'), 409

@app.route('/api/v1/resources/message/delete', methods=['DELETE'])
def delete_message():
    request_json = request.get_json()
    MessageID = request_json.get('messageid')

    try:
        conn = sqlite3.connect('redditDB.db')
        cur = conn.cursor()
        cur.execute("DELETE FROM message_tbl WHERE messageid=?", (MessageID,))
        conn.commit()
        cur.close()
        conn.close()
        return jsonify(message='Message Deleted.'), 200
    except:
        return jsonify(message='Message does not exists'), 404

@app.route('/api/v1/resources/message/favorite', methods=['GET'])
def favorite_message():
    request_json = request.get_json()
    MessageFlag = request_json.get('messageflag')

    try:
        conn = sqlite3.connect('redditDB.db')
        cur = conn.cursor()
        Message = cur.execute("SELECT * FROM message_tbl WHERE messageflag=?", (MessageFlag,)).fetchall()
        conn.commit()
        cur.close()
        conn.close()
        return jsonify(Message), 200
    except:
        return jsonify(message='Message does not exists'), 404

if __name__ == '__main__':
    app.run()