import turtle
from geometry.scheme.twoDimensional import Plan, Elevation
from geometry.construction.threeDimensional import Building
intersection_point = 'empty'


def compare_directions(line1, line2, index):
    if len(line1) > 1 and len(line2) > 1 and index < len(line1):
        global intersection_point
        turtle.penup()

        line1_x_y = line1[index]
        x1 = line1_x_y[0]
        y1 = line1_x_y[1]

        line2_x_y = line2[index]
        x2 = line2_x_y[0]
        y2 = line2_x_y[1]

        if x1 == x2 and y1 == y2:
            intersection_point = line1[index]
            turtle.goto(intersection_point)
            turtle.dot(4, 'red')
            print(f'Intersection point is: {intersection_point}')
            return intersection_point

        elif x1 >= x2 and y1 >= y2:
            x_difference = x1 - x2
            y_difference = y1 - y2
            if x_difference < 3.0 and y_difference < 3.0:
                intersection_point = line1[index]
                turtle.goto(intersection_point)
                turtle.dot(4, 'red')
                print(f'Intersection point is: {intersection_point}')
                return intersection_point
            elif index < len(line1):
                index += 1
                compare_directions(line1, line2, index=index)
            else:
                print('There is no intersection point')

        elif x1 <= x2 and y1 <= y2:
            x_difference = x2 - x1
            y_difference = y2 - y1
            if x_difference < 3.0 and y_difference < 3.0:
                intersection_point = line1[index]
                turtle.goto(intersection_point)
                turtle.dot(4, 'red')
                print(f'Intersection point is: {intersection_point}')
                return intersection_point
            elif index < len(line1):
                index += 1
                compare_directions(line1, line2, index=index)
            else:
                print('There is no intersection point')

        elif x1 <= x2 and y1 >= y2:
            x_difference = x2 - x1
            y_difference = y1 - y2
            if x_difference < 3.0 and y_difference < 3.0:
                intersection_point = line1[index]
                turtle.goto(intersection_point)
                turtle.dot(4, 'red')
                print(f'Intersection point is: {intersection_point}')
                return intersection_point
            elif index < len(line1):
                index += 1
                compare_directions(line1, line2, index=index)
            else:
                print('There is no intersection point')

        elif x1 >= x2 and y1 <= y2:
            x_difference = x1 - x2
            y_difference = y2 - y1
            if x_difference < 3.0 and y_difference < 3.0:
                intersection_point = line1[index]
                turtle.goto(intersection_point)
                turtle.dot(4, 'red')
                print(f'Intersection point is: {intersection_point}')
                return intersection_point
            elif index < len(line1):
                index += 1
                compare_directions(line1, line2, index=index)
            else:
                print('There is no intersection point')

        else:
            print('Something wrong before recursion')
    else:
        print('There are no lines or line to compare or intersection point was not found or start index not 0')


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
        turtle.pencolor('cyan')
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




plan = Plan()
elevation = Elevation(plan)
building = Building(plan, elevation)

plan.draw_length()
plan.draw_width()
plan.complete()

elevation.draw_height()
elevation.complete_front()
elevation.complete_side()

plan.transfer()

plan.draw_point_of_view()
plan.draw_screen()

elevation.draw_horizon()

building.draw_frame()
building.draw_perspective()


# _________________________________
# Looking for an upper_left_intersection_point

# Set start and finish points of LINE ONE
x_start1 = building.get_upper_nearest_corner()[0]
y_start1 = building.get_upper_nearest_corner()[1]
x_finish1 = building.get_left_vanishing_point()[0]
y_finish1 = building.get_left_vanishing_point()[1]

measured_line = []
remember_direction(x_start1, y_start1, x_finish1, y_finish1)
first_line = measured_line

# Set start and finish points of LINE TWO
x_start2 = building.get_upper_left_frame_point()[0]
y_start2 = building.get_upper_left_frame_point()[1]
x_finish2 = building.get_right_vanishing_point()[0]
y_finish2 = building.get_right_vanishing_point()[1]

measured_line = []
remember_direction(x_start2, y_start2, x_finish2, y_finish2)
second_line = measured_line

compare_directions(first_line, second_line, 0)

print(f' line 1: {first_line}')
print(f' line 2: {second_line}')
print(f'There is an access to intersection point {intersection_point}')

building.set_upper_left_intersection_point(intersection_point)
# _______________________
# Continue common drawing


# _________________________________
# Looking for an upper_right_intersection_point

# Set start and finish points of LINE ONE
x_start1 = building.get_bottom_nearest_corner()[0]
y_start1 = building.get_bottom_nearest_corner()[1]
x_finish1 = building.get_left_vanishing_point()[0]
y_finish1 = building.get_left_vanishing_point()[1]

measured_line = []
remember_direction(x_start1, y_start1, x_finish1, y_finish1)
first_line = measured_line

# Set start and finish points of LINE TWO
x_start2 = building.get_bottom_left_frame_point()[0]
y_start2 = building.get_bottom_left_frame_point()[1]
x_finish2 = building.get_right_vanishing_point()[0]
y_finish2 = building.get_right_vanishing_point()[1]

measured_line = []
remember_direction(x_start2, y_start2, x_finish2, y_finish2)
second_line = measured_line

compare_directions(first_line, second_line, 0)

print(f' line 1: {first_line}')
print(f' line 2: {second_line}')
print(f'There is an access to intersection point {intersection_point}')

building.set_bottom_left_intersection_point(intersection_point)
# _______________________
# Continue common drawing



building.draw_left_part()


# _________________________________
# Looking for an upper_right_intersection_point

# Set start and finish points of LINE ONE
x_start1 = building.get_upper_nearest_corner()[0]
y_start1 = building.get_upper_nearest_corner()[1]
x_finish1 = building.get_right_vanishing_point()[0]
y_finish1 = building.get_right_vanishing_point()[1]

measured_line = []
remember_direction(x_start1, y_start1, x_finish1, y_finish1)
first_line = measured_line

# Set start and finish points of LINE TWO
x_start2 = building.get_upper_right_frame_point()[0]
y_start2 = building.get_upper_right_frame_point()[1]
x_finish2 = building.get_left_vanishing_point()[0]
y_finish2 = building.get_left_vanishing_point()[1]

measured_line = []
remember_direction(x_start2, y_start2, x_finish2, y_finish2)
second_line = measured_line

compare_directions(first_line, second_line, 0)

print(f' line 1: {first_line}')
print(f' line 2: {second_line}')
print(f'There is an access to intersection point {intersection_point}')

building.set_upper_right_intersection_point(intersection_point)
# _______________________
# Continue common drawing


# _________________________________
# Looking for an bottom_right_intersection_point

# Set start and finish points of LINE ONE
x_start1 = building.get_bottom_nearest_corner()[0]
y_start1 = building.get_bottom_nearest_corner()[1]
x_finish1 = building.get_right_vanishing_point()[0]
y_finish1 = building.get_right_vanishing_point()[1]

measured_line = []
remember_direction(x_start1, y_start1, x_finish1, y_finish1)
first_line = measured_line

# Set start and finish points of LINE TWO
x_start2 = building.get_bottom_right_frame_point()[0]
y_start2 = building.get_bottom_right_frame_point()[1]
x_finish2 = building.get_left_vanishing_point()[0]
y_finish2 = building.get_left_vanishing_point()[1]

measured_line = []
remember_direction(x_start2, y_start2, x_finish2, y_finish2)
second_line = measured_line

compare_directions(first_line, second_line, 0)

print(f' line 1: {first_line}')
print(f' line 2: {second_line}')
print(f'There is an access to intersection point {intersection_point}')

building.set_bottom_right_intersection_point(intersection_point)
# _______________________
# Continue common drawing

building.draw_right_part()

turtle.done()
