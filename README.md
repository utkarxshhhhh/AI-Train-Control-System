# AI-Powered Train Traffic Control System 🚂

This project is an intelligent decision-support system designed to optimize train movements, maximize section throughput, and improve punctuality on railway networks. It was developed as a solution for the Smart India Hackathon (SIH).

## ✨ Features

- **Railway Network Modeling:** Represents real-world railway networks, including stations and tracks with specific attributes (e.g., length, speed limits).
- **Discrete-Event Simulation:** A core simulator built with `SimPy` to model individual train journeys and calculate realistic travel times.
- **Interactive API:** A backend built with **FastAPI** provides an interface to trigger simulations on demand.
- **AI-Powered Optimization:** A scheduler built with **Google OR-Tools** to solve complex scheduling problems, find conflict-free train paths, and minimize delays.
- **Web Dashboard:** An interactive dashboard created with **Streamlit** to visualize the network, run simulations, and view optimized schedules.
- **Database Integration:** Uses **SQLAlchemy** and **SQLite** to store and manage train, station, and schedule data.

## 🛠️ Tech Stack

- **Backend:** Python, FastAPI
- **Frontend:** Streamlit
- **AI & Optimization:** Google OR-Tools (CP-SAT Solver)
- **Simulation:** SimPy
- **Database:** SQLAlchemy, SQLite
- **Data Handling:** Pandas, NetworkX

## 🚀 Setup and Installation

1.  Clone the repository:
    ```bash
    git clone [https://github.com/utkarxshhhhh/AI-Train-Control-System.git](https://github.com/utkarxshhhhh/AI-Train-Control-System.git)
    ```
2.  Navigate to the project directory:
    ```bash
    cd AI-Train-Control-System
    ```
3.  Create and activate a virtual environment:
    ```bash
    # For Windows
    python -m venv .venv
    .\.venv\Scripts\Activate.ps1
    ```
4.  Install the required packages:
    ```bash
    pip install -r requirements.txt
    ```

## Usage

There are two main components to run in separate terminals.

### 1. Backend Server (API)

The FastAPI server provides the API for simulations.
```bash
python -m uvicorn main:app --reload
