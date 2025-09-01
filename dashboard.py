import streamlit as st
st.title("AI Train Traffic Control Dashboard")


import pandas as pd
from src.network import RailwayNetwork
from src.simulator import Simulator, SimulationTrain

st.title("AI Train Traffic Control Dashboard")

# Load network data
network = RailwayNetwork()
network.load_from_files('data/stations.csv', 'data/tracks.csv')

# Network Map Visualization
st.subheader("Network Map")
dot = "digraph G {"
for node in network.graph.nodes:
	dot += f'  {node} [label="{network.graph.nodes[node].get('name', node)}"]\n'
for u, v, data in network.graph.edges(data=True):
	label = f"{data.get('length', '')}km / {data.get('speed_limit', '')}km/h"
	dot += f'  {u} -> {v} [label="{label}"]\n'
dot += "}"
st.graphviz_chart(dot)

# Divider and Single Journey Simulation
st.divider()
st.subheader("Run a Single Journey Simulation")
station_names = [network.graph.nodes[node].get('name', str(node)) for node in network.graph.nodes]
start_station = st.selectbox("Start Station", station_names)
end_station = st.selectbox("End Station", station_names)

if st.button("Run Simulation"):
	name_to_id = {network.graph.nodes[node].get('name', str(node)): node for node in network.graph.nodes}
	start_id = name_to_id[start_station]
	end_id = name_to_id[end_station]

	sim = Simulator(network)
	train = SimulationTrain(train_id=9999, name="Dashboard Test Train")

	# Collect and display simulation events in real-time
	events = []
	def log_event(event):
		events.append(str(event))
		st.info(str(event))

	sim.env.process(sim.run_train_journey(train, start_id, end_id, log_event=log_event))
	sim.env.run()

	st.write(f"Simulation complete for train {train.name} from {start_station} to {end_station}.")
