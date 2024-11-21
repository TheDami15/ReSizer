from PIL import Image
import os

def resizeimagesinfolder(folderpath, target_width, target_height):
    """
    Resizes images in the specified folder.
    """
    if not os.path.isdir(folder_path):
        print("Folder path is invalid.")
        return

    # Process each image file in the folder
    for filename in os.listdir(folder_path):
        if filename.lower().endswith(('.png', '.jpg', '.jpeg')):
            image_path = os.path.join(folder_path, filename)
            with Image.open(image_path) as img:
                resized_image = img.resize((target_width, target_height))
                resized_image.save(image_path)  # Overwrites original file
                print(f"Resized {filename}")

if __name == "__main":
    folder_path = input("Enter the folder path containing images: ")
    target_width = 100
    target_height = 100
    resize_images_in_folder(folder_path, target_width, target_height)
