from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("pages/index.html")

@app.route('/<page>')
def page(page):
    return render_template("pages/"+page)

@app.errorhandler(404)
def page_not_found(error):
    return render_template("pages/404.html")

@app.errorhandler(500)
def error_500(error):
    return render_template("pages/404.html")

if __name__ == '__main__':
    app.run(debug=True)
