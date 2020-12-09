from flask.blueprints import Blueprint
from flask import render_template
from flask import request
from managers.DatabaseManager import DatabaseManager
from extensions import db

db_manager = DatabaseManager(db)

addSubject = Blueprint('addSubject', __name__,
                template_folder='templates',
                static_folder='static')


@addSubject.route('/addSubject')
def index5():
	return render_template('addSubject.html')


@addSubject.route('/addSubject', methods=['post', 'get'])
def addSubj():
    if request.method == 'POST':

        subject_name = request.form.get('subject_name')


    if subject_name:
        message = "Subject added successfuly"
        db_manager.add_subject(subject_name=subject_name)
    else:
        message = "error"

    return render_template('addSubject.html', message=message)