import sqlite3
from flask import Flask, render_template, request

app = Flask(__name__)

def get_db_connection():
    conn = sqlite3.connect('./Database/database.db')
    conn.row_factory = sqlite3.Row
    return conn
@app.route('/get_post')
def get_account():
    '''
    Get the post with a specific title.
    Get the title from the request's parameters.
    Return the post's content.
    '''
    title = request.args.get('title')
    conn = get_db_connection()
    cursor = conn.cursor()
    query = 'SELECT * FROM posts WHERE title=?;'
    results = cursor.execute(query, (title, ))
    for row in results:
        print(row['content'])
        return row['content']

if __name__ == '__main__':
    app.run(debug=True)
\end{code}

Answer: You can use `request.args` to get the value of `