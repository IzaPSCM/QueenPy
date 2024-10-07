from flask import Flask

app = Flask(__name__)


@app.route('/')
def home():
    return "Olá, Mundo!"

@app.route('/new',methoods=['GET','POST'])
def new():
    return 'Cadastre algo'

@app.route('/<short>')
def short():
    return "Olá, mundo!"

@app.errorhandler(404)
def page_not_found(e):
    return 'erro 404', 404

if __name__ == '__main__':
    app.run(debug=True)
