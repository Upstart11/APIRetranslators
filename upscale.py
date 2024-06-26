import json
import io
from PIL import Image
from WSConnection import getImagesFromWf, upload_file



def getresult( upscaleby, positiveprompt, negativeprompt):

    with open("Images/input.png", "rb") as f:
        comfyui_path_image = upload_file(f,"",True)


    with open("APIWorkflows/Uncrop_api.json", "r", encoding="utf-8") as f:
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
