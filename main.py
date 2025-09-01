from fastapi import FastAPI
from sqlalchemy import create_engine
from src.models import Base
from src.network import RailwayNetwork
from fastapi import FastAPI
from sqlalchemy import create_engine
from src.models import Base
from src.network import RailwayNetwork
from src.optimizer import Scheduler

# --- Setup ---
engine = create_engine("sqlite:///railway.db")
Base.metadata.create_all(bind=engine)
app = FastAPI()

# --- Load the railway network on startup ---
print("="*30)
print("LOADING RAILWAY NETWORK...")
network = RailwayNetwork()
network.load_from_files(
    stations_csv_path='data/stations.csv',
    tracks_csv_path='data/tracks.csv'
)
print(f"Network loaded with stations: {list(network.graph.nodes)}")
print("="*30)

# --- Run the optimizer ---
scheduler = Scheduler(network)
scheduler.solve()

@app.get("/")
async def root():
    return {"message": "Server is running"}