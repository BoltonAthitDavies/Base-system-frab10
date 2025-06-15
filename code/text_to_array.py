import re

# Load the full text from the user's file
file_path = "C:\\Users\\User\\Base-system-frab10\\code\\hope.txt"
with open(file_path, "r") as file:
    content = file.read()

# Extract all numeric strings inside np.float64()
matches = re.findall(r'np\.float64\(([\d\.]+)\)', content)

# Convert to integers by truncating the decimal part
integers = [float(num) for num in matches]
print(len(integers))

theta = integers[0:len(integers)//2]
r = integers[len(integers)//2:] 

# save theta and r values to a file
output_file_path = ".\\theta_hope.txt"
with open(output_file_path, "w") as output_file:
    for t in theta:
        output_file.write(f"{t},")

output_file_path = ".\\r_hope.txt"
with open(output_file_path, "w") as output_file:
    for r_value in r:
        output_file.write(f"{r_value},")

print(2560/2)