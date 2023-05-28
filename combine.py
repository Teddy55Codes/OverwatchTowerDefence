import os

ow_directory = "WorkshopMode"
output_file = "combined.ow"
contents = []

for root, dirs, files in os.walk(ow_directory):
    for file in files:
        if file.endswith(".ow"):
            with open(os.path.join(root, file), 'r') as f:
                contents.append(f.read() + "\n")

with open(output_file, 'w') as f:
    for content in contents:
        f.write(content)
        f.write("\n")
