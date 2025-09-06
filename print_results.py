def print_results(ode, track_id, title):
    if len(ode.t_events[0] != 0):
        print(f"Result of {title} on {track_id}: Success with Time = {ode.t_events[0][0]/100}")
    elif len(ode.t_events[1] != 0):
        print(f"Result of {title} on {track_id}: Failure at Time = {ode.t_events[1][0]/100}")
    else:
        print(f"Result of {title} on {track_id}: Error")

