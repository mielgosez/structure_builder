from structure_builder.composites import *


class ClassicalColumns(BaseMesh):
    def __init__(self,
                 height: float,
                 radius: float,
                 column_type: str = 'doric',
                 n_points: int = 20,
                 x_center: float = 0.0,
                 y_center: float = 0.0
                 ):
        super().__init__(n_points=n_points,
                         height=height,
                         x_center=x_center,
                         y_center=y_center)
        self.__radius = radius
        self.__column_type = column_type
        self.__smallest_ratio_proportion = None
        self.__height_in_number_of_diameters = None
        self.create_cloud_points()
        self.define_mesh_faces()

    def define_mesh_faces(self):
        reference_level = self.cloud_points
        node_list = list()
        face_list = list()
        level_count = 0
        while reference_level.child is not None:
            for i in range(self.n_points):
                node_list.append((reference_level.coordinates_dict['x'][i],
                                  reference_level.coordinates_dict['y'][i],
                                  reference_level.coordinates_dict['z'][i]))
                face_list.append((level_count * self.n_points + i,
                                  level_count * self.n_points + ((i + 1) % self.n_points),
                                  (level_count + 1) * self.n_points + i,
                                  (level_count + 1) * self.n_points + ((i + 1) % self.n_points),
                                  ))
            level_count += 1
            reference_level = reference_level.child
        return node_list, face_list

    def set_column_proportions(self):
        if self.column_type == 'doric':
            self.smallest_ratio_proportion = 7/8
            self.height_in_number_of_diameters = 8
        else:
            NotImplementedError(f'{self.column_type} has not being implemented as an classical order.')

    def create_cloud_points(self):
        self.set_column_proportions()
        diameter = 2*self.radius
        column = ColumnMesh(bottom_height=1.5*diameter,
                            radius=self.radius,
                            circle_n_points=self.n_points,
                            smallest_ratio_proportion=self.smallest_ratio_proportion,
                            height_in_number_of_diameters=self.height_in_number_of_diameters,
                            x_center=self.x_center,
                            y_center=self.y_center)
        base = CubicMesh(square_n_points=self.n_points,
                         width=diameter,
                         length=diameter,
                         height=1.5*diameter,
                         x_center=self.x_center,
                         y_center=self.y_center)
        self.cloud_points = base.cloud_points
        base.cloud_points.child.child = column.cloud_points

    # Getters and Setters
    @property
    def height_in_number_of_diameters(self):
        return self.__height_in_number_of_diameters

    @height_in_number_of_diameters.setter
    def height_in_number_of_diameters(self, new_height: int):
        self.__height_in_number_of_diameters = new_height

    @property
    def smallest_ratio_proportion(self):
        return self.__smallest_ratio_proportion

    @smallest_ratio_proportion.setter
    def smallest_ratio_proportion(self, new_proportion: float):
        self.__smallest_ratio_proportion = new_proportion

    @property
    def radius(self):
        return self.__radius

    @property
    def column_type(self):
        return self.__column_type
