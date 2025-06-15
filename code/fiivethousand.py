from matplotlib.textpath import TextPath
from matplotlib.font_manager import FontProperties
import matplotlib.pyplot as plt
import numpy as np

# === ฟังก์ชันช่วย ===
def cartesian_to_polar(x, y, cx=150, cy=150):
    dx = x - cx
    dy = y - cy
    r = np.sqrt(dx**2 + dy**2)
    theta = np.arctan2(dy, dx) % (2 * np.pi)
    return r, theta

def interpolate_contours(contours, target_points=5000):
    all_interp = []
    total_segments = sum(len(c) - 1 for c in contours)
    avg_points = int(target_points / total_segments)

    for contour in contours:
        new_contour = []
        for i in range(len(contour) - 1):
            p1 = contour[i]
            p2 = contour[i + 1]
            seg = np.linspace(p1, p2, avg_points, endpoint=False)
            new_contour.extend(seg)
        if not np.allclose(contour[0], contour[-1]):
            seg = np.linspace(contour[-1], contour[0], avg_points, endpoint=False)
            new_contour.extend(seg)
        all_interp.extend(new_contour)
    return np.array(all_interp)

# === ตั้งค่า ===
font_path = "C:\\Users\\User\\Base-system-frab10\\font\\BebasNeue-Regular.ttf"
word = "FIBO_G07"
size = 100

# === โหลดฟอนต์และแปลง ===
fp = FontProperties(fname=font_path)
tp = TextPath((0, 0), word, size=size, prop=fp)
contours = tp.to_polygons()

# === Center and flip contours for workspace (-300, 300) ===
bbox = tp.get_extents()
current_height = bbox.y1 - bbox.y0
desired_height = 100  # or your desired letter height
scale = desired_height / current_height

scaled_contours = [c * scale for c in contours]

x_min, x_max = bbox.x0 * scale, bbox.x1 * scale
y_min, y_max = bbox.y0 * scale, bbox.y1 * scale
center_x = (x_min + x_max) / 2
center_y = (y_min + y_max) / 2

# Flip Y and center at (0, 0)
final_contours = [
    np.array([
        [
            (x - center_x),
            (y_max - (y - y_min)) - center_y
        ]
        for x, y in c
    ])
    for c in scaled_contours
]

# === Interpolate before plot
interp_points = interpolate_contours(final_contours, target_points=3000)

# === Plot
fig, ax = plt.subplots()
for contour in final_contours:
    ax.plot(contour[:, 0], contour[:, 1], 'k-', linewidth=0.5)
ax.plot(interp_points[:, 0], interp_points[:, 1], 'ro', markersize=1)
ax.set_xlim(-300, 300)
ax.set_ylim(-300, 300)
ax.set_aspect('equal')
ax.invert_yaxis()
plt.title(f"'{word}' - Interpolated 3000 points, height=100")
plt.show()

# === Convert to polar coordinates with origin at (0, 0)
radian = []
theta = []
for x, y in interp_points:
    r = np.sqrt(x**2 + (y+140)**2)
    t = (np.arctan2((y+140), x)) % (2 * np.pi)  # Shift -90°, so 0 rad is at the bottom
    radian.append(r)
    theta.append(t)

print(f"Number of points: {len(radian)}")
# Save to file
with open("r_shift.txt", "w") as f:
    for r in radian:
        f.write(f"{r:.2f},")
with open("theta_shift.txt", "w") as f:
    for t in theta:
        f.write(f"{t:.3f},")

# Find the angle of the first point
theta_first = theta[0]
# Calculate rotation needed to move first point to π (left)
rotation = (theta_first) % (2 * np.pi)
# Rotate all theta values so first point is at the left
theta_rotated = [ (t - rotation) % (2 * np.pi) for t in theta ]

# Save to file (rotated)
with open("theta_shift_rotated.txt", "w") as f:
    for t in theta_rotated:
        f.write(f"{t:.3f},")