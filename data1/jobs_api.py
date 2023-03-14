import flask
from flask import jsonify
from jobs import Jobs
import db_session

blueprint = flask.Blueprint('jobs_api', __name__, template_folder='templates')


@blueprint.route('/api/jobs')
def get_jobs():

    jobs = db_session.create_session().query(Jobs).all()
    return jsonify({'jobs': [i.to_dict() for i in jobs]})
