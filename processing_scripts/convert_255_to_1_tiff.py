import os
import numpy as np
from PIL import Image

def convert_tif_to_binary():
    source_folder = "C:/Users/lochana.marasingha/Downloads/Crop-Residue/Training/output"
    destination_folder = "C:/Users/lochana.marasingha/Downloads/Crop-Residue/Training/output/converted"

    try:
        os.makedirs(destination_folder, exist_ok=True)  # Create destination if needed

        for filename in os.listdir(source_folder):
            source_path = os.path.join(source_folder, filename)
            destination_path = os.path.join(destination_folder, filename)  # Same name

            try:
                img = Image.open(source_path)
                img_array = np.array(img)

                # Check if the image is grayscale or multi-channel (e.g., RGB)
                if len(img_array.shape) == 2:  # Grayscale
                    binary_array = np.where(img_array > 0, 1, 0)  # 255 becomes 1, others 0
                else:
                    print(f"Skipping unsupported image format: {filename}")
                    continue

                binary_image = Image.fromarray(binary_array.astype(np.uint8)) # Important: Convert to uint8
                binary_image.save(destination_path)
                print(f"Converted {filename} to binary.")

            except Exception as e:
                print(f"Error processing {filename}: {e}")

    except Exception as e:
        print(f"An error occurred: {e}")

convert_tif_to_binary()
print("TIFF conversion complete.")