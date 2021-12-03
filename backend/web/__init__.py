from flask import Flask

#configuration
app = Flask(__name__, static_url_path='/static')
app.config.from_object('config.Config')


from web import routes