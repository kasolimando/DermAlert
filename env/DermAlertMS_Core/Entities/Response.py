from DermAlertMS_Core.Entities.Person import base
from DermAlertMS_Core.Entities.Patient import Patient
from DermAlertMS_Core.Entities.Survey import Survey
from sqlalchemy import Column, String, Date, Integer, ForeignKey, func
from sqlalchemy.orm import relationship


class Response(base):
    __tablename__ = 'response'

    id = Column(Integer, ForeignKey('survey.id'),  primary_key=True)
    username = Column(String(15), ForeignKey('patient.username'),  primary_key=True)
    answer = Column(String(500), nullable=False)
    created_at = Column(Date, default=func.now())
    updated_at = Column(Date, nullable=True)
    patient = relationship("Patient", uselist=False,foreign_keys=[username])
    survey = relationship("Survey",uselist=False,foreign_keys=[id])

    def __repr__(self):
        return self.id