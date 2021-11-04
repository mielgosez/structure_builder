import math


class CircleMesh:
    def __init__(self, radius: float, n_points: int, height: float = 1.0):
        self.__height = height
        self.__radius = radius
        self.__n_points = n_points
        self.__cloud_points = None
        self.create_cloud_points()

    @staticmethod
    def positive_checker(quantity: float, quantity_name: str):
        if quantity <= 0:
            raise ValueError(f'{quantity_name} should be positive. Value inputted is equal to {quantity}')

    def create_cloud_points(self):
        cloud_points = {'x': {}, 'y': {}, 'z': {}}
        for i in range(self.n_points):
            cloud_points['x'][i] = self.radius*math.cos(2*math.pi*i/self.n_points)
            cloud_points['y'][i] = self.radius*math.sin(2*math.pi*i/self.n_points)
            cloud_points['z'][i] = self.height
        self.cloud_points = cloud_points

    # Getters and setters
    @property
    def cloud_points(self):
        return self.__cloud_points

    @cloud_points.setter
    def cloud_points(self, new_cloud: dict):
        self.__cloud_points = new_cloud

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, new_height: float):
        self.positive_checker(new_height, 'height')
        self.__height = new_height
        self.create_cloud_points()

    @property
    def radius(self):
        return self.__radius

    @radius.setter
    def radius(self, new_radius: float):
        self.positive_checker(new_radius, 'radius')
        self.__radius = new_radius
        self.create_cloud_points()

    @property
    def n_points(self):
        return self.__n_points

    @n_points.setter
    def n_points(self, n_points: int):
        if n_points < 5:
            raise ValueError(f'{n_points} is not a valid value for n_points. Please set a value'
                             f'higher or equal to 5.')
        else:
            self.__n_points = n_points
            self.create_cloud_points()
