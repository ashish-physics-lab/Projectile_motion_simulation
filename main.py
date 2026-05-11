import math
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# --------------------------------
# INPUT VALUES
# --------------------------------

speed = 20
angle = 45
g = 9.8

# --------------------------------
# ANGLE TO RADIANS
# --------------------------------

radian = math.radians(angle)

# --------------------------------
# VELOCITY COMPONENTS
# --------------------------------

vx = speed * math.cos(radian)
vy = speed * math.sin(radian)

# --------------------------------
# TIME VALUES
# --------------------------------

time = []
t = 0

while t <= 5:
    time.append(t)
    t += 0.05

# --------------------------------
# POSITION LISTS
# --------------------------------

x = []
y = []

# --------------------------------
# CALCULATE POSITIONS
# --------------------------------

for t in time:

    x_pos = vx * t

    y_pos = (vy * t) - (0.5 * g * t**2)

    if y_pos < 0:
        break

    x.append(x_pos)
    y.append(y_pos)

# --------------------------------
# CREATE FIGURE
# --------------------------------

fig, ax = plt.subplots()

ax.set_xlim(0, max(x) + 5)
ax.set_ylim(0, max(y) + 5)

ax.set_xlabel("Distance")
ax.set_ylabel("Height")

ax.set_title("Projectile Motion Animation")

ax.grid(True)

# --------------------------------
# BALL OBJECT
# --------------------------------

ball, = ax.plot([], [], 'ro', markersize=10)

# --------------------------------
# INITIAL FUNCTION
# --------------------------------

def init():
    ball.set_data([], [])
    return ball,

# --------------------------------
# ANIMATION FUNCTION
# --------------------------------

def update(frame):

    ball.set_data([x[frame]], [y[frame]])

    return ball,

# --------------------------------
# CREATE ANIMATION
# --------------------------------

ani = FuncAnimation(
    fig,
    update,
    frames=len(x),
    init_func=init,
    blit=True,
    interval=30
)

# --------------------------------
# SHOW ANIMATION
# --------------------------------

plt.show()
