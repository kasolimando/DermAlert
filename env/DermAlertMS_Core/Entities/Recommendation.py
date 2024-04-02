from DermAlertMS_Core.Entities.Person import base
from DermAlertMS_Core.Entities.Admin import Admin
from sqlalchemy import Column, String, Date, Integer, ForeignKey, func
from sqlalchemy.orm import relationship

class Recommendation(base):
    __tablename__ = 'recommendation'

    id = Column(Integer, primary_key=True)
    description = Column(String(300), nullable=False)
    created_at = Column(Date, default=func.now())
    updated_at = Column(Date, nullable=True)
    entry_value = Column(Integer, nullable=False)
    end_value = Column(Integer, nullable=False)
    created_by = Column(String(15),ForeignKey('admin.username'), nullable=False)
    updated_by = Column(String(15),ForeignKey('admin.username'), nullable=True)
    created_admin = relationship("Admin", uselist=False,foreign_keys=[created_by])
    updated_admin = relationship("Admin", uselist=False,foreign_keys=[updated_by])

    def __repr__(self):
        return self.id

    def __init__(self, description,entry_value,end_value,created_by,updated_by):
        self.description = description
        self.entry_value = entry_value
        self.end_value = end_value
        self.created_by = created_by
        self.updated_by = updated_by