from DermAlertMS_Core.Entities.Person import base
from DermAlertMS_Core.Entities.Patient import Patient
from sqlalchemy import Column, String, Date, Integer, Numeric, func,ForeignKey
from sqlalchemy.orm import relationship


class Evaluation(base):
    __tablename__ = 'evaluation'

    id = Column(Integer, primary_key=True)
    username = Column(String(15),ForeignKey('patient.username'), nullable=False)
    result = Column(Numeric(2, 2), nullable=False)
    image = Column(String(500), nullable=False)
    created_at = Column(Date, default=func.now())
    updated_at = Column(Date, nullable=True)
    patient = relationship("Patient", uselist=False,foreign_keys=[username])

    def __repr__(self):
        return self.id