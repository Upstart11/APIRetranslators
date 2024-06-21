import json
import io
from PIL import Image
from WSConnection import getImagesFromWf, upload_file



def getresult(model):

    with open("Images/input.png", "rb") as f:
        comfyui_path_image = upload_file(f,"",True)


    with open("APIWorkflows/RmBackground_api.json", "r", encoding="utf-8") as f:
        workflow_data = f.read()

    workflow = json.loads(workflow_data)
    workflow["91"]["inputs"]["image"] = comfyui_path_image
    workflow["112"]["inputs"]["model"] = model

    images = getImagesFromWf(workflow)
    for node_id in images:
        for image_data in images[node_id]:
            imagetr = Image.open(io.BytesIO(image_data))
            return imagetr
