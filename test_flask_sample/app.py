from flask import Flask, escape, request, render_template
from datetime import datetime
app = Flask(__name__)


@app.route('/')
def hello():
    utc_time=datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S')
    return render_template("index.html",utc_time=utc_time)

# type python hello.py to run directly the server without creating an environment variable
if __name__=='__main__':
    app.run(debug=True)