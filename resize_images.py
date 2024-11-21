from PIL import Image
import os

def resizeimagesinfolder(folderpath, target_width, target_height):
    """
    Resizes images and saves them in a 'thumbnails' folder.
    """
    if not os.path.isdir(folder_path):
        print("Folder path is invalid.")
        return

    # Create a 'thumbnails' folder
    thumbnails_folder = os.path.join(folder_path, "thumbnails")
    os.makedirs(thumbnails_folder, exist_ok=True)

    # Process each image file in the folder
    for filename in os.listdir(folder_path):
        if filename.lower().endswith(('.png', '.jpg', '.jpeg')):
            image_path = os.path.join(folder_path, filename)
            with Image.open(image_path) as img:
                resized_image = img.resize((target_width, target_height))
                save_path = os.path.join(thumbnails_folder, filename)
                resized_image.save(save_path)
                print(f"Thumbnail saved as {save_path}")

if __name == "__main":
    folder_path = input("Enter the folder path containing images: ")
    target_width = 100
    target_height = 100
    resize_images_in_folder(folder_path, target_width, target_height)
