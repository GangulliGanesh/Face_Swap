

def swap_warp(filename1,filename2):
    import sys
    from line_fun_1 import line,read_and_crop1,read_and_crop,intersection,af_transform
    import cv2
    import os
    from remove_bg import remove_bg2

    ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
    target1 = os.path.join(ROOT_DIR, 'static/')

    x=read_and_crop(filename1)
    y=read_and_crop1(filename2)

    k=""
    k=remove_bg2(y)

    d=cv2.imread(x,cv2.IMREAD_UNCHANGED)
    a,b,c=d.shape
    a1=0
    b1=0
    a1=a+60
    b1=b+60
    print(d.shape)

    p=cv2.imread(k,cv2.IMREAD_UNCHANGED)
    print(p.shape)
    p_r=cv2.resize(p,(b1,a1))
    print(p_r.shape)

    cv2.imwrite(target1+'Resized.png',p_r)  ##Transparent bg

    koo=""
    koo=af_transform(filename1)

    print(koo)
    print('Mask_pass_success')
    return koo
