from structure_builder.composites import ColumnMesh
import matplotlib.pyplot as plt


def test_column_printed_properly():
    column_mesh = ColumnMesh(bottom_height=1, radius=4, circle_n_points=50)
    ax = plt.axes(projection='3d')
    for level in column_mesh.cloud_points:
        ax.scatter3D(list(level.cloud_points['x'].values()),
                     list(level.cloud_points['y'].values()),
                     list(level.cloud_points['z'].values()))
    plt.show()
    assert True


def test_column_displaced():
    column_mesh = ColumnMesh(bottom_height=1,
                             radius=4,
                             circle_n_points=50, x_center=2.0, y_center=-3.0)
    ax = plt.axes(projection='3d')
    for level in column_mesh.cloud_points:
        ax.scatter3D(list(level.cloud_points['x'].values()),
                     list(level.cloud_points['y'].values()),
                     list(level.cloud_points['z'].values()))
    plt.show()
    assert True
