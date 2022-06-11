import turtle
from geometry.scheme.twoDimensional import Plan, Elevation
from geometry.construction.threeDimensional import Building
from geometry.memory.trajectory import Direction


plan = Plan()
elevation = Elevation(plan)
building = Building(plan, elevation)
direction = Direction()

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
building.find_upper_left_intersection_point()
building.find_bottom_left_intersection_point()
building.draw_left_part()
building.find_upper_right_intersection_point()
building.find_bottom_right_intersection_point()
building.draw_right_part()

turtle.done()
