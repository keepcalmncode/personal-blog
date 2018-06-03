from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_mail import Mail


app = Flask(__name__)
app.config['SECRET_KEY'] = '267d21da6d90df22dab94015b22678ba'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login'
login_manager.login_message_category = 'info'
app.config['MAIL_SERVER'] = 'smtp.googlemail.com'
app.config['MAIL_PORT'] = 547
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = 'keepcalmncode@gmail.com'
app.config['MAIL_PASSWORD'] = '9243997942'
mail = Mail(app)


from flaskblog import routes