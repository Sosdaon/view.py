import turtle
'''

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
            turtle.dot(8, 'red')
            print(f'Intersection point is: {intersection_point}')
            return intersection_point

        elif x1 >= x2 and y1 >= y2:
            x_difference = x1 - x2
            y_difference = y1 - y2
            if x_difference < 18.0 and y_difference < 18.0:
                intersection_point = line1[index]
                turtle.goto(intersection_point)
                turtle.dot(8, 'red')
                print(f'Intersection point is: {intersection_point}')
                return intersection_point
            elif index < len(line1):
                index += 1
                compare_directions(line1, line2, index=index)
            else:
                print('There is no intersection point')

        elif x1 <= x2 and y1 <= y2:
            x_difference = x1 - x2
            y_difference = y1 - y2
            if x_difference < 18.0 and y_difference < 18.0:
                intersection_point = line1[index]
                turtle.goto(intersection_point)
                turtle.dot(8, 'red')
                print(f'Intersection point is: {intersection_point}')
                return intersection_point
            elif index < len(line1):
                index += 1
                compare_directions(line1, line2, index=index)
            else:
                print('There is no intersection point')

        elif x1 <= x2 and y1 >= y2:
            x_difference = x1 - x2
            y_difference = y1 - y2
            if x_difference < 18.0 and y_difference < 18.0:
                intersection_point = line1[index]
                turtle.goto(intersection_point)
                turtle.dot(8, 'red')
                print(f'Intersection point is: {intersection_point}')
                return intersection_point
            elif index < len(line1):
                index += 1
                compare_directions(line1, line2, index=index)
            else:
                print('There is no intersection point')

        elif x1 >= x2 and y1 <= y2:
            x_difference = x1 - x2
            y_difference = y1 - y2
            if x_difference < 18.0 and y_difference < 18.0:
                intersection_point = line1[index]
                turtle.goto(intersection_point)
                turtle.dot(8, 'red')
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
            print('There is something else')'''