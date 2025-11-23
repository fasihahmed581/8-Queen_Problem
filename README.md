# 8-Queens Live Simulation GUI

This project is a **visual simulation of the 8-Queens problem** using Python and Tkinter. It allows users to observe how two different algorithms—**Hill Climbing** and **CSP Backtracking**—solve the 8-Queens problem in real time.

---

## Table of Contents
- [Features](#features)
- [Algorithms](#algorithms)
- [Requirements](#requirements)
- [Installation](#installation)
- [Usage](#usage)
- [Screenshots](#screenshots)
- [License](#license)

---

## Features
- Interactive GUI built with Tkinter.
- Visual representation of the chessboard and queens placement.
- Live simulation of the solving process.
- Adjustable speed for simulation updates.
- Supports two algorithms:
  - Hill Climbing
  - CSP Backtracking
- Random board reset functionality.

---

## Algorithms

### Hill Climbing
- Starts with a random board.
- Iteratively moves queens to reduce conflicts.
- Performs **random restarts** if no improvement is found.

### CSP (Constraint Satisfaction Problem) Backtracking
- Systematically assigns queens to columns.
- Ensures no conflicts in rows, columns, or diagonals.
- Backtracks when a conflict is encountered.
- Updates GUI live as the algorithm explores the solution space.

---

## Requirements
- Python 3.x
- Tkinter (usually comes with Python)
- Standard Python libraries: `threading`, `random`, `time`

---

## Installation

1. Clone the repository or download the code:
   ```bash
   git clone <repository-url>

Usage
Jupyter Notebook

Open the notebook in Jupyter.

Run the cell containing the GUI code.

The Tkinter window will pop up.

Select the algorithm (Hill Climbing or CSP Backtracking).

Adjust the speed slider.

Click Run to start the simulation.

Click Reset to generate a new random board.

Python Script

Save the code in a .py file (e.g., queens_gui.py).
