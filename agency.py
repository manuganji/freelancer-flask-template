from flask import Flask
from flask import json
from flask import request
from jinja2 import Environment, PackageLoader
from forms import ContactForm
from flask_mail import Mail, Message

env = Environment(loader=PackageLoader('agency', 'templates'))
app = Flask(__name__)
app.config.from_object('settings')
mail = Mail(app)

team = [
    {
        'name': 'Manu Ganji',
        'position': 'Solution Architect / Web Developer',
        'description': 'Experienced developer',
        'twitter': 'http://twitter.com/manuganji',
        'linkedin': 'http://in.linkedin.com/in/manuganji',
        'image': 'manu.jpeg',
    },
]

portfolios = [
    {
        'title': 'Optmyzr',
        'description': 'We developed end to end solution for web',
        'image': 'cake.png',
        'client_name': 'Optmyzr Inc',
        'client_url': 'www.optmyzr.com',
        'date': '2014-2015',
        'service': 'Web Development',
    },
]

@app.route("/")
def index():
    template = env.get_template("index.html")
    return template.render(
        portfolios=portfolios,
        team = team
    )

@app.route("/contact/", methods=['POST'])
def contact():
    form = ContactForm(request.form)
    if form.validate():
        msg = Message(
            subject="Contact form msg",
            sender="manuganji@gmail.com",
            recipients=["manuganji@gmail.com"],
            reply_to=form.email.data,
            html=form.message.data
        )
        mail.send(msg)
        return "valid data"
    else:
        return json.dumps(form.errors), 400

if __name__ == "__main__":
    app.run()
