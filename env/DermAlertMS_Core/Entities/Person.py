from sqlalchemy import Column, String, Date, func
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

base = declarative_base()

class Person(base):

    __tablename__ = 'person'
    username = Column(String(15), primary_key=True)
    name = Column(String(150), nullable=False)
    last_name = Column(String(150), nullable=False)
    phone = Column(String(30), nullable=False)
    birthdate = Column(Date, nullable=False)
    iden_doc = Column(String(30), nullable=True)
    address = Column(String(30), nullable=True)
    sex = Column(String(1), nullable=True)
    status = Column(String(1), nullable=True)
    email = Column(String(50), unique=True, nullable=False)
    password = Column(String(15), nullable=False)
    created_at = Column(Date, default=func.now())
    updated_at = Column(Date, default=func.now(),nullable=True)

    def __repr__(self):
        return self.username

    def __init__(self, username,name,last_name,phone,birthdate,iden_doc,address,sex,status,email,password,created_at,updated_at):
        self.username = username
        self.name = name
        self.last_name = last_name
        self.phone = phone
        self.birthdate = birthdate
        self.iden_doc = iden_doc
        self.address = address
        self.sex = sex
        self.status = status
        self.email = email
        self.password = password
        self.created_at = created_at
        self.updated_at = updated_at