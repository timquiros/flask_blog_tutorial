from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, Email, EqualTo

class RegistrationForm(FlaskForm):

	#blank not valid and set max no. of characters
	username = StringField('Username', 
		validators=[DataRequired(), Length(min=2, max=20)])

	email = StringField(
			'Email',
			validators==[DataRequired(), Email()])

	password = PasswordField('Password', validators=[DataRequired()])
	
	#check if passwords are the same
	confirm_password = PasswordField('Confirm Password', 
		validators=[DataRequired(), EqualTo('password')])

	submit=  SubmitField('Sign Up')

class LoginForm(FlaskForm):

	email = StringField(
			'Email',
			validators==[DataRequired(), Email()])

	password = PasswordField('Password', validators=[DataRequired()])
	remember = BooleanField('Remember Me')
	submit=  SubmitField('Login')
