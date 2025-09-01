from sqlalchemy import Column, Integer, String, Float, ForeignKey, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()

class Train(Base):
	__tablename__ = 'trains'
	train_id = Column(Integer, primary_key=True, autoincrement=True)
	train_name = Column(String, nullable=False)
	priority = Column(Integer, nullable=False)
	# Relationship to schedules
	schedules = relationship('Schedule', back_populates='train')

class Station(Base):
	__tablename__ = 'stations'
	station_id = Column(Integer, primary_key=True, autoincrement=True)
	station_name = Column(String, nullable=False, unique=True)
	# Relationship to schedules
	schedules = relationship('Schedule', back_populates='station')

class TrackSection(Base):
	__tablename__ = 'track_sections'
	track_id = Column(Integer, primary_key=True, autoincrement=True)
	track_name = Column(String, nullable=False, unique=True)
	track_length = Column(Float, nullable=False)

class Schedule(Base):
	__tablename__ = 'schedules'
	schedule_id = Column(Integer, primary_key=True, autoincrement=True)
	train_id = Column(Integer, ForeignKey('trains.train_id'), nullable=False)
	station_id = Column(Integer, ForeignKey('stations.station_id'), nullable=False)
	arrival_time = Column(DateTime, nullable=False)
	departure_time = Column(DateTime, nullable=False)
	# Relationships
	train = relationship('Train', back_populates='schedules')
	station = relationship('Station', back_populates='schedules')
