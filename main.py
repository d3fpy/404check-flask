from flask import Flask,render_template
from flask import request

app = Flask(__name__)


@app.route("/")
def main_page():
    return render_template ("index.html")


@app.route("/double")
def double():
    return render_template ("double.html")

@app.route('/teach')
def teach():
    return render_template ('teach.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404


@app.route('/login', methods=['GET','POST'])
def login():
    if request.method == 'POST':
        return "It's POST"
    else:
        return "It's GET"

@app.route('/post/<int:post_id>')
def post(post_id):
    return 'Post #' + str(post_id)
 

@app.route('/user/<string:name>/<int:id>')
def root(name,id):
    return "Hello: " + name + " - " + str(id) + "!"



if __name__ == "__main__":
    app.run(debug=True)