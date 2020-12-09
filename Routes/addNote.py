from flask.blueprints import Blueprint
from flask import render_template
from flask import request
from models.lectгurers import Lect
from models.subjects import Subj
from models.intervals import Intervals
from models.groups import Group
from managers.DatabaseManager import DatabaseManager
from extensions import db

db_manager = DatabaseManager(db)

addNote = Blueprint('addNote', __name__,
                template_folder='templates',
                static_folder='static')


@addNote.route('/addNote')
def index4():
	return render_template('addNote.html', lecturers=Lect.query.all(), groups=Group.query.all(), intervals=Intervals.query.all(), subjects = Subj.query.all())


@addNote.route('/addNote',methods=['post', 'get'])
def addN():
    if request.method == 'POST':
        interval = request.form.get('interval')
        chet = request.form.get('chet')
        day = request.form.get('day')
        subject = request.form.get('subject')
        lecturer = request.form.get('lecturer')
        group = request.form.get('group')

    if interval and subject and lecturer and group and chet and day:
        message = "Note added successfully"
        new_dict = {}
        new_dict["lect"] = lecturer
        new_dict["subj"] = subject
        new_dict["interv"] = interval
        new_dict["group"] = group
        new = lecturer.split()
        name = new[1]
        l_name = new[0]
        s_name = new[2]
        lecturer_id = db.session.query(Lect.id).filter(Lect.name == name, Lect.last_name == l_name, Lect.surname == s_name).first()[0]
        group_id = db.session.query(Group.id).filter(Group.name==group).first()[0]
        subject_id = db.session.query(Subj.id).filter(Subj.subject_name == subject).first()[0]
        interval_id = db.session.query(Intervals.id).filter(Intervals.interval == interval).first()[0]
        db_manager.add_schedule(day=day,chet=chet,group_id=group_id, interval_id = interval_id, subject_id = subject_id, lecturer_id= lecturer_id)
    else:
        message = "error"

    return render_template('addNote.html', message=message, prob=" ", lecturers=Lect.query.all(), groups=Group.query.all(), intervals=Intervals.query.all(), subjects = Subj.query.all())