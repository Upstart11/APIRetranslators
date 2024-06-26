from fastapi import FastAPI, File, UploadFile, Form
from fastapi.responses import FileResponse
import uncrop
import rmBackground
import upscale
import uvicorn
import io

from PIL import Image
from pathlib import Path

app = FastAPI()

INPUT_FILE = "Images/input.png"
INPUT_PATH = Path("Images/input.png")

OUTPUT_FILE = "Images/output.png"
OUTPUT_PATH = Path("Images/output.png")



app = FastAPI()

    

@app.post("/uncrop/")
async def uncropEP(
    file: UploadFile = File(...),
    left: int = Form(...),
    top: int = Form(...),
    right: int = Form(...),
    bottom: int = Form(...),
    positiveprompt: str = Form(...),
    negativeprompt: str = Form(...)
):

    image_data = await file.read()
    Inputimage = Image.open(io.BytesIO(image_data))
    Inputimage.save(INPUT_FILE)
    
    # Save the uploaded file
    responseimg = uncrop.getresult(left, top, right, bottom, positiveprompt, negativeprompt)
    responseimg.save(OUTPUT_FILE)

    # Return the processed image
    return FileResponse(OUTPUT_PATH, media_type="image/png", filename=OUTPUT_PATH.name)

@app.post("/rmbackground/")
async def rmBackground(
    file: UploadFile = File(...),
    model: str = Form(...)
):

    image_data = await file.read()
    Inputimage = Image.open(io.BytesIO(image_data))
    Inputimage.save(INPUT_FILE)
    
    # Save the uploaded file
    responseimg = rmBackground.getresult(model)
    responseimg.save(OUTPUT_FILE)

    # Return the processed image
    return FileResponse(OUTPUT_PATH, media_type="image/png", filename=OUTPUT_PATH.name)

@app.post("/upscale/")
async def rmBackground(
    file: UploadFile = File(...),
    upscaleby: int = Form(...),
    positiveprompt: str = Form(...),
    negativeprompt: str = Form(...)
):

    image_data = await file.read()
    Inputimage = Image.open(io.BytesIO(image_data))
    Inputimage.save(INPUT_FILE)
    
    # Save the uploaded file
    responseimg = upscale.getresult(upscaleby, positiveprompt, negativeprompt)
    responseimg.save(OUTPUT_FILE)

    # Return the processed image
    return FileResponse(OUTPUT_PATH, media_type="image/png", filename=OUTPUT_PATH.name)

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=3389)