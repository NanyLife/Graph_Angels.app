import tkinter as tk
from tkinter import messagebox
import matplotlib.pyplot as plt
import numpy as np

class TrajectoryView:
    def __init__(self, root: tk.Tk):
        self.root = root
        self.root.title("Projectile Motion Simulation")
        self.root.geometry("380x220")
        self.root.resizable(False, False)
        self._create_widgets()

    def _create_widgets(self) -> None:
        self.entry_velocity = self._create_input("Initial velocity (m/s):", 0)
        self.entry_angle = self._create_input("Launch angle (degrees):", 1)
        self.entry_gravity = self._create_input("Gravity acceleration (m/s²):", 2)

        self.entry_velocity.insert(0, "20")
        self.entry_angle.insert(0, "45")
        self.entry_gravity.insert(0, "9.81")

        self.button_plot = tk.Button(self.root, text="Plot Graph", width=25)
        self.button_plot.grid(row=3, column=0, columnspan=2, pady=15)

    def _create_input(self, label_text: str, row: int) -> tk.Entry:
        label = tk.Label(self.root, text=label_text, anchor="w")
        label.grid(row=row, column=0, padx=15, pady=5, sticky="w")
        entry = tk.Entry(self.root, width=25)
        entry.grid(row=row, column=1, padx=15, pady=5)
        return entry

    def get_inputs(self) -> tuple[float, float, float]:
        return (
            float(self.entry_velocity.get()),
            float(self.entry_angle.get()),
            float(self.entry_gravity.get())
        )

    def show_error(self, message: str) -> None:
        messagebox.showerror("Input Error", message)

    def plot_trajectory(self, x: np.ndarray, y: np.ndarray) -> None:
        plt.figure(figsize=(8, 6))
        plt.plot(x, y, label="Trajectory", color="blue")
        plt.title("Projectile Trajectory")
        plt.xlabel("Distance S (m)")
        plt.ylabel("Height h (m)")
        plt.grid(True, linestyle="--", alpha=0.7)
        plt.legend()
        plt.axhline(0, color="black", linewidth=1)
        plt.axvline(0, color="black", linewidth=1)
        plt.show()
