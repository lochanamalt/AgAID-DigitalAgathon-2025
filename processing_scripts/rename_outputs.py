import os
import shutil
import glob


import os
import shutil
import glob

def rename_and_copy_images():  # No source_folder argument
    """
    Organizes .jpg and .tif files from subfolders of a *hardcoded* source folder.
    """

    # Hardcoded paths (REPLACE THESE WITH YOUR ACTUAL PATHS)
    source_folder = "C:/Users/lochana.marasingha/Downloads/Crop-Residue/images_512/label/residue_background/Ritzville3-WheatFallow1pass1m20220329"
    training_outputs = "C:/Users/lochana.marasingha/Downloads/Crop-Residue/Training/output"


    try:
        os.makedirs(training_outputs, exist_ok=True)

        for root, _, files in os.walk(source_folder):
            for file in files:

                if file.lower().endswith(".tif") or file.lower().endswith(".tiff"):
                    source_path = os.path.join(root, file)

                    # Get filename without extension
                    filename_without_ext = os.path.splitext(file)[0]  # Split at the last .

                    # Remove "res" (case-insensitive)
                    new_filename_base = filename_without_ext.replace("res_", "", 1).replace("RES", "",
                                                                                           1)  # replace only the first occurence

                    # Create new filename for .tif
                    new_filename = f"{new_filename_base}.jpg"  # Add .tif extension
                    print(new_filename)
                    destination_path = os.path.join(training_outputs, new_filename)
                    shutil.copy2(source_path, destination_path)
                    print(f"Copied and renamed {file} to {new_filename}")

    except Exception as e:
        print(f"An error occurred: {e}")


# Call the function (no arguments needed now)
rename_and_copy_images()

print("Image organization complete.")