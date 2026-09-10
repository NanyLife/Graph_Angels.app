import tkinter as tk
from src.model import TrajectoryModel
from src.view import TrajectoryView
from src.controller import TrajectoryController

def main() -> None:
    root = tk.Tk()

    model = TrajectoryModel()
    view = TrajectoryView(root)
    controller = TrajectoryController(model, view)

    root.mainloop()

if __name__ == "__main__":
    main()
