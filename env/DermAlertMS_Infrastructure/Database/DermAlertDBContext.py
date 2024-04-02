from flask_sqlalchemy import SQLAlchemy
from DermAlertMS_Core.Database.IDermAlertDBContext import IDermAlertDBContext
from DermAlertMS_Core.Entities.Person import Person
from DermAlertMS_Core.Entities.Patient import Patient

class DermAlertDBContext(IDermAlertDBContext):

  def __init__(self,app):
    self.db = SQLAlchemy(app) 

  def getSession(self):
    return self.db

  def getAll(self,model_cls):
    return self.db.session.query(model_cls).all()

  def getByField(self, model_cls, field, value):
    return self.db.session.query(model_cls).filter(getattr(model_cls, field) == value).first()


  def getAllJoin(self, first_table, second_table):
    return self.db.session.query(first_table,second_table).join(second_table).all()

  def save(self,entity):
    self.db.session.add(entity)
    self.db.session.commit()
  
  def delete(self,entity):
    self.db.session.delete(entity)
    self.db.session.commit()

  def Commit(self):
    self.db.session.commit()
