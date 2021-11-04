from structure_builder.composites import ColumnMesh
import matplotlib.pyplot as plt


def test_column_printed_properly():
    column_mesh = ColumnMesh(bottom_height=1, radius=4, circle_n_points=50)
    for level in column_mesh.cloud_points:
        plt.scatter(list(level.cloud_points['x'].values()),
                    list(level.cloud_points['y'].values()),
                    list(level.cloud_points['z'].values()))
    plt.show()
    assert True
