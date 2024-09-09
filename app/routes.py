from flask import render_template, request, redirect, url_for
from app import app

profs = []

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        name = request.form.get('name')
        age = request.form.get('age')
        hobby = request.form.get('hobby')
        city = request.form.get('city')
        if name and age and hobby and city:
            profs.append({'name': name, 'age': age, 'hobby': hobby, 'city': city})
            return redirect(url_for('index'))
    return render_template('profile.html', profs=profs)