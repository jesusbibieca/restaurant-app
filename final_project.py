from flask import Flask

app = Flask(__name__)

# Fake Restaurants
restaurant = {'name': 'The CRUDdy Crab', 'id': '1'}

restaurants = [{'name': 'The CRUDdy Crab', 'id': '1'}, {'name': 'Blue Burgers', 'id': '2'},
               {'name': 'Taco Hut', 'id': '3'}]

# Fake Menu Items
items = [{'name': 'Cheese Pizza', 'description': 'made with fresh cheese', 'price': '$5.99', 'course': 'Entree',
         'id': '1'}, {'name': 'Chocolate Cake', 'description': 'made with Dutch Chocolate', 'price': '$3.99',
         'course': 'Dessert', 'id': '2'}, {'name': 'Caesar Salad', 'description': 'with fresh organic vegetables',
         'price': '$5.99', 'course': 'Entree', 'id': '3'}, {'name': 'Iced Tea', 'description': 'with lemon',
         'price': '$.99', 'course': 'Beverage', 'id': '4'}, {'name': 'Spinach Dip', 'description':
         'creamy dip with fresh spinach', 'price': '$1.99', 'course': 'Appetizer', 'id': '5'}]

item = {'name': 'Cheese Pizza', 'description': 'made with fresh cheese', 'price': '$5.99', 'course': 'Entree'}


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


@app.route('/restaurant/<int:restaurant_id>/menu/<int:menu_id>/edit')
def edit_menu_item(restaurant_id, menu_id):
    return 'This page is for editting the menu item number %s' % menu_id


@app.route('/restaurant/<int:restaurant_id>/menu/<int:menu_id>/delete')
def delete_menu_item(restaurant_id, menu_id):
    return 'This page is for deleting the menu item number %s' % menu_id


if __name__ == '__main__':
    app.secret_key = 'Secret-key'
    app.debug = True
    app.run(host='0.0.0.0', port=5000)
