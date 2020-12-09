from flask.blueprints import Blueprint
from flask import render_template
from models.lectгurers import Lect
from flask import request
from models.subjects import Subj
from models.intervals import Intervals
from models.groups import Group
from models.schedule import Schedule
from managers.DatabaseManager import DatabaseManager
from extensions import db

db_manager = DatabaseManager(db)

lecturers = Blueprint('lecturers', __name__,
                template_folder='templates',
                static_folder='static')

@lecturers.route('/')
def index():
    days = ["Понедельник", "Вторник", "Среда", "Четверг", "Пятница", "Суббота"]
    trv = ['9:30 - 11:05','11:20 - 12:55','13:10 - 14:45','15:25 - 17:00']
    cur_group = "БФИ1801"
    group_id = db.session.query(Group.id).filter(Group.name==cur_group).first()[0]
    schedule = db.session.query(Schedule).filter(Schedule.group_id==group_id)
    return render_template('index.html', cur_group=cur_group, days = days, trvs = trv, lecturers=Lect.query.all(), subjects=Subj.query.all(), intervals=Intervals.query.all(), group_names=Group.query.all(), schedules=schedule)

@lecturers.route('/',methods=['post', 'get'])
def chooseGroup():
    if request.method == 'POST':
        cur_group = request.form.get('cur_group')
    days = ["Понедельник", "Вторник", "Среда", "Четверг", "Пятница", "Суббота"]
    trv = ['9:30 - 11:05','11:20 - 12:55','13:10 - 14:45','15:25 - 17:00']
    message = ''
    group_id = db.session.query(Group.id).filter(Group.name==cur_group).first()[0]
    schedule = db.session.query(Schedule).filter(Schedule.group_id==group_id)

    return render_template('index.html', cur_group=cur_group, days = days, trvs = trv, lecturers=Lect.query.all(), subjects=Subj.query.all(), intervals=Intervals.query.all(), group_names=Group.query.all(), schedules=schedule)