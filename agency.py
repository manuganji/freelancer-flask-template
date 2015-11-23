from flask import Flask
from flask import json
from flask import render_template
from flask import request
from jinja2 import Environment, PackageLoader
from forms import ContactForm, ServiceForm
from flask_mail import Mail, Message
from portfolio import items as portfolio
from team import members as team

env = Environment(loader=PackageLoader('agency', 'templates'))
app = Flask(__name__)
app.config.from_object('settings')
mail = Mail(app)

@app.route("/")
def index():
    return render_template("index.html",
        portfolio=portfolio,
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
        # mail.send(msg)
        return "valid data"
    else:
        return json.dumps(form.errors), 400

@app.route("/service-contact/", methods=['POST'])
def service_contact():
    form = ServiceForm(request.form)
    if form.validate():
        msg = Message(
            subject="Service contact form msg from "+form.name.data,
            sender="manuganji@gmail.com",
            recipients=["manuganji@gmail.com"],
            reply_to=form.email.data,
            html=render_template('service_email.html', **form.data)
        )
        mail.send(msg)
        return "valid data"
    else:
        return json.dumps(form.errors), 400


@app.route("/android-services/", methods=['GET'])
def android():
    return render_template("android.html", portfolio=portfolio, service_name="android")

@app.route("/ios-services/", methods=['GET'])
def ios():
    return render_template("ios.html", portfolio=portfolio, service_name="ios")

@app.route("/web-development-services/", methods=['GET'])
def web():
    return render_template("web.html", portfolio=portfolio, service_name="web")

if __name__ == "__main__":
    app.run()
