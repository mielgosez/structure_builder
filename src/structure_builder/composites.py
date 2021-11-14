from structure_builder.primitives import BaseMesh, CircleMesh, RectangularMesh


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
        """
        Column is created from bottom to top in the loop.
        :return: cloud points is updated.
        """
        diameter = 2*self.radius
        smallest_diameter = 7/8*diameter
        greatest_diameter_difference = 1/8*diameter
        previous_cloud = None
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


class CubicMesh(BaseMesh):
    def __init__(self,
                 height: float,
                 length: float,
                 width: float,
                 square_n_points: int = 20,
                 x_center: float = 0.0,
                 y_center: float = 0.0):
        super().__init__(x_center=x_center,
                         y_center=y_center,
                         height=height,
                         n_points=square_n_points)
        self.__length = length
        self.__width = width
        self.create_cloud_points()

    def create_cloud_points(self):
        """
        Creating the points. It consists of top and bottom sides (that's why there's a loop with 2 elements)
        :return: cloud points is updated.
        """
        previous_cloud = None
        for i in range(2):
            local_height = i*self.height
            new_rectangle = RectangularMesh(
                n_points=self.n_points,
                width=self.width,
                length=self.length,
                height=local_height,
                x_center=self.x_center,
                y_center=self.y_center)
            cloud_points = new_rectangle.cloud_points
            if i == 0:
                self.cloud_points = cloud_points
            else:
                previous_cloud.child = new_rectangle.cloud_points
                new_rectangle.cloud_points.parent = previous_cloud
            previous_cloud = cloud_points

    # Getters and setters
    @property
    def length(self):
        return self.__length

    @length.setter
    def length(self, new_length: float):
        self.positive_checker(new_length, "Length of cube")
        self.__length = new_length
        self.create_cloud_points()

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, new_width: float):
        self.positive_checker(new_width, "Width of cube")
        self.__width = new_width
        self.create_cloud_points()
