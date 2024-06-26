from fastapi import FastAPI, File, UploadFile, Form
from fastapi.responses import FileResponse
import uncrop
import rmBackground
import upscale
import qrcode
import uvicorn
import io
import os

from PIL import Image
from pathlib import Path

app = FastAPI()

current_directory = os.path.dirname(os.path.abspath(__file__))

# Get the parent directory
parent_directory = os.path.basename(os.path.dirname(current_directory))

# Check if the parent directory is named 'APIRetranslators'
if parent_directory == "APIRetranslators":
    INPUT_FILE = "Images/input.png"
    INPUT_PATH = Path("Images/input.png")    

    INPUT2_FILE = "Images/input2.png"
    INPUT2_PATH = Path("Images/input2.png")

    OUTPUT_FILE = "Images/output.png"
    OUTPUT_PATH = Path("Images/output.png")
else:
    INPUT_FILE = "APIRetranslators/Images/input.png"
    INPUT_PATH = Path("APIRetranslators/Images/input.png")    

    INPUT2_FILE = "APIRetranslators/Images/input2.png"
    INPUT2_PATH = Path("APIRetranslators/Images/input2.png")

    OUTPUT_FILE = "APIRetranslators/Images/output.png"
    OUTPUT_PATH = Path("APIRetranslators/Images/output.png")



app = FastAPI()

    

@app.post("/uncrop/")
async def uncroppost(
    image: UploadFile = File(...), 
    left: int = Form(...),
    top: int = Form(...),
    right: int = Form(...),
    bottom: int = Form(...),
    positiveprompt: str = Form(...),
    negativeprompt: str = Form(...)
):

    image_data = await image.read()
    Inputimage = Image.open(io.BytesIO(image_data))
    Inputimage.save(INPUT_FILE)
    
    # Save the uploaded file
    responseimg = uncrop.getresult(left, top, right, bottom, positiveprompt, negativeprompt)
    responseimg.save(OUTPUT_FILE)

    # Return the processed image
    return FileResponse(OUTPUT_PATH, media_type="image/png", filename=OUTPUT_PATH.name)

@app.post("/rmbackground/")
async def rmBackgroundpost(
    image: UploadFile = File(...),
    model: str = Form(...)
):

    image_data = await image.read()
    Inputimage = Image.open(io.BytesIO(image_data))
    Inputimage.save(INPUT_FILE)
    
    # Save the uploaded file
    responseimg = rmBackground.getresult(model)
    responseimg.save(OUTPUT_FILE)

    # Return the processed image
    return FileResponse(OUTPUT_PATH, media_type="image/png", filename=OUTPUT_PATH.name)

@app.post("/upscale/")
async def upscalepost(
    image: UploadFile = File(...),
    upscaleby: int = Form(...),
    positiveprompt: str = Form(...),
    negativeprompt: str = Form(...)
):

    image_data = await image.read()
    Inputimage = Image.open(io.BytesIO(image_data))
    Inputimage.save(INPUT_FILE)
    
    # Save the uploaded file
    responseimg = upscale.getresult(upscaleby, positiveprompt, negativeprompt)
    responseimg.save(OUTPUT_FILE)

    # Return the processed image
    return FileResponse(OUTPUT_PATH, media_type="image/png", filename=OUTPUT_PATH.name)

@app.post("/qrcode/")
async def qrcodepost(
    qrcodeimage: UploadFile = File(...),
    refimage: UploadFile = File(...),
    weight_type: str = Form(...),
    qrmodelver: str = Form(...)
):

    image_data = await qrcodeimage.read()
    Inputimage = Image.open(io.BytesIO(image_data))
    Inputimage.save(INPUT_FILE)
    
    image_data2 = await refimage.read()
    Inputimage2 = Image.open(io.BytesIO(image_data2))
    Inputimage2.save(INPUT2_FILE)
    
    # Save the uploaded file
    responseimg = qrcode.getresult(weight_type, qrmodelver)
    responseimg.save(OUTPUT_FILE)

    # Return the processed image
    return FileResponse(OUTPUT_PATH, media_type="image/png", filename=OUTPUT_PATH.name)

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8082)