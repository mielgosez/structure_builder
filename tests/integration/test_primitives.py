import matplotlib.pyplot as plt
from structure_builder.primitives import *


def test_circle_is_visually_ok():
    new_circle = CircleMesh(radius=1, n_points=50, height=1)
    plot_points = new_circle.cloud_points.coordinates_dict
    plt.scatter(plot_points['x'].values(), plot_points['y'].values())
    plt.show()
    assert True


def test_rectangle_is_visually_ok():
    new_rectangle = RectangularMesh(n_points=50, width=10, length=5, height=0)
    plot_points = new_rectangle.cloud_points.coordinates_dict
    plt.scatter(plot_points['x'].values(), plot_points['y'].values(), alpha=0.5)
    plt.show()


def test_rectangle_optimum_coarseness():
    n_list = list()
    width_error_list = list()
    length_error_list = list()
    length = 10
    width = 20
    for n in range(10, 200, 10):
        new_rectangle = RectangularMesh(n_points=n, width=width, length=length, height=0)
        coordinates = new_rectangle.cloud_points.coordinates_dict
        n_list.append(n)
        granularity = math.ceil(n/8)
        width_error = (width/2 - (coordinates['x'][granularity] - coordinates['x'][2*granularity-1])) / (width/2)
        width_error_list.append(width_error)
        length_error = (length/2 - (coordinates['y'][granularity-1] - coordinates['y'][0])) / (length/2)
        length_error_list.append(length_error)
    plt.scatter(n_list, width_error_list, label='Width Error')
    plt.scatter(n_list, length_error_list, label='Length Error')
    plt.legend()
    plt.xlabel('Number of Points')
    plt.ylabel('Relative Error')
    plt.show()
