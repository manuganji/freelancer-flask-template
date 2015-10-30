from flask import Flask
from flask import json
from flask import render_template
from flask import request
from jinja2 import Environment, PackageLoader
from forms import ContactForm, ServiceForm
from flask_mail import Mail, Message

env = Environment(loader=PackageLoader('agency', 'templates'))
app = Flask(__name__)
app.config.from_object('settings')
mail = Mail(app)

team = [
    {
        'name': 'Mallikarjuna Reddy',
        'position': 'iOS Developer',
        'description': '5 years of experience in iOS development',
        'facebook': 'https://www.facebook.com/punuruMalli?fref=ts',
        'linkedin': 'https://www.linkedin.com/pub/mallikarjuna-reddy-punuru/21/992/258',
        'image': 'malli.jpg',
    },
    {
        'name': 'Manu Ganji',
        'position': 'Solution Architect',
        'description': 'Generalist web programmer with 4 years of experience building industry leading technology',
        'twitter': 'http://twitter.com/manuganji',
        'linkedin': 'http://in.linkedin.com/in/manuganji',
        'image': 'manu.jpeg',
    },
    {
        'name': 'Rama Srinivas',
        'position': 'Android Developer',
        'description': 'Early employee at 3 Android startups',
        'facebook': 'https://www.facebook.com/ramasrinivas.15990',
        'linkedin': 'https://in.linkedin.com/pub/rama-srinivas/40/668/2b',
        'image': 'srinivas.jpg',
    }
]

portfolio = [
    {
        'title': 'Dres.sy',
        'description': 'Dres.sy is a virtual Fitting Room for your store. Manu lead the development of Dres.sy beta for Imaginate software. It has many cutting edge features like Computer Vision, Async Task execution, Color clustering and some elements of Augmented Reality',
        'image': 'dressy.png',
        'client_name': 'Dres.sy',
        'client_url': 'http://www.dres.sy',
        'date': '2013',
        'service': 'Web Development',
    },
    {
        'title': 'Optmyzr',
        'description': 'Optmyzr is a collection of Google AdWords Tools for Advertisers, Consultants, and Agencies. Manu worked as Senior Software Engineer for Optmyzr where he was responsible for maintenance and new feature development in One Click Optimizations and Data Insights',
        'image': 'optmyzr_home.png',
        'client_name': 'Optmyzr Inc',
        'client_url': 'http://www.optmyzr.com',
        'date': '2014-2015',
        'service': 'Web Development',
    },
    {
        'title': 'OMitra',
        'description': """Rama was the sole developer on OMitra Android App. India's first app for alleviating problems encountered in train travel. Advanced live train tracking,
        Wakup alarm, Train noticeboard, Important Railway contacts, Family trip tracking""",
        'image': 'omitra.png',
        'client_name': 'OMitra on Google Play',
        'client_url': 'https://play.google.com/store/apps/details?id=com.train.omitraapp',
        'date': '2014-2015',
        'service': 'Android Development',
    },
    {
        'title': 'RISSTA',
        'description': """RISSTA – Railway Interactive Security Solution for Traveller’s Assistance.
        This App is developed in collaboration with Secunderabad and Hyderabad RPF.""",
        'image': 'rissta.png',
        'client_name': 'RISSTA on Google Play',
        'client_url': 'https://play.google.com/store/apps/details?id=com.omitrasaftyapp',
        'date': '2015',
        'service': 'Android Development',
    }
]

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
