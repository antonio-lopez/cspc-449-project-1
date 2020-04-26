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
<p>Vote API</p>'''


@app.route('/api/v1/resources/post/upvote', methods=['PUT'])
def upvote():
    request_json = request.get_json()
    postId = request_json.get('postId')

    try:
        conn = sqlite3.connect('redditDB.db')
        cur = conn.cursor()
        cur.execute('''UPDATE userpost_tbl SET upvotes = upvotes + 1  
                            WHERE postId = ?;''', (postId,))
        conn.commit()
        cur.close()
        conn.close()
        return jsonify(message= 'Upvote successfully'), 200
    except:
        return jsonify(message='Post does not exists'), 404

@app.route('/api/v1/resources/post/downvote', methods=['PUT'])
def downvote():
    request_json = request.get_json()
    postId = request_json.get('postId')

    try:
        conn = sqlite3.connect('redditDB.db')
        cur = conn.cursor()
        cur.execute('''UPDATE userpost_tbl SET downvotes = downvotes - 1  
                            WHERE postId = ?;''', (postId,))
        conn.commit()
        cur.close()
        conn.close()
        return jsonify(message= 'Downvote successfully'), 200
    except:
        return jsonify(message='Post does not exists'), 404


@app.route('/api/v1/resources/post/retrieve_vote', methods=['GET'])
def retrieve_vote():
    request_json = request.get_json()
    postId = request_json.get('postId')

    try:
        conn = sqlite3.connect('redditDB.db')
        cur = conn.cursor()
        post = cur.execute('''SELECT upvotes, downvotes FROM userpost_tbl
                            WHERE postId = ?;''', (postId,)).fetchall()
        vote = {
            "upvotes" : post[0][0],
            "downvotes" : post[0][1],
            "postId" : postId
        }
        conn.commit()
        cur.close()
        conn.close()
        return jsonify(vote), 200
    except:
        return jsonify(message='Post does not exists'), 404


@app.route('/api/v1/resources/post/topNthScore', methods=['GET'])
def topNthScore():
    data = request.get_json()
    database = "redditDB.db"
    try:
        conn = sqlite3.connect(database)
        cur = conn.cursor()
        nth = data['nth']
        post = cur.execute('''SELECT * FROM userpost_tbl
                                ORDER by (upvotes - downvotes) DESC
                                LIMIT ?;''', (nth,)).fetchall()

        myList = []
        for i in range(nth):
            thisPostId = post[i][0]
            thisTitle = post[i][1]
            thisUsername = post[i][4]
            thisDate = post[i][6]
            thisUpvotes = post[i][7]
            thisDownvotes = post[i][8]
            iPost = {
                "postId":thisPostId,
                "title":thisTitle ,
                "community":thisUsername ,
                "username": thisUsername,
                "date":thisDate,
                "upvotes" : thisUpvotes,
                "downvotes" : thisDownvotes
            }
            myList.append(iPost)
        conn.commit()
        cur.close()
        conn.close()
        return jsonify(myList), 200
    except:
        return jsonify(message='Post does not exists'), 404


@app.route('/api/v1/resources/post/sortedByScore', methods=['GET'])
def sortedByScore():
    data = request.get_json()
    database = "redditDB.db"
    try:
        conn = sqlite3.connect(database)
        cur = conn.cursor()
        posts = data['list']
        post = posts.split(",")
        print(len(post))

        dict = {}
        myList = ""
        for i in range (len(post)):
            postId = post[i]
            score = cur.execute('''SELECT (upvotes - downvotes) FROM userpost_tbl WHERE postId = ?''', (postId,)).fetchall()
            dict[postId] = score[0][0]
        print(sorted(dict.items(), key = lambda kv: (kv[1], kv[0]), reverse = True))
        for i in (sorted(dict.items(), key = lambda kv: (kv[1], kv[0]), reverse = True)):
            myList = myList + i[0] + ","
        if (len(myList) != 0):
            myList = myList[:-1]
        conn.commit()
        cur.close()
        conn.close()
        return jsonify({"sorted list" : myList}), 200
    except:
        return jsonify(message='Post does not exists'), 404


if __name__ == '__main__':
    app.run()