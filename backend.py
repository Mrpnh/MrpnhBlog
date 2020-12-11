# imports
from flask import Flask,render_template

# Initialising things
app = Flask(__name__)


# endpoints

@app.route("/")
def home():
    return render_template('index.html')


@app.route("/about")
def about():
    return render_template('about.html')


@app.route("/contact")
def contact():
    return render_template('contact.html')

@app.route("/post")
def post():
    return render_template('post.html')



# app run
if __name__ == '__main__':
    app.run(port=5000,debug=True)
    