import tkinter as tk
from .model import TrajectoryModel
from .view import TrajectoryView

class TrajectoryController:
    def __init__(self, model: TrajectoryModel, view: TrajectoryView):
        self.model = model
        self.view = view
        self.view.button_plot.config(command=self.handle_plot_request)

    def handle_plot_request(self) -> None:
        try:
            v0, angle, g = self.view.get_inputs()
            x, y = self.model.calculate(v0, angle, g)
            self.view.plot_trajectory(x, y)
        except ValueError as e:
            self.view.show_error(str(e))
        except tk.TclError:
            self.view.show_error("Please enter valid numeric values.")
        except Exception as e:
            self.view.show_error(f"Unexpected error: {str(e)}")
