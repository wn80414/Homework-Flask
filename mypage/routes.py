from mypage import mypage_obj
from mypage.forms import TopCities
from flask import render_template, flash, request
from mypage import db
from mypage.models import City

@mypage_obj.route("/", methods=['GET', 'POST'])
def home():
    form = TopCities()
    if form.validate_on_submit():
        cityParam = form.city_name.data
        rankParam = form.city_rank.data
        visitParam = form.is_visited.data
        city = City(city_name = cityParam, city_rank = rankParam, is_visited = visistParam)
        db.session.add(city)
        db.session.commit()
        flash(f'{cityParam} Added To List.')
    city_list = City.query.all()
    name = 'William'
    title = 'Top Cities'
    return render_template('home.html', name = name, title = title, form = form, city_list = city_list)
