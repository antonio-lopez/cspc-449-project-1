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

@app.route('/api/v1/resources/post/listNthIntoCommunity', methods=['POST'])
def listNthIntoCommunity():
    data = request.get_json()
    database = "post.db"
    try:
        conn = sqlite3.connect(database)
        cur = conn.cursor()
        nth = data['nth']
        thisCom = data['community']
        post = cur.execute('''WITH myTableWithRows AS (
            SELECT (ROW_NUMBER() OVER (ORDER BY userpost.date DESC)) as row,*
            FROM userpost)
            SELECT * FROM myTableWithRows WHERE row <= ?''', (nth,)).fetchall()

        for i in range(nth):
            unix = time.time()
            date = str(datetime.datetime.fromtimestamp(unix).strftime('%Y-%m-%d %H:%M:%S'))
            thisTitle = post[i][2]
            thisText = post[i][3]
            thisUrl = post[i][5]
            thisUsername = post[i][6]
            cur.execute('''INSERT INTO userpost (title,text,community,url,username,date)
                                VALUES(?,?,?,?,?,?)''', (thisTitle, thisText, thisCom, thisUrl, thisUsername, date))

        conn.commit()
        cur.close()
        conn.close()
        return jsonify(post)
    except Exception as e:
        return jsonify(str(e))


app.run()
