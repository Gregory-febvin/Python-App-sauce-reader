import os
from PIL import ImageTk, Image

def filename_image_sort(filename):
    if filename == "cover.jpg":
        return -1
    return int(filename.split('.')[0])

def get_list_image_sauce(sauce):
    list_image = os.listdir("Image/" + sauce)
    sorted_list_image = sorted(list_image, key=filename_image_sort)

    for list_image in sorted_list_image:
        print(list_image)
    
    cover_path = os.path.join("Image", sauce, "cover.jpg")
    cover = Image.open(cover_path)
    cover.show()

while True:
    list_sauce = os.listdir("Image/")
    for i, sauce in enumerate(list_sauce):
        print(f"Sauce N°{i + 1} : " + sauce)
    
    print("Choose your sauce.")
    choice = int(input('Enter your choice:'))

    if 1 <= choice <= len(list_sauce):
        sauce_number = list_sauce[choice - 1]
        get_list_image_sauce(sauce_number)
        input("\n -------------------------------------------------------- \n")
        
    else:
        print("Invalid choice. Please choose a valid sauce number.")

