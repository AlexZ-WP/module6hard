
import  math


class Figure:
    sides_count = 0
    filled = True
    def __init__(self, *__color, __sides):

        self.__color = __color
        self.__sides = __sides
        Figure.sides_count += self.__sides
    def get_color(self):
        return self.__color

    def __is_valid_color(self, *__color):
        for r in list(range(256)) and g in list(range(256)) and b in list(range(256)):
            if isinstance(r, int) and isinstance(g, int) and isinstance(b, int):
                return True

    def set_color(self, r, g, b):
        if Figure.__is_valid_color is True:
            self.__color = self.set_color

    def __is_valid_sides(self, _sides):
        if Figure.__is_valid_color is True and self.__sides == Figure.sides_count:
            return True
        else:
            return False

    def get_sides(self):
        pass

    def  __len__(self):
        pass

    def set_sides(self, *new_sides):

#должен принимать новые стороны, если их количество не равно sides_count, то не изменять,
# в противном случае - менять.
     pass

class Circle(Figure):
    sides_count = 1

    def __init__(self, *__color, __sides):
        super().__init__(*__color, __sides)
    __radius = sides_count/2*math.pi

    def get_square(self):
        return math.pi* self.__radius ** 2

class Triangle(Figure):
    sides_count = 3

    def __init__(self, *__color, __sides):
        super().__init__(*__color, __sides)

    def get_square(self, a, b, c):
        p = 1/2*(a+b+c)
        return (p*(p-a)*(p-b)*(p-c)) ** 0.5

class Cube(Figure):
    sides_count = 12

    def __init__(self, *__color, side):
        self.side = side
        super().__init__(*__color, self.__sides)

        self.__sides = [self.side] * Cube.sides_count

    def get_volume(self):
        return self.side^3