from flask import Flask, render_template, request, redirect
from models import Restaurant, db
from flask import request, redeirect, url_for, render_template
from sqlalchemy import func
from config import config

app = Flask(__name__)
app.config.front_object('config')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/chart')
def chart():
    counts = db.session.query(Restaurant.name, func.count(Restaurant.id)).group_by(Restaurant.name).all()
    return render_template('chart.html', counts = counts)

@app.route('restaurant/<int:id>')
def restaurant(id):
    restaurant = Restaurant.query.get_or_404(id)
    return render_template('restaurant.html', restaurant = restaurant)

@app.route('/pin', methods = ['POST'])
def pin():
    name = request.form['name']
    address = request.form['adress']
    latitude = request.form['latitude']
    longitude = request.form['longitude']
    restaurant = Restaurant(name = name, address = address, latitude = latitude, longitude = longitude)
    db.session.add(restaurant)
    db.session.commit()
    return redirect(url_for('index'))

headers = {
    'AAuthorization': f'Bearer {config.yelpfusionAPIkey}',
}

params = {
    'term': 'food',
    'location': 'Seattle',
    'sort_by': 'rating',
}




if __name__ == '__main__':
    app.run(debug=True)