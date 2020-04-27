from flask import Flask, request, jsonify
import redis

app = Flask(__name__)

conn = redis.StrictRedis(
    host='redis',
    port=6379 )
key = "autocompl"

def complete(conn, key, prefix, count):
    results = []
    rangelen = 50
    start = conn.zrank(key, prefix)

    if start == None:
        return jsonify(results)

    range = conn.zrange(key,start,start+rangelen-1)

    for n in range:
        entry = n.decode("utf-8")
        minlen = min([len(entry), len(prefix)])
        if entry[0:minlen] != prefix[0:minlen]:
            break
        if entry[-1] == "*" and len(results) != count:
            results.append(entry[:-1])

    return jsonify(results)

@app.route('/add_word')
def add_word():
    word = request.args.get('word')
    if word:
        for value in range(len(word)):
            conn.zadd(key, {word[:value+1]: 0})
        out = word + "*"
        conn.zadd(key, {out: 0})
        return "Word added successfully"
    return "No word given in the parameters"

@app.route('/autocomplete')
def autocomplete():
    word = request.args.get('query')
    return complete(conn, key, word, 50)

if __name__ == '__main__':
    app.run(host="0.0.0.0", debug=True)


