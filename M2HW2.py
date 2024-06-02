class Figure:
    unit = 'cm'

    def __init__(self):
        pass

    def calculate_area(self):
        raise NotImplementedError("Subclasses should implement this method")

    def info(self):
        raise NotImplementedError("Subclasses should implement this method")


class Square(Figure):
    def __init__(self, side_length):
        super().__init__()
        self.__side_length = side_length

    def calculate_area(self):
        return self.__side_length ** 2

    def info(self):
        area = self.calculate_area()
        print(f"Square side length: {self.__side_length}{Figure.unit}, area: {area}{Figure.unit}")


class Rectangle(Figure):
    def __init__(self, length, width):
        super().__init__()
        self.__length = length
        self.__width = width

    def calculate_area(self):
        return self.__length * self.__width

    def info(self):
        area = self.calculate_area()
        print(
            f"Rectangle length: {self.__length}{Figure.unit}, width: {self.__width}{Figure.unit}, area: {area}{Figure.unit}")


if __name__ == "__main__":
    shapes = [
        Square(15),
        Square(17),
        Rectangle(10, 15),
        Rectangle(25, 40),
        Rectangle(40, 70)
    ]

    for shape in shapes:
        shape.info()
