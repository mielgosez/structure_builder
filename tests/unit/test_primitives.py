import random
from structure_builder.primitives import *


def test_number_of_points_in_circle():
    n_points = random.randint(5, 10)
    new_circle = CircleMesh(radius=1, n_points=n_points, height=1)
    assert len(new_circle.cloud_points.coordinates_dict['x'].keys()) == n_points


def test_distance_in_rectangular_is_ok():
    n_points = 50
    new_rectangle = RectangularMesh(n_points=n_points, width=20, length=10, height=0)
    coordinates = new_rectangle.cloud_points.coordinates_dict
    assert 20/2 - (coordinates['x'][7] - coordinates['x'][12]) < 3, 'Width is OK'
    assert 10/2 - (coordinates['y'][6] - coordinates['y'][0]) < 1, 'Length is OK'
