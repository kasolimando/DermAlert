from DermAlertMS_Core.Entities.Person import base
from DermAlertMS_Core.Entities.Degree import Degree
from DermAlertMS_Core.Entities.Speciality import Speciality
from DermAlertMS_Core.Entities.University import University
from sqlalchemy import Column, String, Date, Integer, ForeignKey, func
from sqlalchemy.orm import relationship


class Doctor(base):
    __tablename__ = 'doctor'

    username = Column(String(15), ForeignKey('person.username'), primary_key=True)
    contact = Column(String(30), nullable=False)
    gradution_year = Column(String(5), nullable=False)
    address = Column(String(300), nullable=False)
    created_at = Column(Date, default=func.now())
    updated_at = Column(Date, nullable=True)
    degree = Column(Integer, ForeignKey('degree.id'),nullable=False)
    speciality = Column(Integer,ForeignKey('speciality.id'), nullable=False)
    university = Column(Integer, ForeignKey('university.id'), nullable=False)
    person = relationship("Person", uselist=False,foreign_keys=[username])
    degree_info = relationship("Degree", uselist=False,foreign_keys=[degree])
    speciality_info = relationship("Speciality", uselist=False,foreign_keys=[speciality])
    university_info = relationship("University", uselist=False,foreign_keys=[university])

    def __repr__(self):
        return self.username