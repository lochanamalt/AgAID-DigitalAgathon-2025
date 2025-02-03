import os
from PIL import Image

def convert_tiff_to_jpg():
    """
    Converts all TIFF images in a folder to JPG format.

    Args:
        source_folder: Path to the folder containing TIFF images.
        destination_folder: Path to the folder where JPG images will be saved.
    """
    source_folder = "C:/Users/lochana.marasingha/Downloads/Crop-Residue/Training/output/converted"
    destination_folder = "C:/Users/lochana.marasingha/Downloads/Crop-Residue/Training/output/converted/jpg_files"

    try:
        os.makedirs(destination_folder, exist_ok=True)  # Create destination if it doesn't exist

        for filename in os.listdir(source_folder):
            if filename.lower().endswith((".tif", ".tiff")):  # Handle both .tif and .tiff
                source_path = os.path.join(source_folder, filename)
                name_without_ext = os.path.splitext(filename)[0] # gets the name without the extension
                destination_path = os.path.join(destination_folder, f"{name_without_ext}.jpg")  # Create JPG filename

                try:
                    img = Image.open(source_path)
                    img.save(destination_path, "JPEG")  # Save as JPEG
                    print(f"Converted {filename} to {name_without_ext}.jpg")

                except Exception as e:
                    print(f"Error processing {filename}: {e}")

    except Exception as e:
        print(f"An error occurred: {e}")

convert_tiff_to_jpg()
print("TIFF to JPG conversion complete.")