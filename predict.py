import numpy as np
from cv2 import cv2
from keras import backend as K
from PIL import Image
import os
from model.VGG16 import VGG16
import ceshi1 as t1
import ceshi3 as t2

ok_output = ""
defect_A_output = ""
defect_B_output = ""


def get_classes():
    with open("./data/model/index_word.txt", "r", encoding='utf-8') as f:
        synset = [l.split(";")[1].replace("\n", "") for l in f.readlines()]
    return synset


def predict(img_path):
    global model, ok_output, defect_A_output, defect_B_output
    NCLASSES = 3
    model = VGG16(NCLASSES)
    model.load_weights(r"./logs/middle_one.h5")
    img = Image.open(img_path)
    img = img.resize((224, 224), Image.BICUBIC)
    img = np.expand_dims(np.array(img) / 255, axis=0)
    classes = get_classes()
    tp = classes[np.argmax(model.predict(img)[0])]
    # print("种类为：" + tp)
    if tp == "ok":
        img = Image.open(img_path)
        img.save(f"{ok_output}/{os.path.basename(img_path)}")
    elif tp == "defect-A":
        img = t1.defect_A(img_path)
        cv2.imwrite(f"{defect_A_output}/{os.path.basename(img_path)}", img)
    elif tp == "defect-B":
        img = t2.defect_B(img_path)
        cv2.imwrite(f"{defect_B_output}/{os.path.basename(img_path)}", img)
