from structure_builder.primitives import CircleMesh


class ColumnMesh:
    def __init__(self,
                 bottom_height: float,
                 radius: float,
                 circle_n_points: int = 20,
                 x_center: float = 0.0,
                 y_center: float = 0.0):
        self.__x_center = x_center
        self.__y_center = y_center
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
                                    height=diameter*(i+self.bottom_height),
                                    x_center=self.x_center,
                                    y_center=self.y_center)
            cloud_points.append(new_circle)
        self.cloud_points = cloud_points

    # Getters and setters
    @property
    def x_center(self):
        return self.__x_center

    @x_center.setter
    def x_center(self, new_x: float):
        self.__x_center = new_x

    @property
    def y_center(self):
        return self.__y_center

    @y_center.setter
    def y_center(self, new_y: float):
        self.__y_center = new_y

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
