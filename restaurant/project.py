from flask import Flask, render_template, request, redirect, url_for, flash
from restaurantdb import (save, delete, find_all, find_by,
                          find_menu_items_by_restaurant_id, 
                          find_first_restaurant, find_menu_item_by_id, 
                          saveMenuItem, deleteItem)
from database_setup import Base, Restaurant, MenuItem


app = Flask(__name__)


@app.route("/")
@app.route("/restaurants/<int:restaurant_id>/")
def restaurantsMenu(restaurant_id):
     restaurant = find_by(restaurant_id)
     output = ''
     items = find_menu_items_by_restaurant_id(restaurant.id)
     return render_template('menu.html', restaurant=restaurant, items=items)


@app.route("/restaurants/<int:restaurant_id>/new", methods=['GET', 'POST'])
def newMenuItem(restaurant_id):

    if request.method == 'POST':
        newItem = MenuItem(
            name=request.form['name'],
            description=request.form['description'],
            price=request.form['price'], restaurant_id=restaurant_id)
        saveMenuItem(newItem)
        flash("New item created.")
        return redirect(url_for('restaurantsMenu', restaurant_id=restaurant_id))
    else:
        return render_template('newMenuItem.html', restaurant_id=restaurant_id)


@app.route("/restaurants/<int:restaurant_id>/menuitem/<int:menuitem_id>/edit", methods=['GET', 'POST'])
def editMenuItem(restaurant_id, menuitem_id):

    item = find_menu_item_by_id(menuitem_id)
    if request.method == 'POST':
        if request.form['name']:
            item.name = request.form['name']
        if request.form['description']:
            item.description = request.form['description']
        if request.form['price']:
            item.price = request.form['price']
        saveMenuItem(item)
        flash("Menu Item has been edited")
        return redirect(url_for('restaurantsMenu', restaurant_id=restaurant_id))
    else:
        return render_template('editMenuItem.html', restaurant_id=restaurant_id, menuitem_id=menuitem_id, i=item)
    return


@app.route("/restaurants/<int:restaurant_id>/menuitem/<int:menuitem_id>/delete",  methods=['GET', 'POST'])
def deleteMenuItem(restaurant_id, menuitem_id):

    item = find_menu_item_by_id(menuitem_id)
    if request.method == 'POST':
        deleteItem(item)
        flash("Menu Item has been deleted")
        return redirect(url_for('restaurantsMenu', restaurant_id=restaurant_id))
    else:
        return render_template('deleteMenuItem.html', restaurant_id=restaurant_id, menuitem_id=menuitem_id, i=item)  

if __name__ == '__main__':
    app.secret_key = 'super_secret_key'
    app.debug = True
    app.run(host='0.0.0.0', port=5000)
