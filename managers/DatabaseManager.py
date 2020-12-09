from models.lectгurers import Lect
from models.intervals import Intervals
from models.groups import Group
from models.subjects import Subj
from models.schedule import Schedule

class DatabaseManager:
    def __init__(self, db):
        self.db = db

    def add_interval(self, **kwargs):
        interval = Intervals(interval=kwargs["interval"])
        self.db.session.add(interval)
        self.db.session.commit()

    def add_group(self, **kwargs):
        group = Group(name=kwargs["name"] )
        self.db.session.add(group)
        self.db.session.commit()

    def add_subject(self, **kwargs):
        subject = Subj(subject_name=kwargs["subject_name"], )
        self.db.session.add(subject)
        self.db.session.commit()

    def add_lecturer(self, **kwargs):
        lecturer = Lect(name=kwargs["name"],
                        last_name=kwargs["last_name"],
                        surname=kwargs["surname"])
        self.db.session.add(lecturer)
        self.db.session.commit()


    def add_schedule(self, **kwargs):
        schedule = Schedule(day=kwargs["day"],
                            chet=kwargs["chet"],
                            group_id=kwargs["group_id"],
                            interval_id=kwargs["interval_id"],
                            subject_id=kwargs["subject_id"],
                            lecturer_id=kwargs["lecturer_id"])
        self.db.session.add(schedule)
        self.db.session.commit()
