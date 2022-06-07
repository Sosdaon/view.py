import turtle
from geometry.scheme.twoDimensional import Plan, Elevation
from geometry.memory.trajectory import remember_direction, draw_remembered_line, compare_directions


plan = Plan()
elevation = Elevation(plan)


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


turtle.done()
