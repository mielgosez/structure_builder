from structure_builder.classical_structures import *
import matplotlib.pyplot as plt


def test_column_printed_properly():
    column_mesh = ClassicalColumns(height=1, radius=1, n_points=50)
    ax = plt.axes(projection='3d')
    current_mesh = column_mesh.cloud_points
    while current_mesh is not None:
        level = current_mesh.coordinates_dict
        ax.scatter3D(list(level['x'].values()),
                     list(level['y'].values()),
                     list(level['z'].values()))
        current_mesh = current_mesh.child
    plt.show()
    assert True
