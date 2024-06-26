import json
import io
from PIL import Image
from WSConnection import getImagesFromWf, upload_file



def getresult( weight_type, qrmodelver):

    validwt = ["linear", "ease in-out", "reverse in-out", "strong style transfer"]

    with open("Images/input.png", "rb") as f:
        comfyui_path_image = upload_file(f,"",True)
    
    with open("Images/input2.png", "rb") as f:
        comfyui_path_image2 = upload_file(f,"",True)


    with open("APIWorkflows/Uncrop_api.json", "r", encoding="utf-8") as f:
        workflow_data = f.read()

    workflow = json.loads(workflow_data)
    workflow["11"]["inputs"]["image"] = comfyui_path_image
    workflow["20"]["inputs"]["image"] = comfyui_path_image2
    
    if weight_type in validwt:
        workflow["24"]["inputs"]["weight_type"] = weight_type
    else:
        workflow["24"]["inputs"]["weight_type"] = "ease in-out"

    if qrmodelver == "V2":
        workflow["12"]["inputs"]["control_net_name"] = "control_v1p_sd15_qrcode_monster_v2.safetensors"
    else:
        workflow["12"]["inputs"]["control_net_name"] = "control_v1p_sd15_qrcode_monster.safetensors"
    

    images = getImagesFromWf(workflow)
    for node_id in images:
        for image_data in images[node_id]:
            imagetr = Image.open(io.BytesIO(image_data))
            return imagetr
