import pyautogui
import time

def click_image(image_path):
    while True:
        try:
            # Locate the image on the screen
            location = pyautogui.locateOnScreen(image_path)
            
            if location is not None:
                # Get the center coordinates of the image
                x, y = pyautogui.center(location)
                
                # Click at the center of the image
                pyautogui.click(x, y)
                
                print("Image clicked successfully!")
            else:
                print("Image not found on the screen")
        
        except pyautogui.ImageNotFoundException:
            print("Image not found on the screen")
        
        # Adjust the sleep time as needed to control the frequency of checks
        time.sleep(1)

# Provide the path to the image you want to search for
image_path = "C:/temp/Image/image.png"

# Call the function to continuously click the image
click_image(image_path)
