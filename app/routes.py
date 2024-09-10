from flask import render_template, request, redirect, url_for, flash
from app import app, db
from app.models import Subscription


@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template("index.html")

@app.route('/subscribe', methods=['POST'])
def subscribe():
    email = request.form['email']
    # if Subscription.query.filter_by(email=email).first():
    #     flash('Email already exists', 'error')
    #     return redirect(url_for('index'))

    new_subscription = Subscription(email=email)
    db.session.add(new_subscription)
    db.session.commit()
    flash('Thank you for subscribing!', 'success')
    return redirect(url_for('index'))