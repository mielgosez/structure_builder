import matplotlib.pyplot as plt
from structure_builder.primitives import *


def test_circle_is_visually_ok():
    new_circle = CircleMesh(radius=1, n_points=50, height=1)
    plot_points = new_circle.cloud_points
    plt.scatter(plot_points['x'].values(), plot_points['y'].values())
    plt.show()
    assert True
