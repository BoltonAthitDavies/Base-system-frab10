import re

# Load the full text from the user's file
file_path = "C:\\Users\\User\\Base-system-frab10\\code\\coordinate.txt"
with open(file_path, "r") as file:
    content = file.read()

# Extract all numeric strings inside np.float64()
matches = re.findall(r'np\.float64\(([\d\.]+)\)', content)

# Convert to integers by truncating the decimal part
integers = [float(num) for num in matches]
print(len(integers))

theta = integers[0:len(integers)//2]
r = integers[len(integers)//2:] 

import matplotlib.pyplot as plt
import matplotlib.pyplot as plt
import numpy as np

# # If theta is in degrees, convert to radians
# theta_rad = np.deg2rad(theta)

# plt.figure(figsize=(6, 6))
# ax = plt.subplot(111, polar=True)
# ax.scatter(theta_rad, r, s=10, color='blue')
# ax.set_title("Polar Scatter Plot")
# plt.show()

#I have polar coordinatees in list form, I want to plot them using matplotlib
# Plot as a scatter plot
plt.figure(figsize=(8, 4))
plt.scatter(range(len(r)), r, s=10, color='blue')
plt.title("Scatter Plot of Data")
plt.xlabel("Index")
plt.ylabel("Value")
plt.grid(True)
plt.show()
# [0,73, 104, 360, 648, 656, 976, 1232]
count = 0
list = []
for i in range(len(theta)-1):
    if abs(theta[i+1] - theta[i]) > 28:
        count += 1
        list.append(i)
print(f"Number of values greater than 20: {count}")
print(f"Indices of values greater than 20: {list}")