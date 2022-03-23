from flask import Blueprint, render_template, request, flash, redirect, url_for
from .models import User,Booksread
from werkzeug.security import generate_password_hash, check_password_hash
from . import db
from flask_login import login_user, login_required, logout_user, current_user

auth = Blueprint('auth', __name__)


@auth.route('/login/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')

        user = User.query.filter_by(email=email).first()
        if user:
            if check_password_hash(user.password, password):
                flash('Logged in successfully!', category='success')
                login_user(user, remember=True)
                return redirect(url_for('views.home'))
            else:
                flash('Incorrect password, try again.', category='error')
        else:
            flash('Email does not exist.', category='error')

    return render_template("login.html", user=current_user)


@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('auth.login'))


@auth.route('/sign-up', methods=['GET', 'POST'])
def sign_up():
    if request.method == 'POST':
        email = request.form.get('email')
        first_name = request.form.get('firstName')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')

        user = User.query.filter_by(email=email).first()
        if user:
            flash('Email already exists.', category='error')
        elif len(email) < 4:
            flash('Email must be greater than 3 characters.', category='error')
        elif len(first_name) < 2:
            flash('First name must be greater than 1 character.', category='error')
        elif password1 != password2:
            flash('Passwords don\'t match.', category='error')
        elif len(password1) < 7:
            flash('Password must be at least 7 characters.', category='error')
        else:
            new_user = User(email=email, first_name=first_name, password=generate_password_hash(
                password1, method='sha256'))
            db.session.add(new_user)
            db.session.commit()
            login_user(new_user, remember=True)
            flash('Account created!', category='success')
            return redirect(url_for('views.home'))

    return render_template("sign_up.html", user=current_user)


@auth.route('/read', methods=['GET', 'POST'])
def read():
    if request.method == 'POST':
        book_title = request.form.get('book_title').lower()
        book_author = request.form.get('book_author').lower()
        rating = request.form.get('rating')

        existing_booktitle = Booksread.query.filter_by(book_title=book_title, user_id=current_user.id).first()
        if existing_booktitle:
            flash('Book is already added', category='error')
        elif len(book_title) < 1:
            flash('Enter book name', category='error')
        elif len(book_author) < 1:
            flash('Enter name of the author', category='error')
        else:
            new_readbook = Booksread(book_title=book_title, book_author=book_author,rating=rating,user_id=current_user.id)
            try:
                db.session.add(new_readbook)
                db.session.commit()
                flash(f'{book_title} Book Added!', category='success')
            except:
                flash('There was a problem with Adding Book', category='error')
    return render_template("read.html", user=current_user)


@auth.route('/update/<int:id>', methods=['GET', 'POST'])
def update(id):
    row_to_update = Booksread.query.get_or_404(id)
    if request.method == 'POST':
        row_to_update.book_title = request.form['book_title']
        row_to_update.book_author = request.form['book_author']
        row_to_update.rating = request.form['rating']
        try:
            db.session.commit()
            return redirect('/read')
        except:
            flash('There was a probelm with Update', category='error')
    else:
        return render_template("update.html", user=current_user,row_to_update=row_to_update)

@auth.route('/delete/<int:id>')
def delete(id):
    row_to_delete = Booksread.query.get_or_404(id)
    try:
        db.session.delete(row_to_delete)
        db.session.commit()
        return redirect('/read')
    except:
        flash('There was a probelm with Update', category='error')
