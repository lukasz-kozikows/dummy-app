import socket
from flask import Flask, request, render_template
from db import get_conn

app = Flask(__name__)

def fetch_rows(limit: int):
    limit = max(1, min(limit, 500))
    sql = "SELECT id, created_at, quote FROM quotes ORDER BY created_at DESC LIMIT %s"
    cnx = get_conn()
    try:
        cur = cnx.cursor()
        cur.execute(sql, (limit,))
        return cur.fetchall()
    finally:
        cnx.close()

@app.route("/", methods=["GET"])
def index():
    hostname = socket.gethostname()
    limit = request.args.get("limit", "25")
    try:
        limit_int = int(limit)
    except ValueError:
        limit_int = 25
    rows = fetch_rows(limit_int)
    return render_template("index.html", hostname=hostname, limit=limit_int, rows=rows)