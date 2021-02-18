from flask_wtf import FlaskForm
from wtforms import StringField, FloatField

class NewPost(FlaskForm):
    """New form for adding location"""

    location = StringField("Location")
    picture = StringField("Image URL") 