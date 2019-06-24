import cv2
import locator
import os
import numpy as np
import csv
import imutils
import dlib
from imutils import face_utils
detector = dlib.get_frontal_face_detector()
predictor = dlib.shape_predictor('./shape_predictor_68_face_landmarks.dat')


def line(p1, p2):
    A = (p1[1] - p2[1])
    B = (p2[0] - p1[0])
    C = (p1[0]*p2[1] - p2[0]*p1[1])
    return A, B, -C

def intersection(L1, L2):
    D  = L1[0] * L2[1] - L1[1] * L2[0]
    Dx = L1[2] * L2[1] - L1[1] * L2[2]
    Dy = L1[0] * L2[2] - L1[2] * L2[0]
    if D != 0:
        x = Dx / D
        y = Dy / D
        return x,y
    else:
        return False


def read_and_crop(filenam):
    APP_ROOT = os.path.dirname(os.path.abspath(__file__))

    target = os.path.join(APP_ROOT, 'static/')
    txt=target+'0.txt'

    img2=cv2.imread(filenam)
    q,u,d=img2.shape
    shape= locator.face_points(img2)
    ###########################################
    ##Dlib Keypoints

    gray = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)
    rects = detector(gray, 1)
    for (i, rect) in enumerate(rects):
        shape1 = predictor(gray, rect)
        shape1 = face_utils.shape_to_np(shape1)

    ####################################################
    b = shape1
    b=np.resize(b,(14,2))

    bb1=b
    bb1=bb1.astype(int)

    bb1[0][0]=b[3][0]
    bb1[0][1]=b[3][1]

    bb1[1][0]=b[3][0]
    bb1[1][1]=b[3][1]

    bb1[2][0]=b[3][0]
    bb1[2][1]=b[3][1]

    bb2=np.zeros((6,2))

    bb2[0][0]=u
    bb2[0][1]=b[13][1]

    bb2[1][0]=u
    bb2[1][1]=q

    bb2[2][0]=b[13][0]
    bb2[2][1]=q

    bb2[3][0]=b[3][0]
    bb2[3][1]=q

    bb2[4][0]=0
    bb2[4][1]=q

    bb2[5][0]=0
    bb2[5][1]=b[3][1]

    bb2=np.concatenate((bb1,bb2), axis=0)
    bb2=bb2.astype(int)
    with open(txt,"w") as f:
        f.write("\n".join(" ".join(map(str, x)) for x in (bb2)))
    j=[]

    with open(txt,'r') as file:
        reader = csv.reader(file,delimiter=' ')
        for a,b in reader:
            j.append(a)
            j.append(b)
            kl=np.asarray(j)

    klm=int(len(kl)/2)
    data=np.reshape(kl,(klm,2))
    contours=np.int32(data)

    img2 = cv2.cvtColor(img2,cv2.COLOR_RGB2RGBA)
    img2=cv2.fillPoly(img2, pts =[contours], color=(0,0,0,0))

    x1,y1,w1,h1=cv2.boundingRect(shape)
    L1=line([x1,y1],[x1+w1,y1+h1])
    L2=line([x1+w1,y1],[x1,y1+h1])
    R=intersection(L1,L2)
    j1,k1=R
    print('Intersection:',j1,k1)
    wi1=j1-x1
    he1=k1-y1
    wi2=wi1+(0.45*wi1)
    wi3=2*wi2
    he2=he1+(0.95*he1)
    he3=2*he2
    x2=j1-wi2
    y2=k1-he2
    if x2<0:
        x2=0
    if y2<0:
        y2=0
    wi4=int(wi3)
    he4=int(he3)
    crop = img2[int(y2):int(y2+he4), int(x2):int(x2+wi4)]

    to_crop = os.path.join(target, 'crop1.png')
    cv2.imwrite(to_crop,crop)

    print('Cropped image1 saved')
    print(to_crop)

    return to_crop

def read_and_crop1(filenam):
    APP_ROOT = os.path.dirname(os.path.abspath(__file__))

    target = os.path.join(APP_ROOT, 'static/')
    txt=target+'1.txt'
    BLUE = [255,0,0]
    img2=cv2.imread(filenam)
    img2=cv2.copyMakeBorder( img2,125,0, 0, 0,cv2.BORDER_CONSTANT,value=BLUE)
    q,u,d=img2.shape
    shape= locator.face_points(img2)
    ###########################################
    #Dlib Keypoints

    gray = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)
    rects = detector(gray, 1)
    # loop over the face detections
    for (i, rect) in enumerate(rects):
        shape1 = predictor(gray, rect)
        shape1 = face_utils.shape_to_np(shape1)

        ####################################################
    b = shape1
    b=np.resize(b,(14,2))

    bb1=b
    bb1=bb1.astype(int)

    bb1[0][0]=b[3][0]
    bb1[0][1]=b[3][1]

    bb1[1][0]=b[3][0]
    bb1[1][1]=b[3][1]

    bb1[2][0]=b[3][0]
    bb1[2][1]=b[3][1]

    bb2=np.zeros((6,2))

    bb2[0][0]=u
    bb2[0][1]=b[13][1]

    bb2[1][0]=u
    bb2[1][1]=q

    bb2[2][0]=b[13][0]
    bb2[2][1]=q

    bb2[3][0]=b[3][0]
    bb2[3][1]=q

    bb2[4][0]=0
    bb2[4][1]=q

    bb2[5][0]=0
    bb2[5][1]=b[3][1]

    bb2=np.concatenate((bb1,bb2), axis=0)
    bb2=bb2.astype(int)
    with open(txt,"w") as f:
        f.write("\n".join(" ".join(map(str, x)) for x in (bb2)))
    j=[]

    with open(txt,'r') as file:
        reader = csv.reader(file,delimiter=' ')
        for a,b in reader:
            j.append(a)
            j.append(b)
            kl=np.asarray(j)

    klm=int(len(kl)/2)
    data=np.reshape(kl,(klm,2))
    ############################################################################################################################
    contours=np.int32(data)
    img2 = cv2.cvtColor(img2,cv2.COLOR_RGB2RGBA)
    img2=cv2.fillPoly(img2, pts =[contours], color=(0,0,0,0))

##################################################################################################################################
    x1,y1,w1,h1=cv2.boundingRect(shape)
    L1=line([x1,y1],[x1+w1,y1+h1])
    L2=line([x1+w1,y1],[x1,y1+h1])
    R=intersection(L1,L2)
    j1,k1=R
    wi1=j1-x1
    he1=k1-y1
    wi2=wi1+(0.45*wi1)
    wi3=2*wi2
    he2=he1+(0.95*he1)
    he3=2*he2
    x2=j1-wi2
    y2=k1-he2
    if x2<0:
        x2=0
    if y2<0:
        y2=0
    wi4=int(wi3)
    he4=int(he3)
    crop = img2[int(y2):int(y2+he4), int(x2):int(x2+wi4)]
    to_crop = os.path.join(target, 'crop2.png')
    cv2.imwrite(to_crop,crop)

    print('Cropped image2 saved')
    print(to_crop)

    return to_crop

def af_transform(filenam):
    ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
    target1 = os.path.join(ROOT_DIR, 'static/')
    n=target1+'Resized.png'
    print('From_transform')

    g=cv2.imread(n,-1)
    print('Patch_image:',g.shape)


    img2=cv2.imread(filenam)

    print('Base_image:',img2.shape)

    shape= locator.face_points(img2)
    x1,y1,w1,h1=cv2.boundingRect(shape)
    L1=line([x1,y1],[x1+w1,y1+h1])
    L2=line([x1+w1,y1],[x1,y1+h1])
    R=intersection(L1,L2)
    j1,k1=R
    wi1=j1-x1
    he1=k1-y1
    wi2=wi1+(0.45*wi1)
    wi3=2*wi2
    he2=he1+(0.95*he1)
    he3=2*he2

    x2=j1-wi2
    y2=k1-he2
    if x2<0:
        x2=0
    if y2<0:
        y2=0
    wi4=int(wi3)
    he4=int(he3)
    y21=y2+(0.03*y2)

    alpha_s = g[:, :, 3] / 255.0
    alpha_l = 1.0 - alpha_s

    for c in range(0, 3):
        img2[int(y21-30):int(y21+he4+30), int(x2-30):int(x2+wi4+30), c] = (alpha_s * g[:, :, c] + alpha_l * img2[int(y21-30):int(y21+he4+30), int(x2-30):int(x2+wi4+30), c])

    lay =""
    lay = os.path.join(target1, 'ok.png')
    cv2.imwrite(lay,img2)
    lay1='static/ok.png'
    print('Final save')

    return lay1
