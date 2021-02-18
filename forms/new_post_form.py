from flask_wtf import FlaskForm
from wtforms import StringField, FloatField

class NewPost(FlaskForm):
    """New form for adding location"""

    location = StringField("Location")
    Image = StringField("Image URL") 
    Description = StringField("Short Description")