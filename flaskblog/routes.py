from flask import render_template, url_for,flash,redirect,request
from flaskblog import app,db,bcrypt
from flaskblog.forms import RegistrationForm, LoginForm
from flaskblog.models import User,Post
from flask_login import login_user,logout_user,current_user,login_required


posts = [

{
	'author': 'kkkk',
	'title':'first port',
	'content':'blh blah',
	'date':'may 15 2018'
},
{
	'author':'kkkk',
	'title':'first port',
	'content':'blh blah',
	'date':'may 15 2018'	
}

]

@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html',posts=posts)


@app.route('/about')
def about():
    return render_template('about.html',title='About Page')

@app.route('/register',methods=['GET','POST'])
def register():
	if current_user.is_authenticated:
		return redirect(url_for('home'))
	form = RegistrationForm()
	if form.validate_on_submit():
		hashed_pass = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
		user = User(username=form.username.data,email=form.email.data,password=hashed_pass)
		db.session.add(user)
		db.session.commit()
		flash('Account Successfully Created. You can Login ','success')
		return redirect(url_for('login'))
	return render_template('register.html',title='Register Page', form = form)


@app.route('/login',methods=['GET','POST'])
def login():
	if current_user.is_authenticated:
		return redirect(url_for('home'))
	form = LoginForm()
	if form.validate_on_submit():
		user = User.query.filter_by(email=form.email.data).first()
		if user and bcrypt.check_password_hash(user.password,form.password.data):
			login_user(user,remember=form.remember.data)
			next_page = request.args.get('next')
			return redirect(next_page) if next_page else redirect(url_for('home'))
		else:
			flash('Login Unsuccessful.','danger')
	return render_template('login.html',title='Login Page', form = form)


@app.route('/logout')
def logout():
	logout_user()
	return redirect(url_for('home'))


@app.route('/account')
@login_required
def account():
	logout_user()
	return render_template('account.html',title='Account')
