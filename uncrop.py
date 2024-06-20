import json
from WSConnection import getImagesFromWf, upload_file



def getresult( left, top, right, bottom):

    with open("input.png", "rb") as f:
        comfyui_path_image = upload_file(f,"",True)


    with open("APIWorkflows/UncropFT_api.json", "r", encoding="utf-8") as f:
        workflow_data = f.read()

    workflow = json.loads(workflow_data)
    workflow["12"]["inputs"]["image"] = comfyui_path_image
    workflow["10"]["inputs"]["left"] = left
    workflow["10"]["inputs"]["top"] = top
    workflow["10"]["inputs"]["right"] = right
    workflow["10"]["inputs"]["bottom"] = bottom

    images = getImagesFromWf(workflow)
    return images[0]
