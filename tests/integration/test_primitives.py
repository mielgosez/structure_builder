import matplotlib.pyplot as plt
from structure_builder.primitives import *


def test_circle_is_visually_ok():
    new_circle = CircleMesh(radius=1, n_points=50, height=1)
    plot_points = new_circle.cloud_points.coordinates_dict
    plt.scatter(plot_points['x'].values(), plot_points['y'].values())
    plt.show()
    assert True


def test_rectangle_is_visually_ok():
    new_rectangle = RectangularMesh(n_points=50, width=10, length=10, height=0)
    plot_points = new_rectangle.cloud_points.coordinates_dict
    plt.scatter(plot_points['x'].values(), plot_points['y'].values(), alpha=0.5)
    plt.show()
