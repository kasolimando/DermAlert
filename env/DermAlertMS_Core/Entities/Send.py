from DermAlertMS_Core.Entities.Person import base
from sqlalchemy import Column, String, Date, Integer, func


class Send(base):
    __tablename__ = 'send'


    id_record = Column(Integer, nullable=False,primary_key=True)
    send_date = Column(Date, nullable=False, primary_key=True)
    created_at = Column(Date, default=func.now())

    def __repr__(self):
        return self.id_record