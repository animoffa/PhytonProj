from flask.blueprints import Blueprint
from flask import render_template,request
from managers.DatabaseManager import DatabaseManager
from extensions import db

db_manager = DatabaseManager(db)

addGroup = Blueprint('addGroup', __name__,
                template_folder='templates',
                static_folder='static')


@addGroup.route('/addGroup')
def index4():
	return render_template('addGroup.html')


@addGroup.route('/addGroup', methods=['post', 'get'])
def addGr():
    if request.method == 'POST':

        name = request.form.get('name')


    if name:
        message = ""
        db_manager.add_group(name=name)
    else:
        message = "error"

    return render_template('addGroup.html', message=message)