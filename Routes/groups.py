from flask.blueprints import Blueprint
from flask import render_template
from models.groups import Group

groups = Blueprint('groups', __name__,
				template_folder='templates',
				static_folder='static')


@groups.route('/groups')
def index1():
	return render_template('groups.html',groups=Group.query.all())