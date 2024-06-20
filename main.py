from fastapi import FastAPI, HTTPException, File, UploadFile, Form
from fastapi.responses import FileResponse
from uncrop import getresult
import uvicorn
import io
from PIL import Image
from pathlib import Path

app = FastAPI()


INPUT_DIR = "input.png"
INPUT_PATH = Path("input.png")

OUTPUT_DIR = "result2.png"
OUTPUT_PATH = Path("result2.png")



app = FastAPI()

    

@app.post("/uncrop/")
async def uncropEP(
    file: UploadFile = File(...),
    left: int = Form(...),
    top: int = Form(...),
    right: int = Form(...),
    bottom: int = Form(...)
):
    
    image_data = await file.read()
    Inputimage = Image.open(io.BytesIO(image_data))
    Inputimage.save(INPUT_DIR)
    
    # Save the uploaded file
    responseimg = getresult(left, top, right, bottom)

    imageToSave = Image.open(io.BytesIO(responseimg.read()))
    imageToSave.save(OUTPUT_DIR)

    # Return the processed image
    return FileResponse(OUTPUT_PATH, media_type="image/jpeg", filename=OUTPUT_PATH.name)

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=3389)