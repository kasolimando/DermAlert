from abc import ABC, abstractmethod

class IDermAlertDBContext(ABC):

  @abstractmethod
  def __init__(self):
    pass
  
  @abstractmethod
  def getSession(self):
    pass

  @abstractmethod
  def getAll(self,model_cls):
    pass

  @abstractmethod
  def getByField(self, model_cls, field, value):
    pass

  @abstractmethod
  def getAllJoin(self, first_table, second_table):
    pass

  @abstractmethod
  def save(entity):
    pass
  
  @abstractmethod
  def delete(entity):
    pass

  @abstractmethod
  def Commit(self):
    pass
