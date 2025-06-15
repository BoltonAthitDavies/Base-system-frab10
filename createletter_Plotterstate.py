from HersheyFonts import HersheyFonts
import matplotlib.pyplot as plt
import numpy as np

r = []
theta = []

def cartesian_to_polar(x, y, cx=150, cy=150):
    dx = x - cx
    dy = y - cy
    r = np.sqrt(dx**2 + dy**2)
    theta = np.arctan2(dx, dy)  # radians
    theta = theta % (2 * np.pi)  # Normalize to [0, 2π)
    return r, theta  # Return radians directly

def draw_line(x1, y1, x2, y2):
    plt.plot([x1, x2], [y1, y2], 'k-')
    r1, theta1 = cartesian_to_polar(x1, y1)
    r2, theta2 = cartesian_to_polar(x2, y2)
    # print(f"MOVE_TO r={r1:.2f}, θ={theta1:.3f} rad")
    # print(f"DRAW_TO r={r2:.2f}, θ={theta2:.3f} rad")
    r.append(r1)
    r.append(r2)
    theta.append(theta1)
    theta.append(theta2)

thefont = HersheyFonts()
thefont.load_default_font('rowmand')
# thefont.load_default_font()
thefont.normalize_rendering(85)  # Set height to 85 units

word = "FIBO_G07"
lines = list(thefont.lines_for_text(word))
all_x = [x for line in lines for x, _ in line]
all_y = [y for line in lines for _, y in line]
print("Lines:", len(lines))
print("X values:", len(all_x), "Y values:", len(all_y))
min_x, max_x = min(all_x), max(all_x)
min_y, max_y = min(all_y), max(all_y)
width = max_x - min_x
height = max_y - min_y
offset_x = (300 - width) / 2 - min_x
offset_y = (300 - height) / 2 - min_y

new_lines = []  

resolution = 5  # Number of points per segment (increase for higher resolution)

def interpolate_line(x1, y1, x2, y2, resolution):
    """Interpolate points between two coordinates."""
    x_values = np.linspace(x1, x2, resolution)
    y_values = np.linspace(y1, y2, resolution)
    return list(zip(x_values, y_values))

print(len(lines), "lines")
for (x1, y1), (x2, y2) in lines:
    fy1 = 300 - (y1 + offset_y)
    fy2 = 300 - (y2 + offset_y)
    points = interpolate_line(x1 + offset_x, fy1, x2 + offset_x, fy2, resolution)
    # Draw the line segment
    for i in range(len(points) - 1):
        x_start, y_start = points[i]
        x_end, y_end = points[i + 1]
        new_lines.append((x_start, y_start))
        draw_line(x_start, y_start, x_end, y_end)
        if i == len(points) - 2:  # Last point
            new_lines.append((x_end, y_end))

print("Total points:", len(new_lines))

# plt.xlim(0, 300)
# plt.ylim(0, 300)
# plt.gca().invert_yaxis()
# plt.axis('equal')
# plt.show()

plt.figure()
plt.xlim(0, 300)
plt.ylim(0, 300)
plt.gca().invert_yaxis()
plt.axis('equal')

points = new_lines
point_iter = iter(points)
scatter = None

def on_key(event):
    global scatter
    global i
    try:
        x, y = next(point_iter)
        print(f"No.{i-3}\nDrawing point at x={x:.2f}, y={y:.2f}")
        scatter = plt.scatter(x, y, color='red', s=10)
        plt.draw()
        i+=1
    except StopIteration:
        print("All points plotted.")

cid = plt.gcf().canvas.mpl_connect('key_press_event', on_key)
print("Press any key (e.g., spacebar) in the plot window to plot the next point.")
plt.show()

print(new_lines[30])

# F : 0 - 44
# I : 45 - 65
# B : 66 - 225
# O : 226 - 404
# _ : 405 - 409
# G : 410 - 609/
# 0 : 610 - 770
# 7 : 771 - 779