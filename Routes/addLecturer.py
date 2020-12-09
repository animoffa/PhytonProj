from flask.blueprints import Blueprint
from flask import render_template
from flask import request
from managers.DatabaseManager import DatabaseManager
from extensions import db

db_manager = DatabaseManager(db)

addLecturer = Blueprint('addLecturer', __name__,
                template_folder='templates',
                static_folder='static')


@addLecturer.route('/addLecturer')
def index3():
	return render_template('addLecturer.html')


@addLecturer.route('/addLecturer', methods=['post', 'get'])
def addLec():
    if request.method == 'POST':
        last_name = request.form.get('last_name')
        name = request.form.get('name')
        surname = request.form.get('surname')

    if last_name and name and surname:
        message = ""
        db_manager.add_lecturer(name=name, last_name=last_name, surname=surname)
    else:
        message = "error!"

    return render_template('addLecturer.html', message=message)

