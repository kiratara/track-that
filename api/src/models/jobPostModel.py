from db import db

# 1: {'id':1, 'role':'Analyst', 'company':'Big Bear Co.', 'status': 'new', 'url': 'http://www.google.com'},

class JobPostModel(db.Model):
    '''Model definition for the JobPost'''
    __tablename__ = "jobPost"

    id = db.Column(db.Integer, primary_key=True)
    role = db.Column(db.String(40))
    company = db.Column(db.String(40))
    status = db.Column(db.String(40))
    url = db.Column(db.Text())

    def __init__(self, role, company, status, url):
        '''Initiate JobPostModel object
        '''
        self.role = role
        self.company = company
        self.status = status
        self.url = url

    def json(self):
        '''Return JSON representation of the JobPost object
        '''
        return {'id': self.id, 'role':self.role, "company":self.company, "status":self.status}
    
    def save_to_db(self):
        '''save JobPost object to the database'''
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        '''Delete record from the database'''
        db.session.delete(self)
        db.session.commit()

    @classmethod
    def find_by_id(cls, _id):
        '''Find post on the database by id'''
        return cls.query.filter_by(id=_id).first()

    def __str__(self):
        '''unoffoficial string representation'''
        return f"JobPostModel object with title: {self.role} and status: {self.status}"
