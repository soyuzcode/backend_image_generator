from .utils import upload_temp_image, call_p_api
import os
from dotenv import load_dotenv

load_dotenv()

def process_image_service(image_file, prompt:str|None=None):
    temp_link = upload_temp_image(image_file)
    #if not temp_link:
    #       return {"error": "Failed to upload temporary file"}

    processed_bytes = call_p_api("https://i.postimg.cc/g2Cg4SvW/image.png", TOKEN=os.getenv("API_TOKEN", ""), prompt=None)
    if not processed_bytes:
        return {"error": "API P failed"}
    
    return {"image_bytes": processed_bytes}
