from flask import Flask

app = Flask(__name__)


@app.route('/')
@app.route('/restaurants')
def show_restaurants():
    return 'This page will show all my restaurants'


@app.route('/restaurant/new')
def new_restaurants():
    return 'This page will be for making a new restaurant'


@app.route('/restaurant/<int:restaurant_id>/edit')
def edit_restaurants(restaurant_id):
    return 'This page will be for editting restaurant number %s' % restaurant_id


@app.route('/restaurant/<int:restaurant_id>/delete')
def delete_restaurants(restaurant_id):
    return 'This page will be for deleting restaurant number %s' % restaurant_id


@app.route('/restaurant/<int:restaurant_id>')
@app.route('/restaurant/<int:restaurant_id>/menu')
def show_menu(restaurant_id):
    return 'This page is the menu for restaurant number %s' % restaurant_id


@app.route('/restaurant/<int:restaurant_id>/menu/new')
def new_menu_item(restaurant_id):
    return 'This page is for making a new menu item for restaurant number %s' % restaurant_id


if __name__ == '__main__':
    app.secret_key = 'Secret-key'
    app.debug = True
    app.run(host='0.0.0.0', port=5000)
