import os
import numpy as np
import cv2
from PIL import Image, ImageDraw, ImageFont

# Define output folder
output_folder = "output_annotated"
os.makedirs(output_folder, exist_ok=True)

def compute_percentages(predictedImagePath):
    image = Image.open(predictedImagePath).convert('L')  # Convert to grayscale
    image_array = np.array(image)

    # Count pixel values
    residueSunlitPixels = np.sum(image_array == 1)
    residueShadedPixels = np.sum(image_array == 2)
    backgroundSunlitPixels = np.sum(image_array == 3)
    backgroundShadedPixels = np.sum(image_array == 4)

    totalPixels = image_array.size

    # Compute percentages
    residueSunlitPercentage = (residueSunlitPixels / totalPixels) * 100
    residueShadedPercentage = (residueShadedPixels / totalPixels) * 100
    backgroundSunlitPercentage = (backgroundSunlitPixels / totalPixels) * 100
    backgroundShadedPercentage = (backgroundShadedPixels / totalPixels) * 100
    residuePercentage = ((residueSunlitPixels + residueShadedPixels) / totalPixels) * 100

    return image_array, residueSunlitPercentage, residueShadedPercentage, backgroundSunlitPercentage, backgroundShadedPercentage, residuePercentage

def colorize_and_annotate(image_array, filename, percentages):
    # New Color Mapping
    color_map = {
        1: (0, 128, 0),      # Green for Residue Sunlit
        2: (144, 238, 144),  # Light Green for Residue Shaded
        3: (255, 255, 224),  # Light Yellow for Background Sunlit
        4: (128, 128, 128)   # Grey for Background Shaded
    }

    # Convert grayscale image to color (RGB)
    colored_image = np.zeros((*image_array.shape, 3), dtype=np.uint8)
    for value, color in color_map.items():
        colored_image[image_array == value] = color

    # Convert to PIL for annotation
    pil_image = Image.fromarray(colored_image)

    # Create a new blank image for the legend (same width, 100px height)
    legend_height = 120
    legend_image = Image.new('RGB', (pil_image.width, legend_height), (255, 255, 255))
    draw = ImageDraw.Draw(legend_image)

    # Define font
    try:
        font = ImageFont.truetype("arial.ttf", 11)  # Use Arial if available
    except IOError:
        font = ImageFont.load_default()  # Use default if Arial not found

    # Text legend
    text_lines = [
        f"File: {filename}",
        f"Residue Sunlit (Green): {percentages[0]:.2f}%",
        f"Residue Shaded (Light Green): {percentages[1]:.2f}%",
        f"Background Sunlit (Light Yellow): {percentages[2]:.2f}%",
        f"Background Shaded (Grey): {percentages[3]:.2f}%",
        f"Total Residue: {percentages[4]:.2f}%"
    ]

    # Position to draw text (centered)
    text_x = 20
    text_y = 10

    for i, line in enumerate(text_lines):
        draw.text((text_x, text_y + i * 20), line, fill="black", font=font)

    # Combine legend and image (stack legend on top)
    final_image = Image.new('RGB', (pil_image.width, pil_image.height + legend_height))
    final_image.paste(legend_image, (0, 0))  # Paste legend at top
    final_image.paste(pil_image, (0, legend_height))  # Paste image below legend

    # Save output image
    save_path = os.path.join(output_folder, filename.replace('.tif', '.jpg'))
    final_image.save(save_path, "JPEG")
    print(f"Saved: {save_path}")

def process_files_in_directory(directory_path):
    for filename in os.listdir(directory_path):
        if filename.endswith('.tif'):
            file_path = os.path.join(directory_path, filename)
            image_array, *percentages = compute_percentages(file_path)
            colorize_and_annotate(image_array, filename, percentages)

# Run the function
process_files_in_directory('output_combined')