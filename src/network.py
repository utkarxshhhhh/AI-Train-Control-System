import networkx as nx
import pandas as pd

class RailwayNetwork:
    """
    Represents the railway network using a graph.
    Stations are nodes, and tracks are edges.
    """
    def __init__(self):
        """Initializes an empty railway network graph."""
        self.graph = nx.Graph()

    def add_station(self, station_id, name):
        """Adds a station (node) to the network graph."""
        self.graph.add_node(station_id, name=name)

    def add_track(self, from_station_id, to_station_id, length, speed_limit):
        """Adds a track (edge) between two stations."""
        self.graph.add_edge(
            from_station_id,
            to_station_id,
            length_km=length,
            speed_limit_kmh=speed_limit
        )

    def load_from_files(self, stations_csv_path, tracks_csv_path):
        """
        Loads the network topology from CSV files.
        
        Args:
            stations_csv_path (str): Path to the stations CSV file.
            tracks_csv_path (str): Path to the tracks CSV file.
        """
        # Load stations
        stations_df = pd.read_csv(stations_csv_path)
        for _, row in stations_df.iterrows():
            self.add_station(row['station_id'], row['name'])
            
        # Load tracks
        tracks_df = pd.read_csv(tracks_csv_path)
        for _, row in tracks_df.iterrows():
            self.add_track(
                row['from_station_id'],
                row['to_station_id'],
                row['length_km'],
                row['speed_limit_kmh']
            )
        print("Successfully loaded network data from files.")