import tkinter as tk
from tkinter import ttk
import time
import threading
import random

N = 8

# -------------------------------------
# Utility functions (from your notebook)
# -------------------------------------

def attacks(state):
    n = len(state)
    conflicts = 0
    for i in range(n):
        for j in range(i+1, n):
            if state[i] == state[j] or abs(state[i]-state[j]) == abs(i-j):
                conflicts += 1
    return conflicts

def random_state(n=N):
    return [random.randrange(n) for _ in range(n)]

# ---------------------------------------------------
# Hill Climbing (LIVE SIMULATION VERSION for the GUI)
# ---------------------------------------------------

def hill_climb_live(initial_state, gui_callback, sleep_time=0.3):
    n = N
    current = initial_state[:]
    current_conf = attacks(current)

    restarts = 0
    iterations = 0

    while restarts < 50:

        if current_conf == 0:
            gui_callback(current)
            return current

        improved = False
        best_move = None
        best_conf = current_conf

        for col in range(n):
            orig_row = current[col]
            for row in range(n):
                if row == orig_row:
                    continue
                cand = current[:]
                cand[col] = row
                c_conf = attacks(cand)
                if c_conf < best_conf:
                    best_conf = c_conf
                    best_move = (col, row, cand)

        if best_move:
            col, row, candidate = best_move
            current = candidate
            current_conf = best_conf
            iterations += 1

            gui_callback(current)
            time.sleep(sleep_time)
            continue

        # No improvement → random restart
        restarts += 1
        current = random_state(n)
        current_conf = attacks(current)
        gui_callback(current)
        time.sleep(sleep_time)

    return None

# ------------------------------------------
# CSP (backtracking) with GUI live updating
# ------------------------------------------

def csp_backtrack_live(gui_callback, sleep_time=0.3):
    domains = {col: set(range(N)) for col in range(N)}
    assignment = {}

    def is_consistent(col, row):
        for c, r in assignment.items():
            if r == row or abs(r-row) == abs(c-col):
                return False
        return True

    def backtrack():
        if len(assignment) == N:
            return True

        var = min([c for c in range(N) if c not in assignment],
                  key=lambda c: len(domains[c]))

        for val in sorted(domains[var]):
            if is_consistent(var, val):
                assignment[var] = val

                # Update GUI
                partial = [-1] * N
                for k, v in assignment.items():
                    partial[k] = v
                gui_callback(partial)
                time.sleep(sleep_time)

                if backtrack():
                    return True
                del assignment[var]

        return False

    result = backtrack()
    if not result:
        return None

    return [assignment[c] for c in range(N)]

# ----------------
# GUI APPLICATION
# ----------------

class QueensGUI:
    def __init__(self, root):
        self.root = root
        root.title("8-Queens Solver - Live Simulation")

        self.canvas = tk.Canvas(root, width=400, height=400)
        self.canvas.grid(row=0, column=0, rowspan=20)

        ttk.Label(root, text="Select Algorithm").grid(row=0, column=1)
        self.algo = ttk.Combobox(root, values=["Hill Climbing", "CSP Backtracking"])
        self.algo.current(0)
        self.algo.grid(row=1, column=1)

        ttk.Label(root, text="Speed").grid(row=2, column=1)
        self.speed = ttk.Scale(root, from_=0.05, to=1.0, value=0.3, orient="horizontal")
        self.speed.grid(row=3, column=1)

        ttk.Button(root, text="Run", command=self.run_simulation).grid(row=5, column=1)
        ttk.Button(root, text="Reset", command=self.reset_board).grid(row=6, column=1)

        self.state = random_state()
        self.draw_board(self.state)

    # Draw board
    def draw_board(self, state):
        self.canvas.delete("all")
        cell = 50

        for r in range(N):
            for c in range(N):
                color = "#EEE" if (r+c) % 2 == 0 else "#777"
                self.canvas.create_rectangle(c*cell, r*cell, (c+1)*cell, (r+1)*cell, fill=color)

                if state[c] == r:
                    self.canvas.create_text(c*cell+25, r*cell+25, text="♛", font=("Arial", 30), fill="red")

    def gui_update(self, state):
        self.root.after(0, lambda: self.draw_board(state))

    # Run in background thread
    def run_bg(self, func):
        thread = threading.Thread(target=func)
        thread.daemon = True
        thread.start()

    def run_simulation(self):
        algo = self.algo.get()
        speed = float(self.speed.get())

        if algo == "Hill Climbing":
            init = random_state()
            self.state = init
            self.run_bg(lambda: hill_climb_live(init, self.gui_update, speed))

        elif algo == "CSP Backtracking":
            self.run_bg(lambda: csp_backtrack_live(self.gui_update, speed))

    # Reset random board
    def reset_board(self):
        self.state = random_state()
        self.draw_board(self.state)


# ---- RUN APP ----
root = tk.Tk()
app = QueensGUI(root)
root.mainloop()
