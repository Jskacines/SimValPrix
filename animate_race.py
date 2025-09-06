import svgpathtools as svg
import numpy as np
import matplotlib.pyplot as plt
from shapely.geometry import LineString
from matplotlib.animation import FuncAnimation

def animate_race(odes, colors, track_id):
    path = svg.svg2paths("tracks/" + track_id + ".svg")[0][0]
    offset = 5
    ode_sols = [ode.sol for ode in odes]

    t_ends = [max(ode.t) for ode in odes]
    t_end = max(t_ends)

    linspace = np.linspace(0,0.95,1000)
    xs = np.array([np.real(path.point(t)) for t in linspace])
    ys = np.array([np.imag(path.point(t)) for t in linspace])

    curve = LineString(zip(xs,ys))
    left = curve.parallel_offset(offset,'left')
    right = curve.parallel_offset(offset,'right')

    fig, ax = plt.subplots()
    line_inner = ax.plot(xs,ys,c="darkgray")
    line_outer1 = ax.plot(*left.xy,c="k")
    line_outer2 = ax.plot(*right.xy,c="k")

    ax.set_xlim(0,100)
    ax.set_ylim(0,100)

    duration = 3
    fps = 30
    frame_count = duration*fps
    t_array = np.linspace(0,t_end,frame_count)



    def quiver_fun(ode_sol,t):
        x = ode_sol(t)[0]
        y = ode_sol(t)[1]
        u = np.cos(ode_sol(t)[2])
        v = np.sin(ode_sol(t)[2])
        return x,y,u,v
    quivers = []
    scatters = []
    for i, _ in enumerate(ode_sols):
        x0, y0, u0, v0 = quiver_fun(ode_sols[i], 0)
        quivers.append(ax.quiver(x0,y0,u0,v0, color=colors[i]))
        scatters.append(ax.scatter(x0,y0, color=colors[i]))

    def update(frame):
        t = t_array[frame]
        for i, _ in enumerate(ode_sols):
            t_clip = np.clip(t,0,t_ends[i])
            x,y,u,v = quiver_fun(ode_sols[i],t_clip)
            quivers[i].set_offsets([x,y])
            scatters[i].set_offsets([x,y])
            quivers[i].set_UVC(u,v)
        ax.set_title(f"{track_id}, T = {t/100:.2f}")

    
    ani = FuncAnimation(fig, update, frames=frame_count, interval=1000/fps)
    ani.save(filename="gifs/" + track_id + ".gif", writer="pillow")