import math
from abc import ABC, abstractmethod


class CloudPoints:
    def __init__(self,
                 coordinates_dict: dict = None,
                 parent=None,
                 child=None):
        self.__coordinates_dict = coordinates_dict
        self.__parent = parent
        self.__child = child

    @property
    def coordinates_dict(self):
        return self.__coordinates_dict

    @property
    def parent(self):
        return self.__parent

    @parent.setter
    def parent(self, new_parent):
        self.__parent = new_parent

    @property
    def child(self):
        return self.__child

    @child.setter
    def child(self, new_child):
        self.__child = new_child


class BaseMesh(ABC):
    def __init__(self,
                 n_points: int,
                 height: float = 1.0,
                 x_center: float = 0.0,
                 y_center: float = 0.0):
        self.__x_center = x_center
        self.__y_center = y_center
        self.__height = height
        self.__n_points = n_points
        self.__cloud_points = None

    @staticmethod
    def positive_checker(quantity: float, quantity_name: str):
        if quantity <= 0:
            raise ValueError(f'{quantity_name} should be positive. Value inputted is equal to {quantity}')

    @abstractmethod
    def create_cloud_points(self):
        pass

    # Getters and setters
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
    def cloud_points(self, new_cloud: CloudPoints):
        self.__cloud_points = new_cloud

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, new_height: float):
        self.positive_checker(new_height, 'height')
        self.__height = new_height
        self.create_cloud_points()


class RectangularMesh(BaseMesh):
    def __init__(self,
                 n_points: int,
                 width: float,
                 length: float,
                 height: float,
                 x_center: float = 0.0,
                 y_center: float = 0.0):
        super().__init__(n_points=n_points,
                         height=height,
                         x_center=x_center,
                         y_center=y_center)
        self.__width = width
        self.__length = length
        self.create_cloud_points()

    def create_cloud_points(self):
        cloud_points = {'x': {}, 'y': {}, 'z': {}}
        for i in range(self.n_points):
            angle_value = 2 * math.pi * i / self.n_points
            if angle_value <= math.pi/4:
                cloud_points['x'][i] = self.length/2
                cloud_points['y'][i] = self.length*math.tan(angle_value)/2
                cloud_points['z'][i] = self.height
            elif angle_value > 7*math.pi/4:
                angle_value -= 2*math.pi
                angle_value = abs(angle_value)
                cloud_points['x'][i] = self.length/2
                cloud_points['y'][i] = -self.length * math.tan(angle_value)/2
                cloud_points['z'][i] = self.height
            elif (angle_value > math.pi/4) and (angle_value <= math.pi/2):
                angle_value -= math.pi/2
                angle_value = abs(angle_value)
                cloud_points['x'][i] = self.width*math.tan(angle_value)/2
                cloud_points['y'][i] = self.width/2
                cloud_points['z'][i] = self.height
            elif (angle_value > math.pi/2) and (angle_value <= 3*math.pi/4):
                angle_value -= math.pi/2
                cloud_points['x'][i] = -self.width*math.tan(angle_value)/2
                cloud_points['y'][i] = self.width/2
                cloud_points['z'][i] = self.height
            elif (angle_value > 3*math.pi/4) and (angle_value <= math.pi):
                angle_value -= math.pi
                angle_value = abs(angle_value)
                cloud_points['x'][i] = -self.length/2
                cloud_points['y'][i] = self.length*math.tan(angle_value)/2
                cloud_points['z'][i] = self.height
            elif (angle_value > math.pi) and (angle_value <= 5*math.pi/4):
                angle_value -= math.pi
                cloud_points['x'][i] = -self.length/2
                cloud_points['y'][i] = -self.length*math.tan(angle_value)/2
                cloud_points['z'][i] = self.height
            elif (angle_value > 5*math.pi/4) and (angle_value <= 3*math.pi/2):
                angle_value -= 3*math.pi/2
                angle_value = abs(angle_value)
                cloud_points['x'][i] = -self.width*math.tan(angle_value)/2
                cloud_points['y'][i] = -self.width/2
                cloud_points['z'][i] = self.height
            elif (angle_value > 3*math.pi/2) and (angle_value <= 7*math.pi/4):
                angle_value -= 3*math.pi/2
                cloud_points['x'][i] = self.width*math.tan(angle_value)/2
                cloud_points['y'][i] = -self.width/2
                cloud_points['z'][i] = self.height
            else:
                ValueError(f'{angle_value} is not a valid value for an angle.')
            if abs(cloud_points['x'][i]) > self.width/2:
                print('something wrong')
            if abs(cloud_points['y'][i]) > self.length/2:
                print('something wrong')
        obj_cloud_points = CloudPoints(coordinates_dict=cloud_points)
        self.cloud_points = obj_cloud_points

    # Getters and setters
    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, new_width: float):
        self.positive_checker(new_width, "Width of rectangular mesh")

    @property
    def length(self):
        return self.__length

    @length.setter
    def length(self, new_length: float):
        self.positive_checker(new_length, "Length of rectangular mesh")


class CircleMesh(BaseMesh):
    def __init__(self,
                 radius: float,
                 n_points: int,
                 height: float = 1.0,
                 x_center: float = 0.0,
                 y_center: float = 0.0):
        super().__init__(n_points=n_points,
                         height=height,
                         x_center=x_center,
                         y_center=y_center)
        self.__radius = radius
        self.create_cloud_points()

    def create_cloud_points(self):
        cloud_points = {'x': {}, 'y': {}, 'z': {}}
        for i in range(self.n_points):
            cloud_points['x'][i] = self.x_center + self.radius*math.cos(2*math.pi*i/self.n_points)
            cloud_points['y'][i] = self.y_center + self.radius*math.sin(2*math.pi*i/self.n_points)
            cloud_points['z'][i] = self.height
        obj_cloud_point = CloudPoints(coordinates_dict=cloud_points)
        self.cloud_points = obj_cloud_point

    # Getters and setters
    @property
    def radius(self):
        return self.__radius

    @radius.setter
    def radius(self, new_radius: float):
        self.positive_checker(new_radius, 'radius')
        self.__radius = new_radius
        self.create_cloud_points()
