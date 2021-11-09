import cv2
import numpy as np
from localization import PlateLocation

def get_area_img(origin_img, location):
    """
    Clip the origin img and get the plate
    """
    pos_x,pos_y = location[0]
    width,height = location[1]
    angle = location[2]
    
    # rotation
    RotationMatrix = cv2.getRotationMatrix2D((pos_x,pos_y),angle,1)
    img_rotated = cv2.warpAffine(origin_img, RotationMatrix, (origin_img.shape[1], origin_img.shape[0]))

    # clip
    img_cliped = img_rotated[int(pos_y-height/2):int(pos_y+height/2), int(pos_x-width/2):int(pos_x+width/2)]

    # shear
    ShearMatrix = np.array([[1, 0.5,0],
                            [0, 1,0]])
    img_sheared = cv2.warpAffine(img_cliped, ShearMatrix, (img_cliped.shape[1]+100, img_cliped.shape[0]+10))

    return img_sheared


if __name__=='__main__':
    img_path = "test2.jpg"
    img = cv2.imread(img_path)
    location = PlateLocation(img)
    get_area_img(origin_img=img, location=location)
    