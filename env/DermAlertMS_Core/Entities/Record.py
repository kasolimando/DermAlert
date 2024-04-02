from DermAlertMS_Core.Entities.Person import base
from DermAlertMS_Core.Entities.Evaluation import Evaluation
from sqlalchemy import Column, Date, Integer, func, ForeignKey
from sqlalchemy.orm import relationship

class Record(base):
    __tablename__ = 'record'

    id = Column(Integer, primary_key=True)
    id_evaluation = Column(Integer, ForeignKey('evaluation.id'),primary_key=True)
    seq_no = Column(Integer, nullable=False)
    created_at = Column(Date, default=func.now())
    evaluation = relationship("Evaluation", uselist=False,foreign_keys=[id_evaluation])

    def __repr__(self):
        return self.id