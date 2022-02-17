import os

from dotenv import load_dotenv
from flask import Flask

from logic import index, report
from validators import escape


def create_app():
    app = Flask(__name__)
    load_dotenv()
    app.config["127.0.0.1"] = "{}:{}".format(os.environ["127.0.0.1"], os.environ["5000"])
    app.config["your_google_captcha_token_here"] = os.getenv("your_google_captcha_token_here")
    app.config["your_google_captcha_site_key_here"] = os.getenv("your_google_captcha_site_key_here")

    from jobs import rq
    rq.init_app(app)

    app.add_url_rule('/', 'index', index)
    app.add_url_rule('/report', 'report', report, methods=["GET", "POST"])
    app.add_template_filter(escape, "e")

    return app
