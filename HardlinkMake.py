import os
import argparse

# Set up the argument parser
parser = argparse.ArgumentParser()
parser.add_argument('root_folder', help='The path to the root folder')
args = parser.parse_args()

# Get the root folder from the command line arguments
root_folder = args.root_folder

# Set the path to the destination folder where the hardlinks will be created
destination_folder = os.path.join(os.path.dirname(root_folder), 'destination')
if not os.path.isdir(destination_folder):
    os.mkdir(destination_folder)
# Set the maximum file size in bytes
max_size = 8 * 1024 * 1024

# Iterate through all the files in the root folder and its subfolders
for root, dirs, files in os.walk(root_folder):
    for file in files:
        # Get the full path of the file
        file_path = os.path.join(root, file)

        # Check the file size
        file_size = os.stat(file_path).st_size
        if file_size <= max_size:
            # Check if the file is an image or a video
            if file.endswith(('.jpg', '.jpeg', '.png', '.gif', '.bmp', '.tiff', '.webp', '.mp4', '.avi', '.wmv', '.mkv', '.mov')):
                print(f"Found {file}, hardlinking...")
                # Create a hardlink to the file in the destination folder
                destination_path = os.path.join(destination_folder, file)
                os.link(file_path, destination_path)