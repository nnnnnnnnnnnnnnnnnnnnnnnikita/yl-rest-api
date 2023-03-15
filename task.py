import datetime
from flask_login import LoginManager
from flask import Flask, make_response, jsonify
from data1 import jobs_api, api-user
import data1.db_session as session


app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'
app.config['PERMANENT_SESSION_LIFETIME'] = datetime.timedelta(days=365)
login_manager = LoginManager()
login_manager.init_app(app)


@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)


@app.errorhandler(400)
def bad_request(_):
    return make_response(jsonify({'error': 'Bad Request'}), 400)


if __name__ == '__main__':
    session.global_init("db/blogs.db")
    db_session = session.create_session()
    
    app.register_blueprint(jobs_api.blueprint)
    app.register_blueprint(api-user.blueprint)

    app.run(port=8080, host='127.0.0.1')
