from HersheyFonts import HersheyFonts
import matplotlib.pyplot as plt
import numpy as np

def cartesian_to_polar(x, y, cx=150, cy=150):
    dx = x - cx
    dy = y - cy
    r = np.sqrt(dx**2 + dy**2)
    theta = np.arctan2(dx, dy)  # radians
    theta = theta % (2 * np.pi)  # Normalize to [0, 2π)
    return r, theta  # Return radians directly

def draw_line(x1, y1, x2, y2):
    # print(f"MOVE_TO x={x1:.2f}, y={y1:.3f} ")
    # print(f"DRAW_TO x={x2:.2f}, y={y2:.3f} ")
    plt.plot([x1, x2], [y1, y2], 'k-')
    r1, theta1 = cartesian_to_polar(x1, y1)
    r2, theta2 = cartesian_to_polar(x2, y2)
    print(f"MOVE_TO r={r1:.2f}, θ={theta1:.3f} rad")
    print(f"DRAW_TO r={r2:.2f}, θ={theta2:.3f} rad")

def interpolate_line(x1, y1, x2, y2, num_points):
    """Returns a list of (x, y) points from (x1, y1) to (x2, y2) with num_points in between (including endpoints)."""
    return list(zip(
        np.linspace(x1, x2, num_points),
        np.linspace(y1, y2, num_points)
    ))

thefont = HersheyFonts()
thefont.load_default_font()
thefont.load_default_font('rowmand')  #gothiceng rowmant
thefont.normalize_rendering(105)  # Set height to 85 units

word = "FIBO_G07"
lines = list(thefont.lines_for_text(word))
all_x = [x for line in lines for x, _ in line]
all_y = [y for line in lines for _, y in line]
min_x, max_x = min(all_x), max(all_x)
min_y, max_y = min(all_y), max(all_y)
width = max_x - min_x
height = max_y - min_y
offset_x = (300 - width) / 2 - min_x
offset_y = (300 - height) / 2 - min_y

theta = []
rr = []
resolution = 5  # Number of points per segment (increase for higher resolution)

for (x1, y1), (x2, y2) in lines:
    fy1 = 300 - (y1 + offset_y)
    fy2 = 300 - (y2 + offset_y)
    points = interpolate_line(x1 + offset_x, fy1, x2 + offset_x, fy2, resolution)
    for i in range(len(points) - 1):
        x_start, y_start = points[i]
        x_end, y_end = points[i + 1]
        r1, theta1 = cartesian_to_polar(x_start, y_start)
        r2, theta2 = cartesian_to_polar(x_end, y_end)
        rr.append(r1)
        rr.append(r2)
        theta.append(theta1)
        theta.append(theta2)
        draw_line(x_start, y_start, x_end, y_end)

plt.xlim(0, 300)
plt.ylim(0, 300)
plt.gca().invert_yaxis()
plt.axis('equal')
plt.show()

print(f"Number of points: {len(rr)}")

# Save to file
with open("r_last.txt", "w") as f:
    for r in rr:
        f.write(f"{r:.2f},")
with open("theta_last.txt", "w") as f:
    for t in theta:
        f.write(f"{t:.3f},")
