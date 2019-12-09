from flask import render_template, redirect, url_for, request
from flask_login import login_user, current_user, logout_user, login_required
from application import app, db, login_manager, bcrypt
from application.models import User, Anime, Anime_Watching
from application.forms import RegisterForm, LoginForm, AddWatching, UpdatePasswordForm

@app.route('/')

@app.route('/home')
@login_required
def home():
    return render_template('home.html', title='Home')

@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        hashed_pw = bcrypt.generate_password_hash(form.password.data)
        user = User(
                firstname=form.firstname.data, 
                lastname=form.lastname.data, 
                email=form.email.data, 
                password=hashed_pw)
        db.session.add(user)
        db.session.commit()
        return redirect(url_for('login'))
    return render_template('register.html', title='Register', form=form)

@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('home'))

    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user, remember=form.remember.data)
            next_page = request.args.get('next')
            if next_page:
                return redirect(next_page)
            else:
                return redirect(url_for('home'))

    return render_template('login.html', title='Login', form=form)


@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('login'))

@app.route('/profile', methods=['GET', 'POST'])
@login_required
def profile():
    form = UpdatePasswordForm()
    if form.validate_on_submit():
        #user = User.query.get(id)
        #user = User.query.filter_by(id = current_user.id).first()
        #if request.method == 'POST':
        if bcrypt.check_password_hash(current_user.password, form.old_password.data):
            hashed_pw = bcrypt.generate_password_hash(form.new_password.data)
                #user = User(
                    #firstname=current_user.firstname,
                    #lastname=current_user.lastname,
                    #email=current_user.email,
            password=hashed_pw
                    #)
            #db.session.delete(user.password)
            db.session.commit()
            return redirect(url_for('home'))
    else:
        return render_template('profile.html', title='Profile', form=form)

@app.route('/animelist')
@login_required
def animelist():
    animeData = Anime.query.all()
    return render_template('animelist.html', title='AnimeList', animes=animeData)

@app.route('/watchinglist')
@login_required
def addwatch():
    form = AddWatching()
    if request.method == 'POST':
        newwatch = Anime_Watching(
                user_id=current_user.id,
                anime_id=form.Anime.id,
                episode='1'
                )
        db.session.add(newwatch)
        db.session.commit()
        return redirect(url_for('animelist'))
    return render_template('watchlist')



