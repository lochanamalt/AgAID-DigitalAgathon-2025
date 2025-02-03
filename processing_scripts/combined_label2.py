import os
import re
import numpy as np
import tifffile as tiff

# Define folder paths
output_residue = "output_residue"
output_sunlit = "output_sunlit"
output_combined = "output_combined"

# Ensure the output directory exists
if not os.path.exists(output_combined):
    os.makedirs(output_combined)


# Function to extract the unique identifier from filenames
def extract_identifier(filename):
    match = re.match(r"(.{8}).*(.{6}\.tif)$", filename)
    return match.group(1) + match.group(2) if match else None


# Get all files in the residue and sunlit folders
residue_files = {extract_identifier(f): f for f in os.listdir(output_residue) if f.endswith(".tif")}
sunlit_files = {extract_identifier(f): f for f in os.listdir(output_sunlit) if f.endswith(".tif")}

# Find matching files
matching_keys = set(residue_files.keys()) & set(sunlit_files.keys())

for key in matching_keys:
    res_file = os.path.join(output_residue, residue_files[key])
    sun_file = os.path.join(output_sunlit, sunlit_files[key])

    # Read images
    res_img = tiff.imread(res_file).astype(np.float32)
    sun_img = tiff.imread(sun_file).astype(np.float32)

    # Perform the calculation
    new_img = 2 * res_img + sun_img

    # Save the new image with the same naming convention
    output_filename = residue_files[key]  # Maintain synchronization
    output_path = os.path.join(output_combined, output_filename)
    tiff.imwrite(output_path, new_img.astype(np.uint16))

    print(f"Saved combined image: {output_path}")

print("Processing complete.")
