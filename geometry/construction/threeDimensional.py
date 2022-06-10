import turtle
from geometry.scheme.twoDimensional import Plan
from geometry.scheme.twoDimensional import Elevation


class Building:
    def __init__(self, plan=Plan(), elevation=Elevation(), bottom_right_frame_point=(0.0, 0.0),
                 left_vanishing_point=(0.0, 0.0), right_vanishing_point=(0.0, 0.0), upper_nearest_corner=(0.0, 0.0),
                 bottom_nearest_corner=(0.0, 0.0), upper_left_frame_point=(0.0, 0.0), upper_right_frame_point=(0.0, 0.0),
                 upper_left_intersection_point=(0.0, 0.0), bottom_left_intersection_point=(0.0, 0.0),
                 upper_right_intersection_point=(0.0, 0.0), bottom_right_intersection_point=(0.0, 0.0)):
        self.plan = plan
        self.elevation = elevation
        self.__bottom_right_frame_point = bottom_right_frame_point
        self.__upper_left_frame_point = upper_left_frame_point
        self.__upper_right_frame_point = upper_right_frame_point
        self.__left_vanishing_point = left_vanishing_point
        self.__right_vanishing_point = right_vanishing_point
        self.__upper_nearest_corner = upper_nearest_corner
        self.__bottom_nearest_corner = bottom_nearest_corner
        self.__upper_left_intersection_point = upper_left_intersection_point
        self.__bottom_left_intersection_point = bottom_left_intersection_point
        self.__upper_right_intersection_point = upper_right_intersection_point
        self.__bottom_right_intersection_point = bottom_right_intersection_point

    def set_bottom_right_frame_point(self, bottom_right_frame_point):
        self.__bottom_right_frame_point = bottom_right_frame_point

    def set_upper_left_frame_point(self, upper_left_frame_point):
        self.__upper_left_frame_point = upper_left_frame_point

    def set_upper_right_frame_point(self, upper_right_frame_point):
        self.__upper_right_frame_point = upper_right_frame_point

    def set_left_vanishing_point(self, vanishing_point):
        self.__left_vanishing_point = vanishing_point

    def set_right_vanishing_point(self, right_vanishing_point):
        self.__right_vanishing_point = right_vanishing_point

    def set_upper_nearest_corner(self, upper_nearest_corner):
        self.__upper_nearest_corner = upper_nearest_corner

    def set_bottom_nearest_corner(self, bottom_nearest_corner):
        self.__bottom_nearest_corner = bottom_nearest_corner

    def set_upper_left_intersection_point(self, upper_left_intersection_point):
        self.__upper_left_intersection_point = upper_left_intersection_point

    def set_bottom_left_intersection_point(self, bottom_left_intersection_point):
        self.__bottom_left_intersection_point = bottom_left_intersection_point

    def set_upper_right_intersection_point(self, upper_right_intersection_point):
        self.__upper_right_intersection_point = upper_right_intersection_point

    def set_bottom_right_intersection_point(self, bottom_right_intersection_point):
        self.__bottom_right_intersection_point = bottom_right_intersection_point

    def get_bottom_left_frame_point(self):
        self.__bottom_left_frame_point = (float(self.plan.get_point_of_view()[0] + self.elevation.get_horizontal_indent()), float(self.plan.get_point_of_view()[1]))
        return self.__bottom_left_frame_point

    def get_bottom_right_frame_point(self):
        return self.__bottom_right_frame_point

    def get_upper_left_frame_point(self):
        return self.__upper_left_frame_point

    def get_upper_right_frame_point(self):
        return self.__upper_right_frame_point

    def get_left_vanishing_point(self):
        return self.__left_vanishing_point

    def get_right_vanishing_point(self):
        return self.__right_vanishing_point

    def get_upper_nearest_corner(self):
        return self.__upper_nearest_corner

    def get_bottom_nearest_corner(self):
        return self.__bottom_nearest_corner

    def get_upper_left_intersection_point(self):
        return self.__upper_left_intersection_point

    def get_bottom_left_intersection_point(self):
        return self.__bottom_left_intersection_point

    def get_upper_right_intersection_point(self):
        return self.__upper_right_intersection_point

    def get_bottom_right_intersection_point(self):
        return self.__bottom_right_intersection_point

    def draw_frame(self):
        turtle.penup()
        turtle.goto(self.get_bottom_left_frame_point())
        turtle.pencolor('gray80')
        turtle.pendown()
        turtle.forward(self.plan.get_length() * 2)
        self.set_bottom_nearest_corner(turtle.pos())
        self.plan.turn_left()
        turtle.forward(self.elevation.get_height() * 2)
        self.set_upper_nearest_corner(turtle.pos())
        self.plan.turn_right()
        turtle.forward(self.plan.get_width() * 2)
        self.set_upper_right_frame_point(turtle.pos())
        self.plan.turn_right()
        turtle.forward(self.elevation.get_height() * 2)
        self.set_bottom_right_frame_point(turtle.pos())
        self.plan.turn_right()
        turtle.forward(self.plan.get_width() * 2)
        self.plan.turn_right()
        turtle.forward(self.elevation.get_height() * 2)
        self.plan.turn_left()
        turtle.forward(self.plan.get_length() * 2)
        self.set_upper_left_frame_point(turtle.pos())
        self.plan.turn_left()
        turtle.forward(self.elevation.get_height() * 2)
        self.plan.turn_left()
        self.plan.turn_left()
        turtle.forward(self.elevation.get_horizon() * 2)
        self.set_left_vanishing_point(turtle.pos())
        self.plan.turn_right()
        turtle.forward(self.plan.get_length() * 2 + self.plan.get_width() * 2)
        self.set_right_vanishing_point(turtle.pos())

    def draw_perspective(self):
        turtle.penup()
        turtle.goto(self.get_upper_nearest_corner())
        turtle.pendown()
        turtle.goto(self.get_left_vanishing_point())
        turtle.goto(self.get_bottom_nearest_corner())
        turtle.goto(self.get_right_vanishing_point())
        turtle.goto(self.get_upper_nearest_corner())
        turtle.forward(self.plan.get_width() * 2)
        turtle.goto(self.get_left_vanishing_point())
        turtle.goto(self.get_bottom_right_frame_point())
        turtle.goto(self.get_bottom_left_frame_point())
        turtle.goto(self.get_right_vanishing_point())
        turtle.goto(self.get_upper_left_frame_point())

    def draw_left_part(self):
        turtle.penup()
        turtle.goto(self.get_upper_nearest_corner())
        turtle.pencolor('black')
        turtle.pendown()
        turtle.goto(self.get_upper_left_intersection_point())
        self.plan.turn_right()
        left_vertical_path = turtle.distance(self.get_bottom_left_intersection_point())
        turtle.forward(left_vertical_path)
        turtle.goto(self.get_bottom_nearest_corner())

    def draw_right_part(self):
        turtle.penup()
        turtle.goto(self.get_upper_nearest_corner())
        turtle.pencolor('black')
        turtle.pendown()
        turtle.goto(self.get_upper_right_intersection_point())
        right_vertical_path = turtle.distance(self.get_bottom_right_intersection_point())
        turtle.forward(right_vertical_path)
        turtle.goto(self.get_bottom_nearest_corner())
        turtle.goto(self.get_upper_nearest_corner())




