from flask import Flask, request, render_template
from prsaw import RandomStuff


app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')



@app.route('/', methods=['POST'])
def post_message():
    message = request.form['message']
    rs = RandomStuff()
    response = rs.get_ai_response(message)
    return f"""<h1>You >> {message}<br> Spot >>> {response}<br></h1>"""

app.run(debug=True)
