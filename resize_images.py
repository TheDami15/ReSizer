import os

def resize_images_in_folder(folder_path, target_width, target_height):
    """
    Basic script: Only validates the folder path. Does not resize images yet.
    """
    # Check if the folder exists
    if not os.path.isdir(folder_path):
        print("Folder path is invalid.")
        return

    print(f"Folder '{folder_path}' exists. Ready to process images.")

if __name__ == "__main__":
    # User input for folder path
    folder_path = input("Enter the folder path containing images: ")

    # Hardcoded dimensions
    target_width = 100
    target_height = 100

    # Call the resize function
    resize_images_in_folder(folder_path, target_width, target_height)
