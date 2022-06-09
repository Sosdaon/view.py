import turtle
from geometry.scheme.twoDimensional import Plan, Elevation
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
            turtle.dot(7, 'red')
            print(f'Intersection point is: {intersection_point}')
            return intersection_point

        elif x1 >= x2 and y1 >= y2:
            x_difference = x1 - x2
            y_difference = y1 - y2
            if x_difference < 2.0 and y_difference < 2.0:
                intersection_point = line1[index]
                turtle.goto(intersection_point)
                turtle.dot(7, 'red')
                print(f'Intersection point is: {intersection_point}')
                return intersection_point
            else:
                index += 1
                compare_directions(line1, line2, index=index)

        elif x1 <= x2 and y1 <= y2:
            x_difference = x1 - x2
            y_difference = y1 - y2
            if x_difference < 2.0 and y_difference < 2.0:
                intersection_point = line1[index]
                turtle.goto(intersection_point)
                turtle.dot(7, 'red')
                print(f'Intersection point is: {intersection_point}')
                return intersection_point
            else:
                index += 1
                compare_directions(line1, line2, index=index)

        elif x1 <= x2 and y1 >= y2:
            x_difference = x1 - x2
            y_difference = y1 - y2
            if x_difference < 2.0 and y_difference < 2.0:
                intersection_point = line1[index]
                turtle.goto(intersection_point)
                turtle.dot(7, 'red')
                print(f'Intersection point is: {intersection_point}')
                return intersection_point
            else:
                index += 1
                compare_directions(line1, line2, index=index)

        elif x1 >= x2 and y1 <= y2:
            x_difference = x1 - x2
            y_difference = y1 - y2
            if x_difference < 2.0 and y_difference < 2.0:
                intersection_point = line1[index]
                turtle.goto(intersection_point)
                turtle.dot(7, 'red')
                print(f'Intersection point is: {intersection_point}')
                return intersection_point
            else:
                index += 1
                compare_directions(line1, line2, index=index)

        else:
            print('Something wrong before recursion')


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



plan = Plan()
elevation = Elevation(plan)


plan.draw_length()
plan.draw_width()
plan.complete()

elevation.draw_height()
elevation.complete_front()
elevation.complete_side()

plan.transfer()

#______________________________________________________
#Looking for an intersection point
'''
#Set start and finish points of LINE ONE that doesn't work:
x_start1 = plan.get_point_of_view()[0]
y_start1 = plan.get_point_of_view()[1]
x_finish1 = plan.get_back_point()[0]
y_finish1 = plan.get_back_point()[1]
'''
#Set start and finish points of LINE ONE (It works with>>> lenght: 100; width: 50)
x_start1 = plan.get_point_of_view()[0]
y_start1 = plan.get_point_of_view()[1]
x_finish1 = plan.get_back_point()[0]
y_finish1 = plan.get_back_point()[1]

measured_line = []
remember_direction(x_start1, y_start1, x_finish1, y_finish1)
first_line = measured_line

'''
#Set start and finish points of LINE TWO that doesn't work:
x_start2 = float(plan.get_main_point()[0])
y_start2 = float(plan.get_main_point()[1])
x_finish2 = float(plan.get_left_point()[0])
y_finish2 = float(plan.get_left_point()[1])
'''
#Set start and finish points of LINE TWO (It works with>>> lenght: 100; width: 50)
x_start2 = float(plan.get_left_point()[0])
y_start2 = float(plan.get_left_point()[1] - plan.get_length())
x_finish2 = float(plan.get_right_point()[0] + plan.get_width())
y_finish2 = float(plan.get_right_point()[1])

measured_line = []
remember_direction(x_start2, y_start2, x_finish2, y_finish2)
second_line = measured_line

compare_directions(first_line, second_line, 0)

print(f' line 1: {first_line}')
print(f' line 2: {second_line}')
print(f'There is an access to intersection point {intersection_point}')

turtle.pencolor('black')
#______________________________________________________
#continue common drawing

plan.draw_point_of_view()
plan.draw_screen()

elevation.draw_horizon()

turtle.done()
