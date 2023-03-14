import flask
from flask import jsonify, request
from jobs import Jobs
import db_session
from users import User

blueprint = flask.Blueprint('jobs_api', __name__, template_folder='templates')


@blueprint.route('/api/jobs')
def get_jobs():

    jobs = db_session.create_session().query(Jobs).all()
    return jsonify({'jobs': [i.to_dict() for i in jobs]})


@blueprint.route('/api/jobs/<int:job_id>', methods=['GET'])
def get_a_job(job_id):
    
    job = db_session.create_session().query(Jobs).get(job_id)
    if not job:
        return jsonify({'error': 'Not found'})
    else:
        return jsonify({'job': job.to_dict()})
    

@blueprint.route('/api/jobs', methods=['POST'])
def add_a_job():
    
    if not request.json:
        return jsonify({'error': 'Empty request'})
    elif not all(key in request.json for key in ['team_leader', 'title', 'work_size', 'collaborators', 'is_finished', 'start_date', 'end_date']):
        return jsonify({'error': 'Bad request'})
    session = db_session.create_session()
    if 'id' in request.json:
        if session.query(Jobs).filter(Jobs.id == request.json['id']).first():
            return jsonify({'error': ' Id already exists'})
    if not session.query(User).filter(User.id == request.json['team_leader']).first():
        return jsonify({'error': 'Bad request'})
    
    job = Jobs(job=request.json['title'],
                team_leader=request.json['team_leader'],
                work_size=request.json['work_size'],
                collaborators=request.json['collaborators'],
                start_date=request.json['start_date'],
                end_date=request.json['end_date'],
                is_finished=request.json['is_finished'])
    
    session.add(job)
    session.commit()
    return jsonify({'success': 'OK'})
