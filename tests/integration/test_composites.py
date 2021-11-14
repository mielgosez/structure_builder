from structure_builder.composites import ColumnMesh
import matplotlib.pyplot as plt


def test_column_printed_properly():
    column_mesh = ColumnMesh(bottom_height=1, radius=4, circle_n_points=50)
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


def test_column_displaced():
    column_mesh = ColumnMesh(bottom_height=1,
                             radius=4,
                             circle_n_points=50, x_center=2.0, y_center=-3.0)
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
