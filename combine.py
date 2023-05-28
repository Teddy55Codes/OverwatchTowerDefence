import os

ow_directory = "WorkshopMode"
output_file = "combined.ow"
header_files = ["Settings.ow", "Variables.ow"]
contents = []

def check_excluded(filename):
    for file in header_files:
        if filename == file:
            return True
    return False

for file in header_files:
    with open(os.path.join(ow_directory, file), 'r') as f:
                contents.append(f.read() + "\n")


for root, dirs, files in os.walk(ow_directory):
    for file in files:
        if file.endswith(".ow") and not check_excluded(file):
            with open(os.path.join(root, file), 'r') as f:
                contents.append(f.read() + "\n")

with open(output_file, 'w') as f:
    for content in contents:
        f.write(content)
        f.write("\n")
