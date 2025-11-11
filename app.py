import sqlite3
from flask import Flask, g, request, render_template_string

DB = 'users.db'
app = Flask(__name__)

def get_db():
    if 'db' not in g:
        # use row_factory if you want nicer rows (optional)
        g.db = sqlite3.connect(DB)
        g.db.row_factory = sqlite3.Row
    return g.db

@app.teardown_appcontext
def close_db(e=None):
    db = g.pop('db', None)
    if db:
        db.close()

@app.route('/')
def index():
    return "MiniSQL Lab: visit /user?user_id=<id>"

# Safer endpoint using parameterized query + input validation
@app.route('/user')
def user():
    user_id = request.args.get('user_id', '')
    # Validate: make sure it's an integer
    try:
        user_id_int = int(user_id)
    except ValueError:
        return "Invalid user_id. Use a number like ?user_id=1", 400

    db = get_db()
    try:
        # Parameterized query prevents SQL injection
        cur = db.execute("SELECT id, username FROM users WHERE id = ?", (user_id_int,))
        rows = cur.fetchall()
        out = "<br>".join([f"{r['id']} - {r['username']}" for r in rows]) or "No results"
    except Exception as e:
        # Don't show exception text to the user in production.
        # Here we return a friendly message. In real apps, log the full exception.
        out = "An internal error occurred."

    # For learning you can show the query, but don't do this in production.
    template = "<h3>Results</h3>{{out}}"
    return render_template_string(template, out=out)

if __name__ == '__main__':
    # For development use Flask's default port 5000 (no root needed)
    app.run(host='0.0.0.0', port=5000)

