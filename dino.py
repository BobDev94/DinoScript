import time, pyautogui as pygui
from PIL import ImageGrab, ImageOps
import numpy as np

def pixsum(pt):

    box=tuple(pt)
    box1=(box[0]+30,box[1],box[0]+80,box[1]+2)
    box2=(box[0]+80,box[1],box[0]+130,box[1]+2)
    box3=(box[0]+80,box[1]-12,box[0]+130,box[1]-10)

    img1,img2,img3 = ImageGrab.grab(box1),ImageGrab.grab(box2),ImageGrab.grab(box3)

    gs1,gs2,gs3 = ImageOps.grayscale(img1), ImageOps.grayscale(img2), ImageOps.grayscale(img3)

    if (np.array(gs1.getcolors())).sum()!=(np.array(gs2.getcolors())).sum() or (np.array(gs1.getcolors())).sum()!=(np.array(gs3.getcolors())).sum():
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
    while 1:
        if not pixsum(pt):
            pygui.press(' ')
            time.sleep(0.15)
            pygui.press('Down')
            count+=1
            print(count)
            if count>100:
                count=0
                pt[0]+=1

if __name__=='__main__':
    main()
