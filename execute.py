import cv2 as cv
import numpy as np
import os,sys
import matplotlib.pyplot as plt
import openai
import pandas as pd
import requests
import uuid
import time
import json
from glob import glob
import datetime
import json

import crop
import ocr
import gpt_inference


def execute():

    img_crop = crop.ImageCrop()
    img_ocr = ocr.OCR()
    gpt_infer = gpt_inference.gpt()

    img_path = img_crop.crop_image()
    text = img_ocr.ocr(img_path)
    answer = gpt_infer.classify_text(text)

    
    # print(json.loads(answer))

    return answer

execute()




