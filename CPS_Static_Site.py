from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/<page>')
def page(page):
    return render_template(page)

@app.errorhandler(404)
def page_not_found(error):
    return render_template("404.html")

@app.errorhandler(500)
def error_500(error):
    return render_template("404.html")

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
