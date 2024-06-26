import json
import io
import os
from PIL import Image
from WSConnection import getImagesFromWf, upload_file



def getresult( upscaleby, positiveprompt, negativeprompt):

    imgdir = "APIRetranslators/Images"
    wfdir = "APIRetranslators/APIWorkflows"
    

    if os.path.exists("Images"):
        imgdir = "Images"
        wfdir = "APIWorkflows"
        

    with open(os.path.join(imgdir, "input.png"), "rb") as f:
        comfyui_path_image = upload_file(f,"",True)


    with open(os.path.join(wfdir, "Upscale_api.json"), "r", encoding="utf-8") as f:
        workflow_data = f.read()

    workflow = json.loads(workflow_data)
    workflow["2"]["inputs"]["image"] = comfyui_path_image
    workflow["24"]["inputs"]["scale_by"] = upscaleby
    workflow["9"]["inputs"]["positive_prompt"] = positiveprompt
    workflow["9"]["inputs"]["negative_prompt"] = negativeprompt

    images = getImagesFromWf(workflow)
    for node_id in images:
        for image_data in images[node_id]:
            imagetr = Image.open(io.BytesIO(image_data))
            return imagetr
