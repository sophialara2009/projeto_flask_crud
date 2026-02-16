# app.py

from flask import Flask
from config import Config

from pages.home import home_bp
from pages.about import info_bp

app = Flask(__name__)
app.config.from_object(Config)


@app.context_processor
def inject_globals():
    return {
        "app_title": app.config["APP_TITLE"],
        "app_name": app.config["APP_NAME"],
    }


app.register_blueprint(home_bp)
app.register_blueprint(info_bp)


if __name__ == "__main__":
    app.run(debug=True)
