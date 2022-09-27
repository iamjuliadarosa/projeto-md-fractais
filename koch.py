import numpy as np
import matplotlib.pyplot as plt
def koch_snowflake(order, scale=10):
    def _koch_snowflake_complex(order):
        if order == 0:
            angles = np.array([0, 120, 240]) + 90
            return scale / np.sqrt(3) * np.exp(np.deg2rad(angles) * 1j)
        else:
            ZR = 0.5 - 0.5j * np.sqrt(3) / 3
            p1 = _koch_snowflake_complex(order - 1)
            p2 = np.roll(p1, shift=-1)
            dp = p2 - p1
            new_points = np.empty(len(p1) * 4, dtype=np.complex128)
            new_points[::4] = p1
            new_points[1::4] = p1 + dp / 3
            new_points[2::4] = p1 + dp * ZR
            new_points[3::4] = p1 + dp / 3 * 2
            return new_points
    points = _koch_snowflake_complex(order)
    x, y = points.real, points.imag
    return x, y

x, y = koch_snowflake(order=20)

plt.figure(figsize=(8, 8))
plt.axis('equal')
plt.fill(x, y, facecolor='none', edgecolor='blue', linewidth=1)
plt.show()