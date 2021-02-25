from flask_wtf import FlaskForm
from wtforms import StringField, FloatField, TextAreaField

class NewPost(FlaskForm):
    """New form for adding location"""

    title = StringField("Post Title")
    image = StringField("Image URL") 
    description = TextAreaField("Short Description")