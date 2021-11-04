from structure_builder.primitives import CircleMesh


class ColumnMesh:
    def __init__(self, bottom_height: float, radius: float, circle_n_points: int = 20):
        self.__bottom_height = bottom_height
        self.__radius = radius
        self.__circle_n_points = circle_n_points
        self.__cloud_points = None
        self.create_cloud_points()

    def create_cloud_points(self):
        diameter = 2*self.radius
        smallest_diameter = 7/8*diameter
        greatest_diameter_difference = 1/8*diameter
        cloud_points = []
        for i in range(8):
            diameter_difference = (7-i)*greatest_diameter_difference/7
            local_diameter = smallest_diameter+diameter_difference
            new_circle = CircleMesh(radius=local_diameter/2,
                                    n_points=self.circle_n_points,
                                    height=diameter*(i+self.bottom_height))
            cloud_points.append(new_circle)
        self.cloud_points = cloud_points

    # Getters and setters
    @property
    def cloud_points(self):
        return self.__cloud_points

    @cloud_points.setter
    def cloud_points(self, new_cloud: list):
        self.__cloud_points = new_cloud

    @property
    def bottom_height(self):
        return self.__bottom_height

    @property
    def radius(self):
        return self.__radius

    @property
    def circle_n_points(self):
        return self.__circle_n_points
