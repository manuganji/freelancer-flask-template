from flask import Flask
from jinja2 import Environment, PackageLoader

env = Environment(loader=PackageLoader('agency', 'templates'))
app = Flask(__name__)

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
    return template.render(portfolios=portfolios)

if __name__ == "__main__":
    app.run(debug=True)
