from ortools.sat.python import cp_model

class Scheduler:
	def __init__(self, railway_network):
		self.railway_network = railway_network
		self.model = cp_model.CpModel()

	def solve(self):
		from sqlalchemy import create_engine
		from sqlalchemy.orm import sessionmaker
		from src.models import Schedule, Train
		import datetime

		# Connect to DB
		engine = create_engine('sqlite:///railway.db')
		Session = sessionmaker(bind=engine)
		session = Session()

		# Query all schedules
		schedules = session.query(Schedule).all()

		interval_vars = []
		train_names = []
		for sched in schedules:
			train = session.query(Train).filter_by(train_id=sched.train_id).first()
			name = train.train_name if train else f"Train_{sched.train_id}"
			# Assume duration in minutes (departure - arrival)
			duration = int((sched.departure_time - sched.arrival_time).total_seconds() // 60)
			start_minute = int(sched.arrival_time.hour * 60 + sched.arrival_time.minute)
			end_minute = start_minute + duration
			start = self.model.NewIntVar(start_minute, start_minute, f"start_{name}")
			end = self.model.NewIntVar(end_minute, end_minute, f"end_{name}")
			interval = self.model.NewIntervalVar(start, duration, end, f"interval_{name}")
			interval_vars.append(interval)
			train_names.append(name)

		# Add no-overlap constraint
		self.model.AddNoOverlap(interval_vars)

		# Solve
		solver = cp_model.CpSolver()
		status = solver.Solve(self.model)

		results = []
		if status == cp_model.OPTIMAL or status == cp_model.FEASIBLE:
			for name in train_names:
				start_var = self.model.GetVarByName(f"start_{name}")
				end_var = self.model.GetVarByName(f"end_{name}")
				start_time = solver.Value(start_var)
				end_time = solver.Value(end_var)
				results.append(f"Train '{name}': Scheduled from {start_time} to {end_time}")
		else:
			results.append("No solution found.")
		session.close()
		return results
