import cv2
import numpy as np
import os
import pyautogui
import webbrowser

def Record(data) :
    webbrowser.open(f"file:{os.getcwd()}/swintro/index.html?ip={data['query']}&country={data['country']}&region={data['regionName']}&city={data['city']}&zip={data['zip']}&lat={data['lat']}&lon={data['lon']}")  # Open browser

    output = "final.mp4"
    img = pyautogui.screenshot()
    img = cv2.cvtColor(np.array(img), cv2.COLOR_RGB2BGR)
    #get info from img
    height, width, channels = img.shape
    # Define the codec and create VideoWriter object
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')
    out = cv2.VideoWriter(output, fourcc, 20.0, (width, height))

    for i in range(190): #95
        try:
            img = pyautogui.screenshot()
            image = cv2.cvtColor(np.array(img), cv2.COLOR_RGB2BGR)
            out.write(image)
            StopIteration(0.5)
        except KeyboardInterrupt:
            break

    print("finished recording!")
    out.release()
    cv2.destroyAllWindows()