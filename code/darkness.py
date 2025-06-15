import numpy as np
import matplotlib.pyplot as plt 

# Read the text file and convert the comma-separated values to a list of floats
with open("D:\\Downloads\\theta_3000.txt", "r") as f:
    content = f.read().strip()
    theta = [float(x) for x in content.split(",") if x]

with open("D:\\Downloads\\r_3000.txt", "r") as f:
    content = f.read().strip()
    r = [float(x) for x in content.split(",") if x]

# polar to cartesian conversion
def polar_to_cartesian(r, theta):
    x = r * np.cos(theta)
    y = r * np.sin(theta)
    return x, y

print("First 5 r values:", r[:5])
print("First 5 theta values:", theta[:5])  

# Convert polar coordinates to cartesian coordinates
x, y = polar_to_cartesian(r, theta)

# # Plot the points
# plt.figure(figsize=(8, 8))
# plt.plot(x, y, 'o', markersize=1, color='black')
# plt.xlim(-300, 300)
# plt.ylim(-300, 300)
# plt.gca().set_aspect('equal', adjustable='box')
# plt.title("Polar to Cartesian Conversion")
# plt.xlabel("X-axis")
# plt.ylabel("Y-axis")
# plt.grid(True)
# plt.show()

# catesian to polar conversion
def cartesian_to_polar(x, y):
    r = np.sqrt((x-90)**2 + (y-0)**2)
    theta = np.arctan2((y-0), (x-90)) % (2 * np.pi)
    return r, theta

# Convert back to polar coordinates
r_converted, theta_converted = cartesian_to_polar(x, y)
# Print the first few values to verify
print("First 5 converted r values:", r_converted[:5])
print("First 5 converted theta values:", theta_converted[:5])

with open("r_shift_last.txt", "w") as f:
    for r in r_converted:
        f.write(f"{r:.2f},")
with open("theta_shift_last.txt", "w") as f:
    for t in theta_converted:
        f.write(f"{t:.3f},")

print(max(r_converted))
print(max(theta_converted))
print(len(r_converted))
print(len(theta_converted))
