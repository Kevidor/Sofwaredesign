#%% Example 1
robot_name : str = "Dave"
robot_type : str = "KVN"
distance_to_wall_cm : int = 10
speed_cm_s : float = 0.5

time_to_hit_the_wall_s : float = distance_to_wall_cm / speed_cm_s

print(robot_name + " is a " + robot_type + " and will hit the wall in " + str(time_to_hit_the_wall_s) + " sec")

#%% Example 2
robot_name = "Nr5"
robot_type = "LegoRobot"
distance_to_wall_cm = 10
speed_cm_s = 0.5

time_to_hit_the_wall_s = distance_to_wall_cm / speed_cm_s

close_to_wall = distance_to_wall_cm < 5

print(F"{robot_name} is a {robot_type} and will hit the wall in {time_to_hit_the_wall_s} s")
print("{} is a {} is close to the wall:  {}".format(robot_name, robot_type, close_to_wall))


# %% Example 3
robot_name = "Nr5"
robot_type = "LegoRobot"
distance_to_wall_cm = 29
speed_cm_s = 0.5
emergency_stop = False

time_to_hit_the_wall_s = distance_to_wall_cm / speed_cm_s

close_to_wall = distance_to_wall_cm > 5

if distance_to_wall_cm < 5:
    emergency_stop = True
    print("Critical! Did a emergency stop!")
elif distance_to_wall_cm < 10:
    print("Warning! Is coming close to the wall!")
else:
    print("Current distance to wall is {} cm".format(distance_to_wall_cm))

# %%
