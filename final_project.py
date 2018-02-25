from flask import Flask

app = Flask(__name__)


@app.route('/')
@app.route('/restaurants')
def show_restaurants():
    return 'This page will show all my restaurants'


if __name__ == '__main__':
    app.secret_key = 'Secret-key'
    app.debug = True
    app.run(host='0.0.0.0', port=5000)
