import pandas as pd
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from src.models import Train, Schedule, Base

# Read schedules CSV
df = pd.read_csv('data/schedules.csv')

# Connect to database
engine = create_engine('sqlite:///railway.db')
Session = sessionmaker(bind=engine)
session = Session()

# Seed trains and schedules
for _, row in df.iterrows():
	train_name = row['train_name']
	priority = row.get('priority', 1)

	# Check if train already exists
	train = session.query(Train).filter_by(train_name=train_name).first()
	if not train:
		train = Train(train_name=train_name, priority=priority)
		session.add(train)
		session.commit()

	# Create schedule
	schedule = Schedule(
		train_id=train.train_id,
		station_id=row['station_id'],
		arrival_time=row['arrival_time'],
		departure_time=row['departure_time']
	)
	session.add(schedule)

session.commit()
session.close()
