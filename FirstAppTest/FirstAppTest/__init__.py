from flask import Flask
from FirstAppTest.api.routes import mod as site_mod
from FirstAppTest.site.routes import mod as api_mod

app = Flask(__name__)

app.register_blueprint(site_mod)
app.register_blueprint(api_mod, url_prefix="/api")