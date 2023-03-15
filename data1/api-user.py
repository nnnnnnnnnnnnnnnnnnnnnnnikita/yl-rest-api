import flask
from flask import jsonify, request
from users import User
import db_session

blueprint = flask.Blueprint('users_api', __name__, template_folder='templates')


@blueprint.route('/api/users')
def get_all_users():

    users = db_session.create_session().query(User).all()
    return jsonify({'users': [i.to_dict() for i in users]})


@blueprint.route('/api/users/<int:user_id>', methods=['GET'])
def get_a_user(id_user):

    users = db_session.create_session().query(User).get(id_user)
    if not users:
        return jsonify({'error': 'Not found'})
    else:
        return jsonify({'user': users.to_dict()})


@blueprint.route('/api/users', methods=['POST'])
def add_a_user():

    if not request.json:
        return jsonify({'error': 'Empty request'})
    elif not all(i in request.json for i in ['address', 'age', 'email', 'modified_date', 'name', 'position', 'surname', 'speciality', 'password_hash']):
        return jsonify({'error': 'Bad request'})

    session = db_session.create_session()
    if 'id' in request.json:
        if session.query(User).filter(User.id == request.json['id']).first():
            return jsonify({'error': ' Id already exists'})

    new_user = User(address=request.json['address'],
                age=request.json['age'],
                email=request.json['email'],
                modified_date=request.json['modified_date'],
                name=request.json['name'],
                position=request.json['position'],
                surname=request.json['surname'],
                speciality=request.json['speciality'],
                password_hash=request.json['password_hash'])

    session.add(new_user)
    session.commit()
    return jsonify({'success': 'OK'})


@blueprint.route('/api/users/<int:user_id>', methods=['DELETE'])
def del_a_user(id_user):

    session = db_session.create_session()
    user = session.query(User).get(id_user)
    if not user:
        return jsonify({'error': 'Not found'})
    else:
        session.delete(user)
        session.commit()
        return jsonify({'success': 'OK'})


@blueprint.route('/api/users/<int:user_id>', methods=['PUT'])
def edit_a_user(id_user):

    if not request.json:
        return jsonify({'error': 'Empty request'})
    elif not all(key in request.json for key in ['address', 'age', 'email', 'modified_date', 'name', 'position', 'surname', 'speciality', 'password_hash']):
        return jsonify({'error': 'Bad request'})

    session = db_session.create_session()
    if 'id' in request.json:
        if session.query(User).filter(User.id == id_user).first():
            return jsonify({'error': 'Exception'})
    if session.query(User).filter(User.email == request.json['email']).first():
        return jsonify({'error': 'Email already exists'})

    user = session.query(User).filter(User.id == id_user).first()
    user.address = request.json['address'],
    user.age = request.json['age'],
    user.email = request.json['email'],
    user.modified_date = request.json['modified_date'],
    user.name = request.json['name'],
    user.position = request.json['position'],
    user.surname = request.json['surname'],
    user.speciality = request.json['speciality'],
    user.password_hash = request.json['password_hash'],
    session.commit()
    return jsonify({'success': 'OK'})
