import cv2
import os

# set isResidue to True for residue images, False for sunlit_shaded images
def adjust_pixels(image_path, output_dir='output', isResidue = True):
    r,b, g = 0, 0, 0
    # Load the image
    image = cv2.imread(image_path, cv2.IMREAD_UNCHANGED)  # IMREAD_UNCHANGED reads the image without changing channels

    if image is None:
        print("Error: Unable to load image.")
        return
    
    
    # Change values: 255 -> 0, 0 -> 1
    if (isResidue):
        # Change all 255 values to 0, and all 0 values to 1
        image[image == 0] = 1
        image[image == 255] = 0
    else:
        # Change all 255 values to 0, and all 0 values to 1
        image[image == 0] = 1
        image[image == 255] = 2

    # Create output directory if it doesn't exist
    os.makedirs(output_dir, exist_ok=True)

    # Save the modified image
    output_path = os.path.join(output_dir, os.path.basename(image_path))
    cv2.imwrite(output_path, image)
    print(f"Modified image saved as {output_path}")

def navigate_directory(root_directory, output_dir='output', isResidue=True):
    for dirpath, dirnames, filenames in os.walk(root_directory):
        for image_file in filenames:
            if image_file.lower().endswith(".tif"):
                impath = os.path.join(dirpath, image_file)
                adjust_pixels(impath, output_dir=output_dir, isResidue=isResidue)

navigate_directory('sunlit_shaded', output_dir='output_sunlit', isResidue=False)
#adjust_rgb('IMG_0629_res_part01.tif',)