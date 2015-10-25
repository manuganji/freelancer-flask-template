import wtforms
from wtforms.validators import Email, Length, InputRequired

class ContactForm(wtforms.Form):
    name = wtforms.StringField('Name', validators = [InputRequired()])
    email = wtforms.StringField('Email', validators = [Email(), InputRequired()])
    phone = wtforms.StringField('Phone Number')
    message = wtforms.TextField('Message', validators=[InputRequired(), Length(min=20)])
