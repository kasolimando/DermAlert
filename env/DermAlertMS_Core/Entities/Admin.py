from DermAlertMS_Core.Entities.Person import base
from sqlalchemy import Column, String, Date, func, ForeignKey
from sqlalchemy.orm import relationship

class Admin(base):
    __tablename__ = 'admin'

    username = Column(String(15), ForeignKey('person.username'),  primary_key=True)
    created_at = Column(Date, default=func.now())
    updated_at = Column(Date, nullable=True)
    person = relationship("Person", uselist=False,foreign_keys=[username])

    def __repr__(self):
        return self.username