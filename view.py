import turtle


class Plan:
    def __init__(self, length=0, width=0):
        self.__LEFT_EDGE = -300
        self.__length = length
        self.__width = width

    def set_length(self, length):
        self.__length = length

    def set_width(self, width):
        self.__width = width

    def get_length(self):
        return self.__length

    def get_width(self):
        return self.__width

    def get_left_edge(self):
        return self.__LEFT_EDGE


class Elevation:
    def __init__(self, height=0):
        self.__CORNER = 90
        self.__height = height

    def set_height(self, height):
        self.__height = height

    def get_height(self):
        return self.__height


class Building(Plan, Elevation):
    def __init__(self, length=0, width=0, height=0, horizon=0, main_point=(0.0, 0.0), back_point=(0.0, 0.0),
                 left_point=(0.0, 0.0), right_point=(0.0, 0.0)):
        self.__CORNER = 90
        self.__ELEVATION_INDENT = 40
        self.__VERTICAL_INDENT = 180
        self.__horizon = horizon
        self.__main_point = main_point
        self.__back_point = back_point
        self.__left_point = left_point
        self.__right_point = right_point

        Plan.__init__(self, length, width)
        Elevation.__init__(self, height)

    def set_horizon(self, horizon):
        self.__horizon = horizon

    def set_main_point(self, main_point):
        self.__main_point = main_point

    def set_back_point(self, back_point):
        self.__back_point = back_point

    def set_left_point(self, left_point):
        self.__left_point = left_point

    def set_right_point(self, right_point):
        self.__right_point = right_point

    def get_horizon(self):
        return self.__horizon

    def get_corner(self):
        return self.__CORNER

    def get_horizontal_indent(self):
        return self.__ELEVATION_INDENT

    def get_vertical_indent(self):
        return self.__VERTICAL_INDENT

    def get_point_of_view(self):
        self.__point_of_view = (
            float(self.get_right_point()[0] + self.get_width()), float(self.get_left_point()[1] - self.get_length()))
        return self.__point_of_view

    def get_main_point(self):
        return self.__main_point

    def get_back_point(self):
        return self.__back_point

    def get_left_point(self):
        return self.__left_point

    def get_right_point(self):
        return self.__right_point

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

    def complete_plan(self):
        turtle.forward(self.get_length())
        self.turn_left()
        turtle.forward(self.get_width())
        self.turn_left()
        self.turn_left()

    def draw_height(self):
        turtle.penup()
        turtle.goto(0, 200)
        self.set_height(int(input('Enter the height: ')))
        turtle.pendown()
        turtle.forward(self.get_height())
        self.turn_left()

    def complete_front_elevation(self):
        turtle.forward(self.get_length())
        self.turn_left()
        turtle.forward(self.get_height())
        self.turn_left()
        turtle.forward(self.get_length())

    def complete_side_elevation(self):
        turtle.penup()
        turtle.forward(self.get_horizontal_indent())
        turtle.pendown()
        turtle.forward(self.get_width())
        self.turn_left()
        turtle.forward(self.get_height())
        self.turn_left()
        turtle.forward(self.get_width())
        self.turn_left()
        turtle.forward(self.get_height())

    def transfer_plan(self):
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
        turtle.done()


'''

#house = Building()

#house.draw_length()
#house.draw_width()
#house.complete_plan()
#house.draw_height()
#house.complete_front_elevation()
#house.complete_side_elevation()
#house.transfer_plan()
#house.draw_point_of_view()
#house.draw_screen()

'''


def avoid_division_by_zero(number):
    int(number)
    if number == 0:
        number += 1
        float(number)
        return number


def draw_remembered_line(line):
    if len(line) > 1:
        line_length = len(line)
        percent = 0

        turtle.penup()
        turtle.goto(line[percent])

        while turtle.pos() != line[line_length - 1]:
            turtle.pendown()
            turtle.pencolor('blue')
            turtle.goto(line[percent])
            percent += 1
    else:
        print('There is no coordinates to draw line')


def compare_directions(line_one, line_two):
    if len(line_one) > 1 and len(line_two) > 1:
        turtle.penup()
        line_length = len(line_one)
        index = 0

        while line_one[index] != line_two[index]:
            if index < line_length - 1:
                index += 1
                if line_one[index] == line_two[index]:
                    intersection_point = line_one[index]
                    turtle.goto(intersection_point)
                    turtle.dot(7, 'red')
                    print(f'Intersection point is: {intersection_point}')
                    turtle.hideturtle()
            else:
                return print('There is no intersection point')

    else:
        print('There is no line or there are no lines to compare')


def remember_direction(x_start, y_start, x_finish, y_finish):
    x_decrement = False
    y_decrement = False

    if x_start > x_finish:
        x_decrement = True
    if y_start > y_finish:
        y_decrement = True

    x_points = [x_start, x_finish]
    y_points = [y_start, y_finish]

    x_points.sort(reverse=True)
    y_points.sort(reverse=True)

    x_distance = x_points[0] - x_points[1]
    y_distance = y_points[0] - y_points[1]

    x_percent = x_distance / 100.0
    y_percent = y_distance / 100.0

    turtle.penup()
    turtle.goto(x_start, y_start)

    x_step = x_start
    y_step = y_start

    while turtle.pos()[0] != x_finish and turtle.pos()[1] != y_finish:
        turtle.pendown()
        turtle.pencolor('yellow')
        turtle.goto(x_step, y_step)
        if x_decrement == True and y_decrement == False:
            x_step = x_step - x_percent
            y_step = y_step + y_percent

            current_pose = turtle.pos()

            rounded_x = int(current_pose[0])
            rounded_y = int(current_pose[1])

            current_x = float(rounded_x)
            current_y = float(rounded_y)

            x_y_tuple = (current_x, current_y)
            measured_line.append(x_y_tuple)
            if turtle.pos()[0] < x_finish or turtle.pos()[1] > y_finish:
                break

        elif x_decrement == False and y_decrement == True:
            x_step = x_step + x_percent
            y_step = y_step - y_percent

            current_pose = turtle.pos()

            rounded_x = int(current_pose[0])
            rounded_y = int(current_pose[1])

            current_x = float(rounded_x)
            current_y = float(rounded_y)

            x_y_tuple = (current_x, current_y)
            measured_line.append(x_y_tuple)
            if turtle.pos()[0] > x_finish or turtle.pos()[1] < y_finish:
                break

        elif x_decrement == True and y_decrement == True:
            x_step = x_step - x_percent
            y_step = y_step - y_percent

            current_pose = turtle.pos()

            rounded_x = int(current_pose[0])
            rounded_y = int(current_pose[1])

            current_x = float(rounded_x)
            current_y = float(rounded_y)

            x_y_tuple = (current_x, current_y)
            measured_line.append(x_y_tuple)
            if turtle.pos()[0] < x_finish or turtle.pos()[1] < y_finish:
                break

        elif x_decrement == False and y_decrement == False:
            x_step = x_step + x_percent
            y_step = y_step + y_percent

            current_pose = turtle.pos()

            rounded_x = int(current_pose[0])
            rounded_y = int(current_pose[1])

            current_x = float(rounded_x)
            current_y = float(rounded_y)

            x_y_tuple = (current_x, current_y)
            measured_line.append(x_y_tuple)
            if turtle.pos()[0] > x_finish or turtle.pos()[1] > y_finish:
                break

        else:
            print('There is something else')


'''
______________________________________________________________________________________________________________________
Coordinates of the first parallel positive line(-34.0, -20.0, 58.0, 74.0)
Coordinates of the second parallel positive line(-7.0, -32.0, 85.0, 62.0)
______________________________________________________________________________________________________________________
Coordinates of the first parallel negative line(58.0, 74.0, -34.0, -20.0)
Coordinates of the second parallel negative line(85.0, 62.0, -7.0, -32.0)
______________________________________________________________________________________________________________________
Coordinates of the first intersects positive line    1 (34.0, 20.0, 58.0, 74.0)
                                                     2 (10.0, 12.0, 60.0, 75.0)
Coordinates of the second intersects positive line   1 (7.0, 32.0, 85.0, 62.0)
                                                     2 (20.0, 2.0, 50.0, 84.0)
______________________________________________________________________________________________________________________
Coordinates of the first intersects negative line    1 (60.0, 75.0, 10.0, 12.0)
Coordinates of the second intersects negative line   1 (50.0, 84.0, 20.0, 2.0)
______________________________________________________________________________________________________________________
Coordinates of the first intersects negative line that isn't recognized as intersecting one (-34.0, 20.0, -58.0, 74.0)
Coordinates of the second intersects negative line that isn't recognized as intersecting one (7.0, 32.0, -85.0, 62.0)
______________________________________________________________________________________________________________________
'''

measured_line = []
remember_direction(34.0, 20.0, 58.0, 74.0)
first_line = measured_line

measured_line = []
remember_direction(7.0, 32.0, 85.0, 62.0)
second_line = measured_line

draw_remembered_line(first_line)
draw_remembered_line(second_line)

compare_directions(first_line, second_line)

print(f' line 1: {first_line}')
print(f' line 2: {second_line}')

turtle.done()
