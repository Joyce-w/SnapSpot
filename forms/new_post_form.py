from flask_wtf import FlaskForm
from wtforms import StringField, FloatField

class NewPost(FlaskForm):
    """New form for adding location"""

    title = StringField("Post Title")
    location = StringField("Location")
    image = StringField("Image URL") 
    description = StringField("Short Description")