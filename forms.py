import wtforms
from wtforms.validators import Email, Length, InputRequired

class ContactForm(wtforms.Form):
    name = wtforms.StringField('Name', validators = [InputRequired()])
    email = wtforms.StringField('Email', validators = [Email(), InputRequired()])
    phone = wtforms.StringField('Phone Number')
    message = wtforms.TextField('Message', validators=[InputRequired(), Length(min=20)])

class ServiceForm(wtforms.Form):
    # adds some more fields to Contact form
    name = wtforms.StringField('Name', validators = [InputRequired()])
    email = wtforms.StringField('Email', validators = [Email(), InputRequired()])
    phone = wtforms.StringField('Phone Number')
    service = wtforms.StringField('Service')
    location = wtforms.StringField('Location')
    overview = wtforms.TextField('Project Overview', validators=[InputRequired()])
    status = wtforms.TextField('Project Status')
    expectations = wtforms.TextField('Your Expectations', validators=[InputRequired()])
    priority = wtforms.StringField('Your top priority', validators=[InputRequired()])
    budget = wtforms.StringField('Budget', validators=[InputRequired()])
    timeline = wtforms.StringField('Timeline', validators=[InputRequired()])
