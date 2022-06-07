import turtle

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

'''