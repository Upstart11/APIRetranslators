import json
import io
import os
from PIL import Image
from WSConnection import getImagesFromWf, upload_file



def getresult( left, top, right, bottom, positiveprompt, negativeprompt):

    imgdir = "APIRetranslators/Images"
    wfdir = "APIRetranslators/APIWorkflows"
    

    if os.path.exists("Images"):
        imgdir = "Images"
        wfdir = "APIWorkflows"
        

    with open(os.path.join(imgdir, "input.png"), "rb") as f:
        comfyui_path_image = upload_file(f,"",True)


    with open(os.path.join(wfdir, "Uncrop_api.json"), "r", encoding="utf-8") as f:
        workflow_data = f.read()

    workflow = json.loads(workflow_data)
    workflow["12"]["inputs"]["image"] = comfyui_path_image
    workflow["10"]["inputs"]["left"] = left
    workflow["10"]["inputs"]["top"] = top
    workflow["10"]["inputs"]["right"] = right
    workflow["10"]["inputs"]["bottom"] = bottom
    workflow["6"]["inputs"]["text"] = positiveprompt
    workflow["7"]["inputs"]["text"] = negativeprompt

    images = getImagesFromWf(workflow)
    for node_id in images:
        for image_data in images[node_id]:
            imagetr = Image.open(io.BytesIO(image_data))
            return imagetr
