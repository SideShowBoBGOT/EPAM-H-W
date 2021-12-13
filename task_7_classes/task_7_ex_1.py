class Rectangle:
    """
    Class that represents an instance of rectangle
    """
    __side_a = 4.0
    __side_b = 3.0

    def __init__(self, side_a: int, side_b: int):
        """
        Initializes sides of rectangle
        :param a: side_a
        :param b: side_b
        """
        if side_a <= 0 or side_b <= 0:
            raise ValueError
        self.__side_a = side_a
        self.__side_b = side_b

    def get_side_a(self) -> float:
        """
        Property returning side_a
        :return: self.side_a
        """
        return self.__side_a

    def get_side_b(self) -> float:
        """
        Property returning side_b
        :return: self.side_b
        """
        return self.__side_b

    def area(self) -> float:
        """
        Method returning area of rectangle
        :return: product of side_a and side_b
        """
        return self.__side_a * self.__side_b

    def perimeter(self) -> float:
        """
        Method returning perimeter of rectangle
        :return: sum of doubled sides of rectangle
        """
        return 2 * (self.__side_a + self.__side_b)

    def is_square(self) -> bool:
        """
        Method determining whether rectangle is square
        :return: True if sides are equal else False
        """
        if self.__side_a == self.__side_b:
            return True
        else:
            return False

    def replace_sides(self) -> None:
        """
        Method switching sides of rectangle
        :return: None
        """
        c = self.__side_a
        self.__side_a = self.__side_b
        self.__side_b = c


class ArrayRectangles:
    __rectangle_array = []

    def __init__(self, *args, n=0):
        """
        Initializes an instance of array of rectangles.
        :param args: list of rectangles or any amount of rectangles
        :param n: the length of the array
        !!!Note: if n > number of args then None elements will be added to array to achieve desired length!!!
        """
        self.__rectangle_array = [*args]
        if len(self.__rectangle_array) < n:
            for i in range(n - len(self.__rectangle_array)):
                self.__rectangle_array.append(None)

    def add_rectangle(self, rectangle: Rectangle) -> bool:
        """
        Method adding rectangle to the end of the array.
        :param rectangle: an instance of class Rectangle
        :return: if there is en empty( None ) elements then element is added and method return True else False
        """
        for index, el in enumerate(self.__rectangle_array):
            if el == None:
                self.__rectangle_array.insert(index, rectangle)
                self.__rectangle_array.pop(-1)
                return True
        return False

    def number_max_area(self) -> int:
        """
        Method returning order number (index) of the first rectangle with the maximum area value
        :return: index
        """
        max_area = 0
        for el in self.__rectangle_array:
            if el is not None:
                if max_area < el.area():
                    max_area = el.area()
        for index, el in enumerate(self.__rectangle_array):
            if el is not None:
                if max_area == el.area():
                    return index

    def number_min_perimeter(self) -> int:
        """
        Method returning order number (index) of the first rectangle with the minimum area value
        :return: index
        """
        min_perimeter = self.__rectangle_array[0].perimeter()
        for el in self.__rectangle_array:
            if el is not None:
                if min_perimeter > el.perimeter():
                    min_perimeter = el.perimeter()
        for index, el in enumerate(self.__rectangle_array):
            if el is not None:
                if min_perimeter == el.perimeter():
                    return index

    def number_square(self) -> int:
        """
        Method returning the number of squares in the array of rectangles
        :return: count
        """
        count = 0
        for el in self.__rectangle_array:
            if el is not None:
                if el.is_square():
                    count += 1
        return count

a = Rectangle(4, 5)
b = Rectangle(7, 6)
c = Rectangle(3, 7)
d = Rectangle(10 ,1)
e = Rectangle(1, 1)
l = ArrayRectangles(a, b, c, n=5)
l.add_rectangle(d)
l.add_rectangle(e)
print(l.number_min_perimeter())
