import numpy as np

class TrajectoryModel:
    @staticmethod
    def calculate(v0: float, angle_degrees: float, g: float) -> tuple[np.ndarray, np.ndarray]:
        if v0 <= 0 or angle_degrees <= 0 or g <= 0:
            raise ValueError("All values must be strictly positive.")

        angle_radians = np.radians(angle_degrees)
        v_x = v0 * np.cos(angle_radians)
        v_y = v0 * np.sin(angle_radians)

        time_of_flight = (2 * v_y) / g
        t = np.linspace(0, time_of_flight, num=500)

        x = v_x * t
        y = v_y * t - 0.5 * g * t**2
        return x, y
