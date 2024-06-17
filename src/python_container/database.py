import os
from sqlalchemy import create_engine, Column, String, Float, DateTime, Integer
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

DATABASE_URI = os.getenv('DATABASE_URI')
engine = create_engine(DATABASE_URI, echo=False)
Base = declarative_base()

class Candlestick(Base):
    __tablename__ = 'candlestick_data'
    id = Column(Integer, primary_key=True)
    time = Column(DateTime, nullable=False)
    open_price = Column(Float, nullable=False)
    close_price = Column(Float, nullable=False)
    high_price = Column(Float, nullable=False)
    low_price = Column(Float, nullable=False)
    volume = Column(Float, nullable=False)
    symbol = Column(String(10), nullable=False)

Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()
