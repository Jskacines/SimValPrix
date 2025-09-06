from generate_race import generate_race
from drone import Drone
from animate_race import animate_race
from print_results import print_results
from control_functions.example_function import control_fun as fun1
from control_functions.bad_example_fun import control_fun as fun2

track_ids = ["Body Bend","Dynamics Drive","Powertrain Parkway","SimVal Speedway"]

drone1 = Drone(fun1)
drone2 = Drone(fun2)
for track_id in track_ids:
    ode1 = generate_race(track_id,drone1)
    print_results(ode1, track_id, "Example")
    ode2 = generate_race(track_id,drone2)
    print_results(ode2, track_id, "Bad Example")
    animate_race([ode1, ode2], ["indigo","orange"], track_id)
