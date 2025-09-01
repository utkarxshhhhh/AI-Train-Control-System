import simpy
from src.network import RailwayNetwork

class SimulationTrain:
    """A simple class to hold the state of a train in the simulation."""
    def __init__(self, train_id, name):
        self.train_id = train_id
        self.name = name
        self.current_location = None
        self.status = 'PARKED'

class Simulator:
    """Manages the discrete-event simulation of train traffic."""
    def __init__(self, network: RailwayNetwork):
        self.env = simpy.Environment()
        self.network = network

    def run_train_journey(self, train: SimulationTrain, start_station_id, end_station_id, log_event=None):
        """A simpy process that simulates a train's journey across multiple stations."""
        import networkx as nx
        train.current_location = start_station_id
        train.status = 'AT_STATION'
        msg1 = f"[Time: {self.env.now:.2f}] Train '{train.name}' is at Station {start_station_id}."
        if log_event:
            log_event(msg1)
        else:
            print(msg1)

        # Find path
        try:
            path = nx.shortest_path(self.network.graph, start_station_id, end_station_id)
        except nx.NetworkXNoPath:
            error_msg = f"No path found from Station {start_station_id} to Station {end_station_id}. Simulation aborted."
            if log_event:
                log_event(error_msg)
            else:
                print(error_msg)
            return

        # Simulate journey along the path
        for i in range(len(path) - 1):
            from_station = path[i]
            to_station = path[i + 1]
            msg_depart = f"[Time: {self.env.now:.2f}] Train '{train.name}' is departing Station {from_station} for Station {to_station}."
            if log_event:
                log_event(msg_depart)
            else:
                print(msg_depart)
            train.status = 'IN_TRANSIT'

            if not self.network.graph.has_edge(from_station, to_station):
                error_msg = f"No track found from Station {from_station} to Station {to_station}. Simulation aborted."
                if log_event:
                    log_event(error_msg)
                else:
                    print(error_msg)
                return

            track = self.network.graph.edges[from_station, to_station]
            travel_time_minutes = (track['length_km'] / track['speed_limit_kmh']) * 60
            yield self.env.timeout(travel_time_minutes)

            train.current_location = to_station
            train.status = 'AT_STATION'
            msg_arrive = f"[Time: {self.env.now:.2f}] Train '{train.name}' has arrived at Station {to_station}."
            if log_event:
                log_event(msg_arrive)
            else:
                print(msg_arrive)