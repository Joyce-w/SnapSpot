from flask_wtf import FlaskForm
from wtforms import StringField, FloatField, TextAreaField, PasswordField
from wtforms.validators import DataRequired, Length, InputRequired


class UserSignup(FlaskForm):
    """Form for user signup"""
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired(), Length(min=8)])
    display_name = StringField('Display Name', validators=[DataRequired()])
    area = StringField('Area of Interest (zipcode, location, etc)', validators=[DataRequired()])
    caption = TextAreaField("Short caption", validators=[DataRequired()])


class UserLogin(FlaskForm):
    """Existing user login form"""
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])

class NewPost(FlaskForm):
    """New form for adding location"""
    title = StringField("Post Title", validators=[DataRequired()])
    image = StringField("Image URL") 
    description = TextAreaField("Short Description", validators=[DataRequired()])
