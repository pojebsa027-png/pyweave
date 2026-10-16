from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, Length


class TaskForm(FlaskForm):
    title = StringField("Title", validators=[DataRequired(), Length(max=120)])
    submit = SubmitField("Save")
