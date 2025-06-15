from pygcode import Line
from HersheyFonts import HersheyFonts
import matplotlib.pyplot as plt
import numpy as np

file_path = "C:\\Users\\User\\Base-system-frab10\\code\\G7.nc"

coordinates = []

with open(file_path) as f:
    for raw_line in f:
        line = Line(raw_line)
        x = y = None
        for word in line.block.words:
            if word.letter == 'X':
                x = word.value
            if word.letter == 'Y':
                y = word.value
        if x is not None and y is not None:
            coordinates.append((x, y))

print(f"Extracted {len(coordinates)} coordinates:")
# for coord in coordinates:
#     print(coord)
print(type(coordinates[0]))  # Print first 10 coordinates for verification
print(len(coordinates))

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

for i in range(len(coordinates) - 1):
    x1, y1 = coordinates[i]
    x2, y2 = coordinates[i + 1]
    draw_line(x1, y1, x2, y2)

print(coordinates[0])
all_x = []
all_y = []
for coord in coordinates:
    all_x.append(coord[0])
    all_y.append(coord[1])
# # all_x = [x for line in coordinates for x, _ in line]
# # all_y = [y for line in coordinates for _, y in line]
# print("Lines:", len(coordinates))
# print("X values:", len(all_x), "Y values:", len(all_y))
# min_x, max_x = min(all_x), max(all_x)
# min_y, max_y = min(all_y), max(all_y)
# width = max_x - min_x
# height = max_y - min_y
offset_x = 0
offset_y = 0

new_lines = []  

resolution = 6  # Number of points per segment (increase for higher resolution)

def interpolate_line(x1, y1, x2, y2, resolution):
    """Interpolate points between two coordinates."""
    x_values = np.linspace(x1, x2, resolution)
    y_values = np.linspace(y1, y2, resolution)
    return list(zip(x_values, y_values))

print(len(coordinates), "lines")
for i in range(len(coordinates) - 1):
    x1, y1 = coordinates[i]
    x2, y2 = coordinates[i + 1]
    fy1 = 300 - (y1 + offset_y)
    fy2 = 300 - (y2 + offset_y)
    points = interpolate_line(x1 + offset_x, fy1, x2 + offset_x, fy2, resolution)
    # Draw the line segment
    for j in range(len(points) - 1):
        x_start, y_start = points[j]
        x_end, y_end = points[j + 1]
        new_lines.append((x_start, y_start))
        new_lines.append((x_end, y_end))
        plt.plot([x_start, x_end], [y_start, y_end], 'k-')

print("Total points:", len(new_lines))

plt.xlim(0, 300)
plt.ylim(0, 300)
plt.gca().invert_yaxis()
plt.axis('equal')
plt.show()

