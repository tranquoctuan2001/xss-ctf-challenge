import os

from dotenv import load_dotenv
from flask import Flask

from logic import index, report
from validators import escape


def create_app():
    app = Flask(__name__)
    load_dotenv()
    # app.config["IP_OR_DOMAIN_WITH_PORT"] = "{}:{}".format(
    #     os.environ["IP_OR_DOMAIN"], os.environ["PORT"])
    # app.config["CAPTCHA_TOKEN"] = os.getenv("CAPTCHA_TOKEN")
    # app.config["CAPTCHA_SITE_KEY"] = os.getenv("CAPTCHA_SITE_KEY")

    # app.config["127.0.0.1"] = "{}:{}".format(
    #     os.environ["127.0.0.1"], os.environ[""])
    # app.config["your_google_captcha_token_here"] = os.getenv(
    #     "your_google_captcha_token_here")
    # app.config["CAPTCHA_SITE_KEY"] = os.getenv("CAPTCHA_SITE_KEY")
    # port = int(os.environ.get("PORT", 33507))
    # app.run(debug=True, threaded=True, host="127.0.0.1", port=4000)
    from jobs import rq
    rq.init_app(app)

    app.add_url_rule('/', 'index', index)
    app.add_url_rule('/report', 'report', report, methods=["GET", "POST"])
    app.add_template_filter(escape, "e")

    return app
