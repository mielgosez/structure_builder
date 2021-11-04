import random
from structure_builder.primitives import *


def test_number_of_points_in_circle():
    n_points = random.randint(5, 10)
    new_circle = CircleMesh(radius=1, n_points=n_points, height=1)
    assert len(new_circle.cloud_points['x'].keys()) == n_points
