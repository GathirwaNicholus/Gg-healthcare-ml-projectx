from sqlalchemy import (
    Column, Integer, Float, String, MetaData, Table
)
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class CleanedPatient(Base):
    __tablename__ = "cleaned_patients"

    id                = Column(Integer, primary_key=True, autoincrement=True)
    age               = Column(Integer,  nullable=False)
    gender            = Column(String,   nullable=False)
    blood_type        = Column(String,   nullable=False)
    medical_condition = Column(String,   nullable=False)
    hospital          = Column(String)
    insurance_provider= Column(String)
    billing_amount    = Column(Float,    nullable=False)
    room_number       = Column(Integer)
    admission_type    = Column(String,   nullable=False)
    medication        = Column(String)
    test_results      = Column(String,   nullable=False)   # target
    length_of_stay    = Column(Integer)
    admission_month   = Column(Integer)
    admission_year    = Column(Integer)

def create_tables(engine):
    Base.metadata.create_all(engine)
    print("[db] Tables created ")