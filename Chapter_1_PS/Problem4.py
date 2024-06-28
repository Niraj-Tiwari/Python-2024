import os

def print_directory_contents(path):
    # List all files and directories in the specified path
    # use the os module to list the directory content
    contents = os.listdir(path)
    print(f"Contents of directory '{path}':")
    for item in contents:
        print(item)

# Specify the path to the directory
# Select the directory whose content you want to list
directory_path = "/Web_Development_CWH_2023"

# Print the contents of the directory
print_directory_contents(directory_path)
