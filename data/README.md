# AI-Powered Train Traffic Control System 🚂

This project is an intelligent decision-support system designed to optimize train movements, maximize section throughput, and improve punctuality on railway networks. It was developed as a solution for the Smart India Hackathon (SIH).

## ✨ Features

* **Railway Network Modeling:** Represents real-world railway networks, including stations and tracks with specific attributes.
* **Discrete-Event Simulation:** A core simulator built with `SimPy` to model train journeys and calculate travel times.
* **Interactive API:** A backend built with **FastAPI** allows for triggering simulations on demand.
* **AI-Powered Optimization:** A scheduler built with **Google OR-Tools** to solve complex scheduling problems and find conflict-free train paths.
* **Web Dashboard:** An interactive dashboard created with **Streamlit** to visualize the network and simulation results.

## 🛠️ Tech Stack

* **Backend:** Python, FastAPI
* **Frontend:** Streamlit
* **AI & Optimization:** Google OR-Tools (CP-SAT Solver)
* **Simulation:** SimPy
* **Database:** SQLAlchemy, SQLite
* **Data Handling:** Pandas, NetworkX

## 🚀 Setup and Installation

1.  Clone the repository:
    `git clone https://github.com/utkarxshhhhh/AI-Train-Control-System.git`
2.  Navigate to the project directory:
    `cd AI-Train-Control-System`
3.  Install the required packages:
    `pip install -r requirements.txt`

## Usage

There are two main components to run:

### 1. Backend Server

The FastAPI server provides the API for simulations.
```bash
python -m uvicorn main:app --reload
