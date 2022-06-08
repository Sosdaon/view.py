import turtle
from geometry.memory.trajectory import remember_direction, draw_remembered_line, compare_directions


class Plan:
    def __init__(self, length=0, width=0, main_point=(0.0, 0.0), left_point=(0.0, 0.0), right_point=(0.0, 0.0),
                 back_point=(0.0, 0.0), measured_line_one=(), measured_line_two=(), intersection_point=(0.0, 0.0)):
        self.__CORNER = 90
        self.__LEFT_EDGE = -300
        self.__VERTICAL_INDENT = 180
        self.__length = length
        self.__width = width
        self.__main_point = main_point
        self.__left_point = left_point
        self.__right_point = right_point
        self.__back_point = back_point
        self.__measured_line_one = measured_line_one
        self.__measured_line_two = measured_line_two
        self.__intersection_point = intersection_point

    def set_length(self, length):
        self.__length = length

    def set_width(self, width):
        self.__width = width

    def set_main_point(self, main_point):
        self.__main_point = main_point

    def set_left_point(self, left_point):
        self.__left_point = left_point

    def set_right_point(self, right_point):
        self.__right_point = right_point

    def set_back_point(self, back_point):
        self.__back_point = back_point

    def set_measured_line_one(self, measured_line_one):
        self.__measured_line_one = measured_line_one

    def set_measured_line_two(self, measured_line_two):
        self.__measured_line_two = measured_line_two

    def set_intersection_point(self, intersection_point):
        self.__intersection_point = intersection_point

    def get_length(self):
        return self.__length

    def get_corner(self):
        return self.__CORNER

    def get_width(self):
        return self.__width

    def get_left_edge(self):
        return self.__LEFT_EDGE

    def get_vertical_indent(self):
        return self.__VERTICAL_INDENT

    def get_main_point(self):
        return self.__main_point

    def get_left_point(self):
        return self.__left_point

    def get_right_point(self):
        return self.__right_point

    def get_back_point(self):
        return self.__back_point

    def get_measured_line_one(self):
        return self.__measured_line_one

    def get_measured_line_two(self):
        return self.__measured_line_two

    def get_intersection_point(self):
        return self.__intersection_point

    def get_point_of_view(self):
        self.__point_of_view = (
            float(self.get_right_point()[0] + self.get_width()), float(self.get_left_point()[1] - self.get_length()))
        return self.__point_of_view

    def draw_length(self):
        turtle.penup()
        turtle.goto(self.get_left_edge(), 200)
        self.set_length(int(input('Enter the length: ')))
        turtle.pendown()
        turtle.forward(self.get_length())
        self.turn_left()

    def draw_width(self):
        self.set_width(int(input('Enter the width: ')))
        turtle.forward(self.get_width())
        self.turn_left()

    def turn_left(self):
        turtle.left(self.get_corner())

    def turn_right(self):
        turtle.right(self.get_corner())

    def complete(self):
        turtle.forward(self.get_length())
        self.turn_left()
        turtle.forward(self.get_width())
        self.turn_left()
        self.turn_left()

    def transfer(self):
        turtle.penup()
        turtle.goto(self.get_left_edge(), self.get_vertical_indent())
        turtle.pendown()
        self.set_back_point(turtle.pos())
        turtle.forward(self.get_width())
        self.set_left_point(turtle.pos())
        self.turn_left()
        turtle.forward(self.get_length())
        self.set_main_point(turtle.pos())
        self.turn_left()
        turtle.forward(self.get_width())
        self.set_right_point(turtle.pos())
        self.turn_left()
        turtle.forward(self.get_length())

    def draw_point_of_view(self):
        turtle.penup()
        turtle.goto(self.get_point_of_view())
        turtle.pendown()
        turtle.goto(self.get_main_point())
        turtle.penup()
        turtle.goto(self.get_point_of_view())
        turtle.pendown()
        turtle.goto(self.get_back_point())
        turtle.penup()
        turtle.goto(self.get_point_of_view())
        turtle.pendown()
        turtle.goto(self.get_left_point())
        turtle.penup()
        turtle.goto(self.get_point_of_view())
        turtle.pendown()
        turtle.goto(self.get_right_point())

    def draw_screen(self):
        turtle.penup()
        turtle.goto(float(self.get_left_point()[0]), float(self.get_left_point()[1] - self.get_length()))
        turtle.pendown()
        turtle.goto(float(self.get_right_point()[0] + self.get_width()), float(self.get_right_point()[1]))
        turtle.penup()
        self.turn_right()


class Elevation:
    def __init__(self, plan=Plan(), height=0, horizon=0):
        self.plan = plan
        self.__HORIZONTAL_INDENT = 40
        self.__height = height
        self.__horizon = horizon

    def set_height(self, height):
        self.__height = height

    def set_horizon(self, horizon):
        self.__horizon = horizon

    def get_horizontal_indent(self):
        return self.__HORIZONTAL_INDENT

    def get_height(self):
        return self.__height

    def get_horizon(self):
        return self.__horizon

    def draw_height(self):
        turtle.penup()
        turtle.goto(0, 200)
        self.set_height(int(input('Enter the height: ')))
        turtle.pendown()
        turtle.forward(self.get_height())
        self.plan.turn_left()

    def draw_horizon(self):
        turtle.penup()
        turtle.goto(0 - self.plan.get_length(), 200)
        self.set_horizon(int(input('Enter the height of the horizon: ')))
        turtle.pendown()
        turtle.forward(self.get_horizon())
        self.plan.turn_right()
        turtle.pencolor('gray80')
        turtle.forward(self.plan.get_length())
        turtle.pencolor('black')
        turtle.forward(self.get_horizontal_indent())
        turtle.pencolor('gray80')
        turtle.forward(self.plan.get_width())
        turtle.pencolor('black')

    def complete_front(self):
        turtle.forward(self.plan.get_length())
        self.plan.turn_left()
        turtle.forward(self.get_height())
        self.plan.turn_left()
        turtle.forward(self.plan.get_length())

    def complete_side(self):
        turtle.penup()
        turtle.forward(self.get_horizontal_indent())
        turtle.pendown()
        turtle.forward(self.plan.get_width())
        self.plan.turn_left()
        turtle.forward(self.get_height())
        self.plan.turn_left()
        turtle.forward(self.plan.get_width())
        self.plan.turn_left()
        turtle.forward(self.get_height())
