from structure_builder.primitives import BaseMesh, CircleMesh


class ColumnMesh(BaseMesh):
    def __init__(self,
                 bottom_height: float,
                 radius: float,
                 circle_n_points: int = 20,
                 x_center: float = 0.0,
                 y_center: float = 0.0):
        super().__init__(x_center=x_center,
                         y_center=y_center,
                         height=bottom_height,
                         n_points=circle_n_points)
        self.__radius = radius
        self.create_cloud_points()

    def create_cloud_points(self):
        diameter = 2*self.radius
        smallest_diameter = 7/8*diameter
        greatest_diameter_difference = 1/8*diameter
        for i in range(8):
            diameter_difference = (7-i)*greatest_diameter_difference/7
            local_diameter = smallest_diameter+diameter_difference
            new_circle = CircleMesh(radius=local_diameter/2,
                                    n_points=self.n_points,
                                    height=diameter*(i+self.height),
                                    x_center=self.x_center,
                                    y_center=self.y_center)
            cloud_points = new_circle.cloud_points
            if i == 0:
                self.cloud_points = cloud_points
            else:
                previous_cloud.child = new_circle.cloud_points
                new_circle.cloud_points.parent = previous_cloud
            previous_cloud = cloud_points

    # Getters and setters
    @property
    def radius(self):
        return self.__radius
