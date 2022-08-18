import time, pyautogui as pygui
from PIL import ImageGrab, ImageOps
import numpy as np

def pixsum(pt):

    box=tuple(pt)
    box_whole=(box[0]+5,box[1]-12,box[0]+105,box[1]+2)
    box1=(0,0,50,14)
    box2=(50,0,100,14)

    img = ImageGrab.grab(box_whole)
    img1=img.crop((box1))
    img2=img.crop((box2))

    gs1,gs2 = ImageOps.grayscale(img1), ImageOps.grayscale(img2)

    if (np.array(gs1.getcolors())).sum() != (np.array(gs2.getcolors())).sum():
        return False

    return True

def main():
    coord=input('Enter new coordinates for dinosour origin point? enter "y" if yes, else just hit enter: ')
    if coord.lower()=='y':
        pt=[int(i) for i in input('Enter new coordinates separated by a comma: ').split(',')]
        print(f'Got it, new dino coords are: {pt}')
    else:
        print('Using default coordinares (440,222) for dino origin point')
        pt=[440,222]
    print('Please switch to chrome, the script will begin in 3 seconds')
    for i in range(3):
        print(i+1)
        time.sleep(1)
    pygui.press(' ')
    count=0

    #MAIN LOOP
    tot=0
    while 1:
        if not pixsum(pt):
            pygui.press(' ')
            time.sleep(0.15)
            pygui.press('Down')
            count+=1
            if count>5:
                if tot>30:
                    continue
                count=0
                pt[0]+=2
                tot+=2

if __name__=='__main__':
    main()
