import os
from flask import Flask, send_from_directory
from flask_mysqldb import MySQL

app = Flask(__name__, static_folder="img", static_url_path='')

static_file_dir = os.path.join(os.path.dirname(os.path.realpath(__file__)), '../img')

app_settings = os.getenv('APP_SETTINGS', 'src.server.config.DevelopmentConfig')

app.config.from_object(app_settings)

#Just for development on localhost
app.config['MYSQL_USER']='diego'
app.config['MYSQL_PASSWORD']='p@ssword'
app.config['MYSQL_DB']='wallapoop'
app.config['MYSQL_HOST']='localhost'

#Creating the database instance
db = MySQL(app)

@app.route('/img/<path:path>', methods=['GET'])
def send_img(path):
    print(os.path.join(static_file_dir, "teclado.jpg"))
    print(os.path.isfile(os.path.join(static_file_dir, "teclado.jpg")) )
    return send_from_directory(static_file_dir, "teclado.jpg")

from .views import views
app.register_blueprint(views.bp)